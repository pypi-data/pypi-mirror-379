"""Helper functions to interact with evergreen."""

import os
import pathlib
from typing import List, Optional

import structlog
from evergreen import EvergreenApi, RetryingEvergreenApi

EVERGREEN_HOST = "https://evergreen.mongodb.com"
EVERGREEN_CONFIG_LOCATIONS = (
    # Common for machines in Evergreen
    os.path.join(os.getcwd(), ".evergreen.yml"),
    # Common for local machines
    os.path.expanduser(os.path.join("~", ".evergreen.yml")),
)

LOGGER = structlog.getLogger(__name__)


def _find_evergreen_yaml_candidates() -> List[str]:
    # Common for machines in Evergreen
    candidates = [os.getcwd()]

    cwd = pathlib.Path(os.getcwd())
    # add every path that is the parent of CWD as well
    for parent in cwd.parents:
        candidates.append(str(parent))

    # Common for local machines
    candidates.append(os.path.expanduser(os.path.join("~", ".evergreen.yml")))

    out = []
    for path in candidates:
        file = os.path.join(path, ".evergreen.yml")
        if os.path.isfile(file):
            out.append(file)

    return out


def get_evergreen_api(evergreen_config: Optional[str] = None) -> EvergreenApi:
    """
    Return evergreen API.

    :param evergreen_config: Path to Evergreen auth config.
    :return: Evergreen API client.
    """
    if evergreen_config:
        possible_configs = [evergreen_config]
    else:
        possible_configs = _find_evergreen_yaml_candidates()

    if not possible_configs:
        LOGGER.error("Could not find .evergreen.yml", candidates=possible_configs)
        raise RuntimeError("Could not find .evergreen.yml")

    last_ex = None
    for config in possible_configs:
        try:
            return RetryingEvergreenApi.get_api(config_file=config, log_on_error=True)
        except Exception as ex:
            last_ex = ex
            continue

    LOGGER.error(
        "Could not connect to Evergreen with any .evergreen.yml files available on this system",
        config_file_candidates=possible_configs,
    )
    if last_ex is not None:
        raise last_ex

    return RetryingEvergreenApi.get_api(log_on_error=True)
