"""Main simulation runner and public API."""

import shutil
import subprocess
from pathlib import Path
from typing import Optional

from travelpy.config.paths import get_travel_executable
from travelpy.exceptions import TravelNotFoundError
from travelpy.results.result import Result


def _validate_input_files(beam_file: str, beamline_file: str) -> None:
    """Validate input file existence and formats."""
    beam_path = Path(beam_file)
    beamline_path = Path(beamline_file)

    # Check file existence
    if not beam_path.exists():
        raise FileNotFoundError(f"Beam file not found: {beam_file}")

    if not beamline_path.exists():
        raise FileNotFoundError(f"Beamline file not found: {beamline_file}")

    # Check beam file format
    beam_suffix = beam_path.suffix.lower()
    if beam_suffix != ".dat":
        raise ValueError(
            f"Unsupported beam file format '{beam_suffix}': only .dat (TRAVEL format) files are supported"
        )

    # Check beamline file format
    beamline_suffix = beamline_path.suffix.lower()
    if beamline_suffix != ".in":
        raise ValueError(
            f"Unsupported beamline file format '{beamline_suffix}': only .in files are supported"
        )


def _get_travel_executable(travel_exe: Optional[str] = None) -> str:
    """Get TRAVEL executable path, either custom or auto-detected."""
    if travel_exe:
        # Validate custom executable
        travel_path = Path(travel_exe)
        if not travel_path.exists():
            raise TravelNotFoundError(
                f"Custom TRAVEL executable not found: {travel_exe}"
            )
        return travel_exe
    else:
        # Auto-detect TRAVEL executable
        return get_travel_executable()


def _prepare_workspace(workspace_directory: Optional[str]) -> Path:
    """Prepare workspace directory for TRAVEL execution."""
    if workspace_directory:
        # Use custom workspace directory
        workspace_path = Path(workspace_directory)
        workspace_path.mkdir(parents=True, exist_ok=True)
    else:
        # Use current directory
        workspace_path = Path.cwd()

    return workspace_path


def _parse_output_cards(beamline_file: str) -> list[str]:
    """
    Parse beamline file to detect output files from cards 32-39.

    Extracts filenames from TRAVEL output cards:
    - Card 32 (REFERENCE PARTICLE OUTPUT): reference particle evolution
    - Card 33 (BEAM CENTER (AVG) OUTPUT): average beam properties along beamline
    - Card 34 (RMS OUTPUT): RMS beam properties along beamline
    - Card 35 (SINGLE PARTICLE TRACKING): individual particle trajectory
    - Card 36 (BEAM OUTPUT EXCEL FORMAT): beam dump in Excel format
    - Card 37 (BEAM OUTPUT TRAVEL FORMAT): beam dump in TRAVEL .dat format
    - Card 38 (BEAM OUTPUT PARMILAS FORMAT): beam dump in PARMILAS .dst format
    - Card 39 (BEAM OUTPUT TXT FORMAT): beam dump in text format

    Args:
        beamline_file: Path to beamline (.in) file

    Returns:
        List of output filenames that will be created by TRAVEL

    Examples:
        >>> _parse_output_cards("test.in")  # doctest: +SKIP
        ["reference.txt", "avgout.txt", "rmsout.txt", "beam.xls"]
    """
    import re

    output_files = []

    try:
        with open(beamline_file, "r") as f:
            for line in f:
                # Skip comment lines (start with 'c')
                stripped = line.strip()
                if not stripped or stripped.startswith("c"):
                    continue

                # Split line into parts, handling quotes
                parts = line.split()
                if not parts:
                    continue

                # Check for output cards 32-39
                card_number = parts[0]
                if card_number in ["32", "33", "34", "35", "36", "37", "38", "39"]:
                    # All output cards have filename in single quotes
                    filename_match = re.search(r"'([^']+)'", line)
                    if filename_match:
                        output_files.append(filename_match.group(1))
                    # If no filename found, skip - card is malformed

    except FileNotFoundError:
        # File doesn't exist - return empty list
        return []

    return output_files


