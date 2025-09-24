"""
Beam format conversion utilities for TRAVEL particle tracking.

This module provides functions to convert between different beam file formats:
- .dat (TRAVEL binary format)
- .dst (PARMILA format)
- .txt (text format)

All functions use the TRAVEL beam conversion executables and support flexible
input/output paths including absolute paths.
"""

import os
import subprocess
from typing import Optional

from travelpy.config.paths import get_travel_directory
from travelpy.exceptions import TravelpyError


def _get_converter_path(executable_name: str) -> str:
    """Get the full path to a beam conversion executable."""
    travel_dir = get_travel_directory()
    if not travel_dir:
        raise TravelpyError(
            "TRAVEL directory not configured. Use travelpy.set_travel_directory()"
        )

    converter_path = os.path.join(
        travel_dir, "Tools", "BeamConversion", executable_name
    )

    if not os.path.exists(converter_path):
        raise TravelpyError(f"Beam conversion executable not found: {converter_path}")

    return converter_path


def _run_converter(
    executable_name: str,
    input_path: str,
    output_path: str,
    interactive_input: Optional[str] = None,
    extra_arg: Optional[str] = None,
) -> None:
    """Run a beam conversion executable with optional input or extra argument."""
    converter_path = _get_converter_path(executable_name)

    # Convert paths to absolute paths
    input_path = os.path.abspath(input_path)
    output_path = os.path.abspath(output_path)

    # Check input file exists
    if not os.path.exists(input_path):
        raise TravelpyError(f"Input file not found: {input_path}")

    try:
        # Build command arguments
        cmd_args = [converter_path, input_path, output_path]
        if extra_arg is not None:
            cmd_args.append(extra_arg)

        if interactive_input is not None:
            # Handle interactive input (e.g., beam current for dat2dst)
            process = subprocess.Popen(
                cmd_args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = process.communicate(input=f"{interactive_input}\n")
        else:
            # Direct conversion
            result = subprocess.run(
                cmd_args, capture_output=True, text=True, check=True
            )
            stderr = result.stderr

        # Check if conversion was successful
        if not os.path.exists(output_path):
            error_msg = f"Conversion failed. Output file not created: {output_path}"
            if stderr:
                error_msg += f"\nError: {stderr}"
            raise TravelpyError(error_msg)

    except subprocess.CalledProcessError as e:
        error_msg = f"Beam conversion failed: {executable_name} returned error code {e.returncode}"
        if e.stderr:
            error_msg += f"\nError details: {e.stderr}"
        raise TravelpyError(error_msg)
    except Exception as e:
        raise TravelpyError(f"Unexpected error during beam conversion: {e}")


def dat2txt(input_path: str, output_path: str) -> None:
    """
    Convert TRAVEL .dat file to text format.

    Args:
        input_path: Path to input .dat file
        output_path: Path for output .txt file

    Raises:
        TravelpyError: If conversion fails, files not found, or executable not found
    """
    _run_converter("Dat2Txt.exe", input_path, output_path)


def dat2dst(input_path: str, output_path: str, beam_current_ma: float = 1.0) -> None:
    """
    Convert TRAVEL .dat file to PARMILA .dst format.

    This conversion requires interactive input for beam current in mA.

    Args:
        input_path: Path to input .dat file
        output_path: Path for output .dst file
        beam_current_ma: Beam current in milliamps (default: 1.0)

    Raises:
        TravelpyError: If conversion fails or files not found
        ExecutableNotFoundError: If dat2dst.exe not found
    """
    _run_converter("Dat2Dst.exe", input_path, output_path, str(beam_current_ma))


def dst2dat(input_path: str, output_path: str, particle_type: str = "p") -> None:
    """
    Convert PARMILA .dst file to TRAVEL .dat format.

    Since .dst files don't specify particle type, it must be provided.

    Args:
        input_path: Path to input .dst file
        output_path: Path for output .dat file
        particle_type: Particle type, "p" for proton, "e" for electron (default: "p")

    Raises:
        TravelpyError: If conversion fails or files not found
        ExecutableNotFoundError: If dst2dat.exe not found

    Note:
        ATTENTION! dst2dat.exe converter may round the proton mass to 938.3 MeV.
        Default particle type is proton.
    """
    _run_converter("Dst2Dat.exe", input_path, output_path, extra_arg=particle_type)


def dst2txt(input_path: str, output_path: str, particle_type: str = "p") -> None:
    """
    Convert PARMILA .dst file to text format.

    Since .dst files don't specify particle type, it must be provided.

    Args:
        input_path: Path to input .dst file
        output_path: Path for output .txt file
        particle_type: Particle type, "p" for proton, "e" for electron (default: "p")

    Raises:
        TravelpyError: If conversion fails or files not found
        ExecutableNotFoundError: If dst2txt.exe not found

    Note:
        ATTENTION! dst2txt.exe converter may round the proton mass to 938.3 MeV.
        Default particle type is proton.
    """
    _run_converter("Dst2Txt.exe", input_path, output_path, extra_arg=particle_type)


def txt2dat(input_path: str, output_path: str) -> None:
    """
    Convert text file to TRAVEL .dat format.

    Args:
        input_path: Path to input .txt file
        output_path: Path for output .dat file

    Raises:
        TravelpyError: If conversion fails or files not found
        ExecutableNotFoundError: If txt2dat.exe not found
    """
    _run_converter("Txt2Dat.exe", input_path, output_path)
