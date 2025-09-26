"""
Simple TUI version compatibility check.
"""
import importlib.metadata
from typing import Optional, Tuple

from celestical.api.api.utils_api import UtilsApi
from celestical.api.api_client import ApiClient
from celestical.config import Config
from celestical.utils.display import print_console


def get_version() -> str:
    """ Get version number of the current celestical library.
    """
    tui_version = "0.0.0"
    try:
        tui_version = importlib.metadata.version('celestical')
    except importlib.metadata.PackageNotFoundError:
        logger = Config().logger
        logger.warning("Version could not be extracted")

    return tui_version


def check_tui_compatibility(config: Optional[Config] = None) -> Tuple[bool, str]:
    """Check if TUI version is compatible with API."""
    is_version_ok = True
    check_msg = "TUI version is compatible"
    tui_version = get_version()

    if config is None:
        config = Config()

    # API Conf without user's auth info
    apiconf = config.api_configuration()

    try:
        api_client = ApiClient(apiconf)
        utils_api = UtilsApi(api_client=api_client)

        # API Call
        version_info = utils_api.version_check_u_versioncheck_get()

        if tui_version < version_info.min_version:
            is_version_ok = False
            check_msg = (f"TUI version update required. Current: {tui_version}, "
                        f"Minimum: {version_info.min_version}")
    #except (OSError, ValueError, AttributeError, KeyError):
    except Exception:
        return True, "TUI version check failed, continuing anyway"

    return is_version_ok, check_msg


def check_cli_version(silent=True) -> bool:
    """
    Check if the CLI version is compatible with the API.
    Returns True if compatible, False if update is required.
    """
    is_compatible, message = check_tui_compatibility()
    if not silent:
        print_console(message)
    return is_compatible
