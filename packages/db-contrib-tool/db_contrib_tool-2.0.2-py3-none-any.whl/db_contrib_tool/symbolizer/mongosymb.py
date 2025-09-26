"""Script for symbolizing MongoDB stack traces."""

from __future__ import annotations

from functools import lru_cache
import json
import os
import signal
import subprocess
import sys
import time
from enum import Enum
from typing import IO, Any, AnyStr, Dict, List, NamedTuple, Optional, TextIO, Tuple
from urllib.parse import urlparse

import inject
import requests
from tenacity import Retrying, retry_if_result, stop_after_delay, wait_fixed

from db_contrib_tool.clients.io_client import IOClient
from db_contrib_tool.clients.download_client import DownloadClient
from db_contrib_tool.config import SETUP_REPRO_ENV_CONFIG
from db_contrib_tool.services.evergreen_service import EvergreenService
from db_contrib_tool.symbolizer.mongo_log_parser_service import (
    BINARY_LOAD_ADDRESS_KEY,
    BUILD_ID_KEY,
    MongoLogParserService,
    SoInfo,
    TraceDoc,
)
from db_contrib_tool.utils.build_system_options import PathOptions
from db_contrib_tool.utils.evergreen_conn import get_evergreen_api
from db_contrib_tool.utils.oauth import (
    Configs,
    get_client_cred_oauth_credentials,
    get_oauth_credentials,
)

SYMBOLIZER_PATH_ENV = "MONGOSYMB_SYMBOLIZER_PATH"
DEFAULT_SYMBOLIZER_PATH = "/opt/mongodbtoolchain/v4/bin/llvm-symbolizer"


class BuildData(NamedTuple):
    """Model for data returned by symbolizer service."""

    url: Optional[str] = None
    debug_symbols_url: Optional[str] = None
    file_name: Optional[str] = None

    @classmethod
    def from_response_data(cls, data: Dict[str, Any]) -> BuildData:
        """
        Make build data from symbolizer service response data.

        :param data: Symbolizer service response data
        :return: Build data.
        """
        return cls(
            url=data.get("url"),
            debug_symbols_url=data.get("debug_symbols_url"),
            file_name=data.get("file_name"),
        )

    def is_san_build(self) -> bool:
        """
        Check whether this is a sanitizer build.

        Sanitizer build binary files has debug symbols, so
        if URL to binaries and URL to debug symbols is the same,
        this is a sanitizer build.

        :return: True if sanitizer build.
        """
        return self.url == self.debug_symbols_url


