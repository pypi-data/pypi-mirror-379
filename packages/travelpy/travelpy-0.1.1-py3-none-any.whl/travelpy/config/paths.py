"""Path configuration and TRAVEL executable management."""

import json
import os
from pathlib import Path
from typing import Dict, Optional

from travelpy.exceptions import ConfigurationError, TravelNotFoundError


def get_config_file_path() -> Path:
    """Get the path to the travelpy configuration file."""
    if os.name == "nt":  # Windows
        config_dir = Path(os.environ.get("APPDATA", "")) / "travelpy"
    else:  # Unix-like
        config_dir = Path.home() / ".config" / "travelpy"

    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / "config.json"


def set_travel_directory(path: str) -> None:
    """
    Set the TRAVEL installation directory permanently.

    Args:
        path: Path to TRAVEL installation directory (should contain Bin/Travel.exe)

    Raises:
        ConfigurationError: If path is invalid or Travel.exe not found in Bin
                           subdirectory
    """
    path_obj = Path(path)

    if not path_obj.exists():
        raise ConfigurationError(f"Directory does not exist: {path}")

    travel_exe = path_obj / "Bin" / "Travel.exe"
    if not travel_exe.exists():
        raise ConfigurationError(
            f"TRAVEL executable not found: {path}\\Bin\\Travel.exe"
        )

    # Save to config file
    config_file = get_config_file_path()
    config = {}
    if config_file.exists():
        try:
            config = json.loads(config_file.read_text())
        except json.JSONDecodeError:
            config = {}  # Start fresh if corrupted

    config["travel_directory"] = str(path_obj.absolute())
    config_file.write_text(json.dumps(config, indent=2))


def get_travel_directory() -> Optional[str]:
    """
    Get the configured TRAVEL installation directory.

    Returns:
        Path to TRAVEL directory, or None if not configured
    """
    config_file = get_config_file_path()
    if config_file.exists():
        try:
            config = json.loads(config_file.read_text())
            return config.get("travel_directory")
        except json.JSONDecodeError:
            return None
    return None


def get_travel_executable() -> str:
    """
    Get the TRAVEL executable, checking configured path and defaults.

    Returns:
        Full path to Travel.exe in Bin subdirectory

    Raises:
        TravelNotFoundError: If Travel.exe cannot be found
    """
    # First check configured path
    configured_path = get_travel_directory()
    if configured_path:
        travel_exe = Path(configured_path) / "Bin" / "Travel.exe"
        if travel_exe.exists():
            return str(travel_exe)

    # Check default location (your specified path)
    default_path = "C:\\Program Files (x86)\\Path Manager\\Travel"
    travel_exe = Path(default_path) / "Bin" / "Travel.exe"
    if travel_exe.exists():
        return str(travel_exe)

    # Check other common locations
    other_paths = [
        "C:\\Program Files\\Travel",
        "C:\\Travel",
        "D:\\Program Files\\Travel",
        "D:\\Travel",
    ]

    for path in other_paths:
        travel_exe = Path(path) / "Bin" / "Travel.exe"
        if travel_exe.exists():
            return str(travel_exe)

    # Not found anywhere
    raise TravelNotFoundError(
        "TRAVEL executable not found: please run "
        "travelpy.set_travel_directory('C:\\\\Program Files (x86)\\\\Path Manager\\\\Travel')"
    )


def find_conversion_tools(travel_directory: str) -> Dict[str, str]:
    """
    Find TRAVEL beam conversion tools in the installation directory.

    Args:
        travel_directory: Path to TRAVEL installation directory

    Returns:
        Dictionary mapping tool names to full paths of available executables
    """
    tools_dir = Path(travel_directory) / "Tools" / "BeamConversion"
    available_tools = {}

    tool_mapping = {
        "dat2dst": "Dat2Dst.exe",
        "dat2txt": "Dat2Txt.exe",
        "dst2dat": "Dst2Dat.exe",
        "dst2txt": "Dst2Txt.exe",
        "txt2dat": "Txt2Dat.exe",
    }

    for tool_name, exe_name in tool_mapping.items():
        tool_path = tools_dir / exe_name
        if tool_path.exists():
            available_tools[tool_name] = str(tool_path)

    return available_tools


def validate_travel_installation(travel_directory: str) -> Dict[str, any]:
    """
    Validate a complete TRAVEL installation.

    Args:
        travel_directory: Path to TRAVEL installation directory

    Returns:
        Dictionary with validation results containing:
        - travel_exe: Path to Travel.exe
        - conversion_tools: Dict of available conversion tools
        - valid: Boolean indicating if installation is valid

    Raises:
        ConfigurationError: If Travel.exe is not found
    """
    path_obj = Path(travel_directory)

    # Check main executable
    travel_exe = path_obj / "Bin" / "Travel.exe"
    if not travel_exe.exists():
        raise ConfigurationError(
            f"TRAVEL executable not found: {travel_directory}\\Bin\\Travel.exe"
        )

    # Find conversion tools (optional)
    conversion_tools = find_conversion_tools(travel_directory)

    return {
        "travel_exe": str(travel_exe),
        "conversion_tools": conversion_tools,
        "valid": True,
    }
