"""Default settings and configuration constants."""

import json
from pathlib import Path
from typing import Any, Dict

from travelpy.config.paths import get_config_file_path

# Default directory names
DEFAULT_RESULTS_DIRECTORY = "./results"

# Default timeout for TRAVEL simulations (seconds)
DEFAULT_SIMULATION_TIMEOUT = 600  # 10 minutes


# Settings persistence
def get_settings() -> Dict[str, Any]:
    """
    Get all travelpy settings from config file.

    Returns:
        Dictionary with all settings, using defaults for missing values
    """
    defaults = {
        "results_directory": DEFAULT_RESULTS_DIRECTORY,
        "simulation_timeout": DEFAULT_SIMULATION_TIMEOUT,
    }

    config_file = get_config_file_path()
    if config_file.exists():
        try:
            config = json.loads(config_file.read_text())
            # Merge with defaults, keeping any extra settings
            merged_settings = defaults.copy()
            merged_settings.update(config)
            return merged_settings
        except json.JSONDecodeError:
            # Return defaults if config is corrupted
            return defaults

    return defaults


def save_settings(settings: Dict[str, Any]) -> None:
    """
    Save settings to config file, preserving other configuration values.

    Args:
        settings: Dictionary of settings to save
    """
    config_file = get_config_file_path()

    # Load existing config to preserve other values (like travel_directory)
    existing_config = {}
    if config_file.exists():
        try:
            existing_config = json.loads(config_file.read_text())
        except json.JSONDecodeError:
            existing_config = {}

    # Update with new settings
    existing_config.update(settings)

    # Save updated config
    config_file.write_text(json.dumps(existing_config, indent=2))


def get_results_directory() -> str:
    """
    Get the configured results directory.

    Returns:
        Path to results directory
    """
    settings = get_settings()
    return settings.get("results_directory", DEFAULT_RESULTS_DIRECTORY)


def set_results_directory(directory: str) -> None:
    """
    Set the results directory and create it if it doesn't exist.

    Args:
        directory: Path to results directory
    """
    # Create directory if it doesn't exist
    results_path = Path(directory)
    if not results_path.exists():
        results_path.mkdir(parents=True, exist_ok=True)

    # Get current settings and update
    current_settings = get_settings()
    current_settings["results_directory"] = directory
    save_settings(current_settings)