class PathResolver(object):
    """
    Class to find path for given buildId.

    We'll be sending request each time to another server to get path.
    This process is fairly small, but can be heavy in case of increased amount of requests per second.
    Thus, I'm implementing a caching mechanism (as a suggestion).
    It keeps track of the last N results from server, we always try to search from that cache, if not found then send
    request to server and cache the response for further usage.
    Cache size differs according to the situation, system resources and overall decision of development team.
    """

    # the main (API) sever that we'll be sending requests to
    default_host = "https://symbolizer-service.server-tig.prod.corp.mongodb.com"
    default_cache_dir = os.path.join(os.getcwd(), "build", "symbolizer_downloads_cache")
    default_creds_file_path = os.path.join(os.getcwd(), ".symbolizer_credentials.json")
    default_client_credentials_scope = "servertig-symbolizer-fullaccess"
    default_client_credentials_user_name = "client-user"

    def __init__(
        self,
        host: Optional[str] = None,
        cache_dir: Optional[str] = None,
        client_credentials_scope: Optional[str] = None,
        client_credentials_user_name: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_port: Optional[int] = None,
        scope: Optional[str] = None,
        auth_domain: Optional[str] = None,
    ):
        """
        Initialize instance.

        :param host: URL of web service running the API to get debug symbol URL.
        :param cache_dir: Full path to a directory to store cache/files.
        :param client_credentials_scope: Client credentials scope.
        :param client_credentials_user_name: Client credentials username.
        :param client_id: Client id for Okta Oauth.
        :param client_secret: Secret key for Okta Oauth.
        :param redirect_port: Redirect port.
        :param scope: Auth scope.
        :param auth_domain: Auth domain.
        """
        self.host = host or self.default_host
        self.cache_dir = cache_dir or self.default_cache_dir
        self.client_credentials_scope = (
            client_credentials_scope or self.default_client_credentials_scope
        )
        self.client_credentials_user_name = (
            client_credentials_user_name or self.default_client_credentials_user_name
        )
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_port = redirect_port
        self.scope = scope
        self.auth_domain = auth_domain
        self.configs = Configs(
            client_credentials_scope=self.client_credentials_scope,
            client_credentials_user_name=self.client_credentials_user_name,
            client_id=self.client_id,
            auth_domain=self.auth_domain,
            redirect_port=self.redirect_port,
            scope=self.scope,
        )
        self.http_client = requests.Session()
        self.path_options = PathOptions()
        self.evergreen_service = EvergreenService(
            evg_api=get_evergreen_api(), setup_repro_config=SETUP_REPRO_ENV_CONFIG
        )

        # create cache dir if it doesn't exist
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

        self.authenticate()

    def authenticate(self) -> None:
        """Login & get credentials for further requests to web service."""
        # try to read from file
        if os.path.exists(self.default_creds_file_path):
            with open(self.default_creds_file_path) as cfile:
                data = json.loads(cfile.read())
                access_token, expire_time = data.get("access_token"), data.get("expire_time")
                if time.time() < expire_time:
                    # credentials not expired yet
                    self.http_client.headers.update({"Authorization": f"Bearer {access_token}"})
                    return

        if self.client_id and self.client_secret:
            # auth using secrets
            credentials = get_client_cred_oauth_credentials(
                self.client_id, self.client_secret, self.configs
            )
        else:
            # since we don't have access to secrets, ask user to auth manually
            credentials = get_oauth_credentials(configs=self.configs, print_auth_url=True)

        self.http_client.headers.update({"Authorization": f"Bearer {credentials.access_token}"})

        # write credentials to local file for further usage
        with open(self.default_creds_file_path, "w") as cfile:
            cfile.write(
                json.dumps(
                    {
                        "access_token": credentials.access_token,
                        "expire_time": time.time() + credentials.expires_in,
                    }
                )
            )

    @staticmethod
    def is_valid_path(path: str) -> bool:
        """
        Sometimes the given path may not be valid: e.g: path for a non-existing file.

        If we need to do extra checks on path, we'll do all of them here.

        :param path: Path string.
        :return: Bool indicating the validation status.
        """
        return os.path.exists(path)

    @staticmethod
    def url_to_filename(url: str) -> str:
        """
        Convert URL to local filename.

        :param url: Download URL.
        :return: Full name for local file.
        """
        parsed = urlparse(url)
        return parsed.path.split("/")[-1]

    @staticmethod
    def unpack(path: str) -> str:
        """
        Use to utar/unzip files.

        :param path: Full path of file.
        :return: Full path of 'bin' directory of unpacked file.
        """
        out_dir = path.replace(".tgz", "", 1)
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        args = ["tar", "xopf", path, "-C", out_dir, "--strip-components 1"]
        cmd = " ".join(args)
        subprocess.check_call(cmd, shell=True)

        return out_dir

    def download(self, url: str) -> Tuple[str, bool]:
        """
        Use to download file from URL.

        :param url: URL string.
        :return: Full path of downloaded file in local filesystem, bool indicating if file is already downloaded or not.
        """
        exists_locally = False
        filename = self.url_to_filename(url)
        path = os.path.join(self.cache_dir, filename)
        if not os.path.exists(path):
            DownloadClient.download_from_url(url, path)
        else:
            print("File already exists in cache")
            exists_locally = True
        return path, exists_locally

    def get_dbg_file(self, soinfo: SoInfo) -> Optional[str]:
        """
        To get path for given buildId.

        :param soinfo: Information about process that printed backtrace.
        :return: Path as string or None (if path not found).
        """
        build_id = soinfo.build_id.lower() if soinfo.build_id is not None else ""
        version = soinfo.mongodb_version
        try:
            search_parameters = {"build_id": build_id}
            if version:
                search_parameters["version"] = version
            print(f"Getting data from service... Search parameters: {search_parameters}")
            response = self.http_client.get(f"{self.host}/find_by_id", params=search_parameters)
            if response.status_code != 200:
                sys.stderr.write(
                    f"Server returned unsuccessful status: {response.status_code}, "
                    f"response body: {response.text}\n"
                )
                return None
            else:
                data = response.json().get("data", {})
                build_data = BuildData.from_response_data(data)
        except Exception as err:  # noqa
            sys.stderr.write(
                f"Error occurred while trying to get response from server "
                f"for buildId({build_id}): {err}\n"
            )
            return None

        if build_data.debug_symbols_url is None:
            return None

        if DownloadClient.is_s3_url(
            build_data.debug_symbols_url
        ) and DownloadClient.is_s3_presigned_url(build_data.debug_symbols_url):
            build_data = build_data._replace(
                debug_symbols_url=self.get_refreshed_debug_symbols_url(build_data.debug_symbols_url)
            )

        if build_data.debug_symbols_url is None:
            return None

        try:
            dl_path, exists_locally = self.download(build_data.debug_symbols_url)
            if exists_locally:
                path = dl_path.replace(".tgz", "", 1)
            else:
                sys.stdout.write("Downloaded, now unpacking...\n")
                path = self.unpack(dl_path)
        except Exception as err:  # noqa
            sys.stderr.write(f"Failed to download & unpack file: {err}\n")
            return None

        binary_name = build_data.file_name or "mongo"
        # Regular builds have separate file with debug symbols and for linux builds it has "<binary-name>.debug" name.
        # Sanitizer builds have debug symbols in the same binary file.
        # Symbolizer service returns us the name of the file the build id was extracted from.
        # If it is a regular build and the binary file name is returned
        # we need to append ".debug" to it to get the debug symbols file name.
        if not build_data.is_san_build() and not binary_name.endswith(".debug"):
            binary_name = f"{binary_name}.debug"

        inner_folder_name = self.path_options.get_binary_folder_name(binary_name)

        return os.path.join(path, inner_folder_name, binary_name)

    @lru_cache(maxsize=8)
    def get_refreshed_debug_symbols_url(self, url: str) -> str:
        """
        Tries to find a new pre-signed download URL from Evergreen. If unable, returns the original URL.

        Detail: Evergreen can provide pre-signed URLs for S3 objects that are otherwise private,
        allowing downloads without any AWS credentials. The URL contains the necessary authorization,
        but is only valid for a short duration, and will likely have expired between when it was
        created and when `db-contrib-tool symbolize` is being used. If expired, the download will fail.
        To avoid this, re-retrieve the artifact URLS from Evergreen for the task it was originally from.
        It will again be a presigned URL, but with a newer expiration.
        """
        _, key = DownloadClient.extract_s3_bucket_key(url)
        # The debug artifact path is assumed to be project/variant/version_id/...
        parts = key.split("/")
        if len(parts) < 3:
            return url
        variant = parts[1]
        version = self.evergreen_service.get_version(parts[2])
        urls = self.evergreen_service.get_compile_artifact_urls(
            version, variant, ignore_failed_push=True
        )
        if not urls:
            return url
        return urls.urls.get("mongo-debugsymbols.tgz", url)


