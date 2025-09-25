"""Config and settings management utilities for Bear Utils."""

from ._base_settings import BaseSetting, BaseSettingHandler
from .config_manager import ConfigManager
from .dir_manager import (
    DirectoryManager,
    clear_temp_directory,
    get_cache_path,
    get_config_path,
    get_local_config_path,
    get_settings_path,
    get_temp_path,
)
from .settings_manager import SettingsManager

__all__ = [
    "BaseSetting",
    "BaseSettingHandler",
    "ConfigManager",
    "DirectoryManager",
    "SettingsManager",
    "clear_temp_directory",
    "get_cache_path",
    "get_config_path",
    "get_local_config_path",
    "get_settings_path",
    "get_temp_path",
]