def _collect_results(
    workspace_path: Path,
    results_directory: str,
    beamline_file: str,
    beam_file: str,
) -> Path:
    """
    Collect TRAVEL output files to results directory using hybrid detection.

    Uses both beamline analysis and directory monitoring to find all output files:
    1. Parse beamline file to detect expected outputs (cards 33, 34, 36-39)
    2. Scan workspace for any additional files created during simulation
    3. Copy all detected files to results directory

    Args:
        workspace_path: Directory where TRAVEL executed
        results_directory: Target directory for collected results
        beamline_file: Original beamline file path for output card parsing
        beam_file: Original beam file path for exclusion from results

    Returns:
        Path to results directory
    """
    results_path = Path(results_directory)
    results_path.mkdir(parents=True, exist_ok=True)

    # Step 1: Parse beamline to detect expected output files
    expected_outputs = _parse_output_cards(beamline_file)

    # Step 2: Move expected output files if they exist
    # NOTE: TRAVEL converts all filenames to UPPERCASE, so we need to check both cases
    moved_files = set()
    for output_file in expected_outputs:
        # Try original case first
        src_file = workspace_path / output_file
        if src_file.exists():
            shutil.move(src_file, results_path / output_file)
            moved_files.add(output_file)
        else:
            # Try uppercase version (TRAVEL's actual output)
            uppercase_file = output_file.upper()
            src_file_upper = workspace_path / uppercase_file
            if src_file_upper.exists():
                # Move with the original filename from beamline (preserve user's intent)
                shutil.move(src_file_upper, results_path / output_file)
                moved_files.add(
                    uppercase_file
                )  # Track the actual file name that was moved

    # Step 3: Directory monitoring - find other output files created during simulation
    # Exclude input files from being moved to results directory (case-insensitive)
    beam_basename = Path(beam_file).name
    beamline_basename = Path(beamline_file).name
    input_basenames_lower = {beam_basename.lower(), beamline_basename.lower()}

    for file_path in workspace_path.iterdir():
        if (
            file_path.is_file()
            and file_path.name not in moved_files
            and file_path.name.lower() not in input_basenames_lower
        ):
            # Skip temporary files and common non-output files
            if not file_path.name.startswith(".") and file_path.suffix.lower() in {
                ".txt",
                ".out",
                ".dat",
                ".dst",
                ".xls",
            }:
                shutil.move(file_path, results_path / file_path.name)
                moved_files.add(file_path.name)

    return results_path