class InputFormat(str, Enum):
    """Input mongo log format types."""

    CLASSIC = "classic"
    THIN = "thin"


class OutputFormat(str, Enum):
    """Output format types."""

    CLASSIC = "classic"
    JSON = "json"


class SymbolizerParameters(NamedTuple):
    """
    Parameters describing how logs should be symbolized.

    * symbolizer_path: Symbolizer executable path.
    * dsym_hint: List of `-dsym-hint` flag values to pass to symbolizer.

    * input_format: Input mongo log format.
    * output_format: Output format.

    * live: Whether it should enter live mode.

    * host: URL of web service running the API to get debug symbol URL.
    * cache_dir: Full path to a directory to store cache/files.
    * total_seconds_for_retries: Timeout for getting data from web service.

    * client_secret: Secret key for Okta Oauth.
    * client_id: Client id for Okta Oauth.
    """

    symbolizer_path: Optional[str]
    dsym_hint: List[str]

    input_format: InputFormat
    output_format: OutputFormat

    live: bool

    host: Optional[str]
    cache_dir: Optional[str]
    total_seconds_for_retries: int

    client_secret: Optional[str]
    client_id: Optional[str]


class SymbolizerOrchestrator:
    """Orchestrator for log symbolizer."""

    @inject.autoparams()
    def __init__(
        self,
        mongo_log_parser_service: MongoLogParserService,
        io_client: IOClient,
        dbg_path_resolver: PathResolver,
    ) -> None:
        """
        Initialize.

        :param mongo_log_parser_service: Service to parse backtraces in log files.
        :param io_client: Client for working with input/output.
        :param dbg_path_resolver: Debug symbols file path resolver.
        """
        self.mongo_log_parser_service = mongo_log_parser_service
        self.io_client = io_client
        self.dbg_path_resolver = dbg_path_resolver

    def substitute_stdin(self, params: SymbolizerParameters) -> None:
        """
        Accept stdin stream as source of logs and symbolize it.

        :param params: Symbolizer parameters.
        """
        # Ignore Ctrl-C. When the process feeding the pipe exits, `stdin` will be closed.
        signal.signal(signal.SIGINT, signal.SIG_IGN)

        print("Live mode activated, waiting for input...")
        global_base_addr_map: Dict[str, SoInfo] = {}
        while True:
            backtrace_indicator = '{"backtrace":'
            line = sys.stdin.readline()
            if not line:
                return

            line = line.strip()

            if "Frame: 0x" in line:
                continue

            if backtrace_indicator in line:
                backtrace_index = line.index(backtrace_indicator)
                prefix = line[:backtrace_index]
                trace_docs = self.mongo_log_parser_service.parse_log_lines(
                    line, global_base_addr_map
                )
                if len(trace_docs) == 0:
                    print("Could not find json backtrace object in input...")
                    continue
                for trace_doc in trace_docs:
                    frames = self.symbolize_frames(trace_doc, params)
                    print(prefix)
                    print("Symbolizing...")
                    self.classic_output(frames, sys.stdout)
                    global_base_addr_map = trace_doc.base_addr_map
                print("Symbolization completed, waiting for input...")
            else:
                print(line)

    def execute(self, params: SymbolizerParameters) -> bool:
        """
        Execute symbolizer.

        :param params: Symbolizer parameters.
        :return: Whether succeeded or not.
        """
        if params.live:
            print("Entering live mode")
            self.substitute_stdin(params)
            return True

        log_lines = self.io_client.read_from_stdin()
        if not log_lines or not log_lines.strip():
            print(
                "Please provide the backtrace through stdin for symbolization;"
                "e.g. `your/symbolization/command < /file/with/stacktrace`"
            )

        trace_docs = self.mongo_log_parser_service.parse_log_lines(log_lines)
        if len(trace_docs) == 0:
            print("Could not find json backtrace object in input", file=sys.stderr)
            return False

        for trace_doc in trace_docs:
            frames = self.symbolize_frames(trace_doc, params)
            if params.output_format == OutputFormat.JSON:
                json.dump(frames, sys.stdout, indent=2)
            elif params.output_format == OutputFormat.CLASSIC:
                self.classic_output(frames, sys.stdout)

        return True

    def produce_frames(self, trace_doc: TraceDoc) -> List[Dict[str, Any]]:
        """
        Return a list of frame dicts from an object of trace doc.

        :param trace_doc: Traceback doc.
        :return: List of traceback frames.
        """
        frames = []
        for frame in trace_doc.backtrace:
            if BINARY_LOAD_ADDRESS_KEY not in frame:
                print(
                    f"Ignoring frame {frame} as it's missing the `{BINARY_LOAD_ADDRESS_KEY}` field;"
                    f" See SERVER-58863 for discussions"
                )
                continue
            soinfo = trace_doc.base_addr_map.get(frame[BINARY_LOAD_ADDRESS_KEY], SoInfo())
            if soinfo.elf_type == 3:
                addr_base = "0"
            elif soinfo.elf_type == 2:
                addr_base = frame[BINARY_LOAD_ADDRESS_KEY]
            else:
                addr_base = soinfo.vmaddr if soinfo.vmaddr is not None else "0"
            addr = int(addr_base, 16) + int(frame["o"], 16)
            # addr currently points to the return address which is the one *after* the call. x86 is
            # variable length so going backwards is difficult. However, llvm-symbolizer seems to do the
            # right thing if we just subtract 1 byte here. This has the downside of also adjusting the
            # address of instructions that cause signals (such as segfaults and divide-by-zero) which
            # are already correct, but there doesn't seem to be a reliable way to detect that case.
            addr -= 1
            frames.append(
                dict(
                    path=self.dbg_path_resolver.get_dbg_file(soinfo),
                    buildId=soinfo.build_id,
                    offset=frame["o"],
                    addr="0x{:x}".format(addr),
                    symbol=frame.get("s", None),
                )
            )
        return frames

    def symbolize_frames(
        self, trace_doc: TraceDoc, params: SymbolizerParameters
    ) -> List[Dict[str, Any]]:
        """
        Return a list of symbolized stack frames from a trace_doc in MongoDB stack dump format.

        :param trace_doc: Traceback doc.
        :param params: Symbolizer parameters.
        :return: List of traceback frames.
        """
        frames = self.preprocess_frames_with_retries(
            trace_doc,
            params.input_format,
            params.total_seconds_for_retries,
        )

        symbolizer_path = params.symbolizer_path
        if not symbolizer_path:
            symbolizer_path = os.environ.get(SYMBOLIZER_PATH_ENV)
            if not symbolizer_path:
                print(
                    f"Env value for '{SYMBOLIZER_PATH_ENV}' not found, using '{DEFAULT_SYMBOLIZER_PATH}' "
                    f"as a defualt executable path."
                )
                symbolizer_path = DEFAULT_SYMBOLIZER_PATH

        symbolizer_args = [symbolizer_path]
        for dh in params.dsym_hint:
            symbolizer_args.append("-dsym-hint={}".format(dh))
        symbolizer_process = subprocess.Popen(
            args=symbolizer_args,
            close_fds=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=sys.stdout,
        )

        for frame in frames:
            if frame["path"] is None:
                print("Path not found in frame:", frame)
                continue
            if symbolizer_process.stdin:
                symbol_line = "CODE {path:} {addr:}\n".format(**frame)
                symbolizer_process.stdin.write(symbol_line.encode())
                symbolizer_process.stdin.flush()
            if symbolizer_process.stdout:
                frame["symbinfo"] = self.extract_symbols(symbolizer_process.stdout)
        if symbolizer_process.stdin:
            symbolizer_process.stdin.close()
        symbolizer_process.wait()
        return frames

    def extract_symbols(self, stdout: IO[AnyStr]) -> List[Dict[str, Any]]:
        """
        Extract symbol information from the output of llvm-symbolizer.

        Return a list of dictionaries, each of which has fn, file, column and line entries.

        The format of llvm-symbolizer output is that for every CODE line of input,
        it outputs zero or more pairs of lines, and then a blank line. This way, if
        a CODE line of input maps to several inlined functions, you can use the blank
        line to find the end of the list of symbols corresponding to the CODE line.

        The first line of each pair contains the function name, and the second contains the file,
        column and line information.

        :param stdout: Output of llvm-symbolizer.
        :return: List of symbol information.
        """
        result: List[Dict[str, Any]] = []
        step = 0
        while True:
            line = self.ensure_str(stdout.readline())
            if line == "\n":
                break
            if step == 0:
                result.append({"fn": line.strip()})
                step = 1
            else:
                file_name, line, column = line.strip().rsplit(":", 3)
                result[-1].update({"file": file_name, "column": int(column), "line": int(line)})
                step = 0
        return result

    @staticmethod
    def ensure_str(any_str: AnyStr) -> str:
        """
        Convert AnyStr to str.

        :param any_str: AnyStr line.
        :return: Line as str
        """
        if hasattr(any_str, "decode"):
            return any_str.decode()
        return str(any_str)

    def preprocess_frames(
        self, trace_doc: TraceDoc, input_format: InputFormat
    ) -> List[Dict[str, Any]]:
        """
        Process the paths in frame objects.

        :param trace_doc: Traceback doc.
        :param input_format: Input format.
        :return: List of traceback frames.
        """
        if input_format == InputFormat.CLASSIC:
            return self.produce_frames(trace_doc)
        elif input_format == InputFormat.THIN:
            frames = trace_doc.backtrace
            for frame in frames:
                soinfo = SoInfo(build_id=frame.get(BUILD_ID_KEY))
                frame["path"] = self.dbg_path_resolver.get_dbg_file(soinfo)
            return frames
        return []

    @staticmethod
    def has_high_not_found_paths_ratio(frames: List[Dict[str, Any]]) -> bool:
        """
        Check whether not found paths in frames ratio is higher than 0.5.

        :param frames: the list of traceback frames
        :return: True if ratio is higher than 0.5
        """
        not_found = [1 for f in frames if f.get("path") is None]
        not_found_ratio = len(not_found) / (len(frames) or 1)
        return not_found_ratio >= 0.5

    def preprocess_frames_with_retries(
        self,
        trace_doc: TraceDoc,
        input_format: InputFormat,
        total_seconds_for_retries: int = 0,
    ) -> List[Dict[str, Any]]:
        """
        Process the paths in frame objects.

        :param trace_doc: Traceback doc.
        :param input_format: Input format.
        :param total_seconds_for_retries: Timeout for retries.
        :return: List of traceback frames.
        """
        retrying = Retrying(
            retry=retry_if_result(self.has_high_not_found_paths_ratio),
            wait=wait_fixed(60),
            stop=stop_after_delay(total_seconds_for_retries),
            retry_error_callback=lambda retry_state: retry_state.outcome.result(),  # type: ignore
        )

        return retrying(self.preprocess_frames, trace_doc, input_format)

    @staticmethod
    def classic_output(frames: List[Dict[str, Any]], outfile: TextIO) -> None:
        """
        Provide classic output.

        :param frames: List of traceback frames.
        :param outfile: Output text file stream.
        """
        for frame in frames:
            symbinfo = frame.get("symbinfo")
            if symbinfo:
                for sframe in symbinfo:
                    outfile.write(" {file:s}:{line:d}:{column:d}: {fn:s}\n".format(**sframe))
            else:
                outfile.write(
                    " Couldn't extract symbols: path={path}\n".format(
                        path=frame.get("path", "no value found")
                    )
                )