def run_travel(
    beam_file: str,
    beamline_file: str,
    *,
    results_directory: Optional[str] = None,
    workspace_directory: Optional[str] = None,
    timeout: Optional[int] = None,
    travel_exe: Optional[str] = None,
    show_popup: bool = False,
) -> Result:
    """
    Run a TRAVEL particle tracking simulation.

    Args:
        beam_file: Path to beam file (.dat TRAVEL format)
        beamline_file: Path to beamline file (.in format)
        results_directory: Directory to save final results (default: same as workspace)
        workspace_directory: Directory where TRAVEL executes (default: current
                            directory).
                            Useful for organizing workspaces or avoiding path issues.
        timeout: Simulation timeout in seconds (default from config).
                TRAVEL simulations can run for hours on complex beamlines.
                Prevents hanging processes and enables batch processing limits.
        travel_exe: Path to custom TRAVEL executable (rarely needed).
                   Default: auto-detected from TRAVEL installation.
                   Use case: TRAVEL developers testing different versions or
                   users with multiple TRAVEL installations.
        show_popup: Show TRAVEL terminal popup window during simulation
                   (default: False).
                   When False: TRAVEL runs silently in background (recommended).
                   When True: Shows traditional TRAVEL console window.
                   Useful for debugging or monitoring simulation progress.

    Returns:
        Result: Object containing simulation outputs and analysis methods.
                Provides access to AVGOUT.txt, RMSOUT.txt, and other TRAVEL outputs
                with built-in plotting and analysis capabilities.

    Raises:
        TravelNotFoundError: TRAVEL executable not found in system PATH or
                            specified location. Check TRAVEL installation.
        SimulationError: TRAVEL simulation failed (non-zero exit code),
                        timed out, or encountered execution errors.
        FileNotFoundError: Input beam or beamline files don't exist.
        ValueError: Unsupported beam file format or beam conversion failure.

    Examples:
        Basic usage with .dat file:
        >>> result = run_travel("beam.dat", "beamline.in")  # doctest: +SKIP




        Custom workspace and timeout:
        >>> result = run_travel("beam.dat", "complex_beamline.in",  # doctest: +SKIP
        ...                     workspace_directory="./my_workspace",
        ...                     timeout=3600)  # doctest: +SKIP

        Show TRAVEL popup window for debugging:
        >>> result = run_travel("beam.dat", "beamline.in",  # doctest: +SKIP
        ...                     show_popup=True)

        Hide popup (default behavior):
        >>> result = run_travel("beam.dat", "beamline.in",  # doctest: +SKIP
        ...                     show_popup=False)  # or omit parameter
    """
    import time

    from travelpy.exceptions import SimulationError

    # Validate input files
    _validate_input_files(beam_file, beamline_file)

    # Get TRAVEL executable path
    travel_executable = _get_travel_executable(travel_exe)

    # Prepare workspace
    workspace_path = _prepare_workspace(workspace_directory)

    # Set default results directory to workspace directory if not specified
    if results_directory is None:
        results_directory = str(workspace_path)

    # Use absolute paths to original files
    beam_path = Path(beam_file).resolve()
    beamline_path = Path(beamline_file).resolve()
    beam_arg = str(beam_path)
    beamline_arg = str(beamline_path)

    # Run TRAVEL simulation
    start_time = time.time()
    try:
        # Prepare TRAVEL command with appropriate file arguments
        command = [travel_executable, beam_arg, beamline_arg]

        # Configure window visibility
        startupinfo = None
        if not show_popup:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE

        result = subprocess.run(
            command,
            cwd=str(workspace_path),
            capture_output=True,
            text=True,
            timeout=timeout,
            startupinfo=startupinfo,
        )

        if result.returncode != 0:
            # Try to get TRAVEL.OUT contents for detailed error information
            travel_out_path = workspace_path / "TRAVEL.OUT"
            error_msg = f"TRAVEL simulation failed with exit code {result.returncode}"
            error_msg += f"\nCommand: {' '.join(command)}"
            error_msg += f"\nWorking directory: {workspace_path}"
            beam_exists = Path(beam_arg).exists()
            beamline_exists = Path(beamline_arg).exists()
            error_msg += f"\nBeam file exists: {beam_exists}"
            error_msg += f"\nBeamline file exists: {beamline_exists}"

            if travel_out_path.exists():
                try:
                    travel_out_content = travel_out_path.read_text()
                    if travel_out_content.strip():
                        # Show last 1000 characters of TRAVEL.OUT for context
                        content_snippet = travel_out_content[-1000:]
                        error_msg += f"\n\nTRAVEL.OUT contents:\n{content_snippet}"
                    else:
                        error_msg += "\n\nTRAVEL.OUT exists but is empty"
                except Exception as e:
                    error_msg += f"\n\nCould not read TRAVEL.OUT: {e}"
            else:
                error_msg += "\n\nTRAVEL.OUT not found in workspace"

            if result.stdout:
                error_msg += f"\n\nSTDOUT:\n{result.stdout}"
            if result.stderr:
                error_msg += f"\n\nSTDERR:\n{result.stderr}"

            raise SimulationError(error_msg)

    except subprocess.TimeoutExpired:
        raise SimulationError(f"TRAVEL simulation timed out after {timeout} seconds")

    simulation_time = time.time() - start_time

    # Collect results
    results_path = _collect_results(
        workspace_path,
        results_directory,
        beamline_file,
        beam_file,
    )

    # Create Result object
    return Result(
        results_directory=str(results_path),
        workspace_directory=str(workspace_path),
        beam_file=beam_file,
        beamline_file=beamline_file,
        simulation_time=simulation_time,
        stdout=result.stdout,
        stderr=result.stderr,
    )
