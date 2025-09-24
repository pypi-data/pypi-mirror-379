"""Result class for simulation output handling."""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from .parsers import AvgOut, Deadray, RmsOut, TravelOut


class Result:
    """
    Container for TRAVEL simulation results with analysis methods.

    Provides easy access to AVGOUT, RMSOUT, and other output files
    with user-friendly property access and file management capabilities.
    """

    def __init__(
        self,
        results_directory: str,
        workspace_directory: str = None,
        beam_file: str = None,
        beamline_file: str = None,
        simulation_time: float = None,
        stdout: str = None,
        stderr: str = None,
    ):
        """
        Initialize result from simulation metadata.

        Args:
            results_directory: Directory containing TRAVEL outputs
            workspace_directory: Directory where TRAVEL was executed
            beam_file: Original beam file path
            beamline_file: Original beamline file path
            simulation_time: Execution time in seconds
            stdout: TRAVEL console output
            stderr: TRAVEL error output
        """
        self.results_directory = str(results_directory)
        self.workspace_directory = workspace_directory
        self.beam_file = beam_file
        self.beamline_file = beamline_file
        self.simulation_time = simulation_time or 0.0
        self.stdout = stdout or ""
        self.stderr = stderr or ""

        # File manifest system - discover available output files
        self._files = self._discover_output_files()

        # Lazy loading cache for parsed data
        self._parsed_data = {}

        # Lazy loading cache for parser instances
        self._avgout = None
        self._rmsout = None
        self._deadray = None
        self._travelout = None

    @property
    def avgout(self) -> Optional[AvgOut]:
        """
        Get AvgOut parser for AVGOUT file data.

        Returns:
            AvgOut parser instance if AVGOUT file exists, None otherwise

        Example:
            result = run_travel('beam.dat', 'beamline.in')
            df = result.avgout.dataframe
            z_positions = df['Length [m]']
            x_avg = df['x Average [m]']
        """
        if self._avgout is None:
            avgout_file = self._find_output_file(
                ["AVGOUT.TXT", "avgout.txt"], card_type=33
            )
            if avgout_file:
                self._avgout = AvgOut(avgout_file)
        return self._avgout

    @property
    def rmsout(self) -> Optional[RmsOut]:
        """
        Get RmsOut parser for RMSOUT file data.

        Returns:
            RmsOut parser instance if RMSOUT file exists, None otherwise

        Example:
            result = run_travel('beam.dat', 'beamline.in')
            df = result.rmsout.dataframe
            x_rms = df['x RMS [m]']
            emitt_x = df["(X,BGX') RMS-Emittance [m.rad]"]
        """
        if self._rmsout is None:
            rmsout_file = self._find_output_file(
                ["RMSOUT.TXT", "rmsout.txt"], card_type=34
            )
            if rmsout_file:
                self._rmsout = RmsOut(rmsout_file)
        return self._rmsout

    @property
    def deadray(self) -> Optional[Deadray]:
        """
        Get Deadray parser for DEADRAY file data.

        Returns:
            Deadray parser instance if DEADRAY file exists, None otherwise

        Example:
            result = run_travel('beam.dat', 'beamline.in')
            df = result.deadray.dataframe
            loss_positions = df['z [m]']
            causes = df['Cause of Death']
        """
        if self._deadray is None:
            deadray_file = self._find_output_file(
                ["DEADRAY.XLS", "deadray.xls", "DEADRAYS.TXT", "deadrays.txt"]
            )
            if deadray_file:
                self._deadray = Deadray(deadray_file)
        return self._deadray

    @property
    def travelout(self) -> Optional[TravelOut]:
        """
        Get TravelOut parser for TRAVEL.OUT file data (placeholder).

        Returns:
            TravelOut parser instance if TRAVEL.OUT file exists, None otherwise

        Example:
            result = run_travel('beam.dat', 'beamline.in')
            # Will be implemented later:
            # rf_phases = result.travelout.rf_phases
            # gap_names = result.travelout.gap_names
        """
        if self._travelout is None:
            travel_file = self._find_output_file(["TRAVEL.OUT", "travel.out"])
            if travel_file:
                self._travelout = TravelOut(travel_file)
        return self._travelout

    def _find_output_file(
        self, filenames: List[str], card_type: Optional[int] = None
    ) -> Optional[str]:
        """
        Find output file by checking multiple possible names and card types.

        Args:
            filenames: List of possible filenames to check
            card_type: Optional card type to match

        Returns:
            Full path to the file if found, None otherwise
        """
        results_path = Path(self.results_directory)

        # First, try direct filename matching
        for filename in filenames:
            file_path = results_path / filename
            if file_path.exists():
                return str(file_path)

        # Then, check discovered files by card type
        if card_type is not None:
            for file_id, file_info in self._files.items():
                if file_info["card_type"] == card_type:
                    return str(file_info["path"])

        return None

    def _discover_output_files(self) -> Dict[str, Dict[str, Any]]:
        """
        Discover available output files in results directory with metadata.

        Returns:
            Dictionary mapping file identifiers to file information including
            path, card_type, size, and modification time
        """
        files = {}
        if not self.results_directory or not os.path.exists(self.results_directory):
            return files

        results_path = Path(self.results_directory)

        # Parse beamline file to get filename -> card type mapping
        filename_to_card = {}
        if self.beamline_file and os.path.exists(self.beamline_file):
            from travelpy.simulation.runner import _parse_output_cards

            beamline_outputs = _parse_output_cards(self.beamline_file)

            # Create mapping from filename (case-insensitive) to card type
            for filename in beamline_outputs:
                # Check for cards by position in beamline (simplified approach)
                # A more sophisticated approach would parse beamline again
                filename_lower = filename.lower()
                if "reference" in filename_lower:
                    filename_to_card[filename] = 32
                elif "avg" in filename_lower:
                    filename_to_card[filename] = 33
                elif "rms" in filename_lower:
                    filename_to_card[filename] = 34
                elif "single" in filename_lower or "track" in filename_lower:
                    filename_to_card[filename] = 35
                elif filename.endswith(".xls"):
                    filename_to_card[filename] = 36
                elif filename.endswith(".dat"):
                    filename_to_card[filename] = 37
                elif filename.endswith(".dst"):
                    filename_to_card[filename] = 38
                elif filename.endswith(".txt"):
                    filename_to_card[filename] = 39

        # System files (always present)
        system_patterns = {
            "travel_log": ["TRAVEL.OUT", "travel.out"],
            "deadrays": ["DEADRAY.XLS", "deadray.xls"],
        }

        # Beam dump files (BEAMT.DAT is auto-created by TRAVEL at end of simulation)
        beam_dump_patterns = {
            "beam_copy": ["BEAMT.DAT", "beamt.dat"],
        }

        # Look for system files
        for file_type, patterns in system_patterns.items():
            for pattern in patterns:
                file_path = results_path / pattern
                if file_path.exists():
                    stat_info = file_path.stat()
                    files[file_type] = {
                        "path": file_path,
                        "card_type": "system",
                        "size": stat_info.st_size,
                        "mtime": stat_info.st_mtime,
                    }
                    break

        # Look for beam dump files (BEAMT.DAT auto-created by TRAVEL)
        for file_type, patterns in beam_dump_patterns.items():
            for pattern in patterns:
                file_path = results_path / pattern
                if file_path.exists():
                    stat_info = file_path.stat()
                    files[file_type] = {
                        "path": file_path,
                        "card_type": "beam_dump",
                        "size": stat_info.st_size,
                        "mtime": stat_info.st_mtime,
                    }
                    break

        # Find all output files and categorize them
        if results_path.exists():
            for file_path in results_path.iterdir():
                if file_path.is_file() and file_path.suffix.lower() in {
                    ".txt",
                    ".out",
                    ".dat",
                    ".dst",
                    ".xls",
                }:
                    # Skip if already found as system file
                    if any(
                        file_info["path"] == file_path for file_info in files.values()
                    ):
                        continue

                    stat_info = file_path.stat()
                    filename = file_path.name

                    # Determine card type from beamline parsing or heuristics
                    card_type = "unknown"
                    for beamline_filename, card_num in filename_to_card.items():
                        # Case-insensitive matching since TRAVEL may change case
                        if (
                            beamline_filename.lower() == filename.lower()
                            or beamline_filename.upper() == filename.upper()
                            or beamline_filename == filename
                        ):
                            card_type = card_num
                            break

                    card_type = self._infer_card_type(filename, card_type)

                    # Create unique identifier (preserve legacy "unknown" prefix)
                    if card_type == "unknown":
                        file_id = f"unknown_{file_path.stem.lower()}"
                    else:
                        suffix = (
                            f"card{card_type}" if card_type != "system" else "system"
                        )
                        file_id = f"unknown_{suffix}_{file_path.stem.lower()}"

                    files[file_id] = {
                        "path": file_path,
                        "card_type": card_type,
                        "size": stat_info.st_size,
                        "mtime": stat_info.st_mtime,
                    }

        return files

    def _infer_card_type(self, filename: str, current_type: Any) -> Any:
        """Infer card type from filename when beamline metadata is unavailable."""
        if current_type and current_type != "unknown":
            return current_type

        name_lower = filename.lower()

        system_names = {
            "travel.out",
            "deadray.xls",
        }
        if name_lower in system_names:
            return "system"

        beam_dump_names = {
            "beamt.dat",
        }
        if name_lower in beam_dump_names:
            return "beam_dump"

        if "reference" in name_lower:
            return 32
        if "avg" in name_lower:
            return 33
        if "rms" in name_lower:
            return 34
        if "single" in name_lower or "track" in name_lower:
            return 35

        suffix = Path(filename).suffix.lower()
        if suffix == ".xls" and ("beam" in name_lower or "dump" in name_lower):
            return 36
        if suffix == ".dat" and ("beam" in name_lower or "dump" in name_lower):
            return 37
        if suffix == ".dst" and ("beam" in name_lower or "dump" in name_lower):
            return 38
        if suffix == ".txt" and ("beam" in name_lower or "dump" in name_lower):
            return 39

        return "unknown"

    def _is_input_file(self, file_path) -> bool:
        """
        Check if a file is an input file that should be preserved during cleanup.

        Args:
            file_path: Path object or string path to check

        Returns:
            True if the file is an input beam or beamline file, False otherwise
        """
        if not self.beam_file and not self.beamline_file:
            return False

        file_path_str = str(file_path)
        file_name = Path(file_path_str).name

        # Check if this file matches the input beam file name
        if self.beam_file:
            beam_name = Path(self.beam_file).name
            if file_name.lower() == beam_name.lower():
                return True

        # Check if this file matches the input beamline file name
        if self.beamline_file:
            beamline_name = Path(self.beamline_file).name
            if file_name.lower() == beamline_name.lower():
                return True

        return False

    def _get_travel_generated_files(self) -> set[str]:
        """
        Get complete list of files that TRAVEL generated during simulation.

        Returns:
            Set of filenames (case-insensitive) that TRAVEL created
        """
        travel_files = set()

        # Known system files that TRAVEL always creates
        system_files = {"TRAVEL.OUT", "DEADRAY.XLS"}
        beam_dump_files = {"BEAMT.DAT"}  # Auto-created beam dump

        for filename in system_files:
            travel_files.add(filename.upper())
            travel_files.add(filename.lower())

        for filename in beam_dump_files:
            travel_files.add(filename.upper())
            travel_files.add(filename.lower())

        # Parse beamline file for declared output files (cards 32-39)
        if self.beamline_file and os.path.exists(self.beamline_file):
            from travelpy.simulation.runner import _parse_output_cards

            declared_files = _parse_output_cards(self.beamline_file)
            for filename in declared_files:
                # TRAVEL may change case, so add both versions
                travel_files.add(filename.upper())
                travel_files.add(filename.lower())
                travel_files.add(filename)  # Original case

        return travel_files

    def _is_travel_generated_file(self, file_path) -> bool:
        """
        Check if a file was generated by TRAVEL during simulation.

        Args:
            file_path: Path object or string path to check

        Returns:
            True if the file was generated by TRAVEL, False otherwise
        """
        file_name = Path(file_path).name
        travel_files = self._get_travel_generated_files()
        return file_name in travel_files

    @property
    def files(self) -> List[str]:
        """
        List of TRAVEL-generated output file paths.

        Returns:
            List of all TRAVEL-generated output file paths (excludes input files)
        """
        output_files = []

        for file_id, file_info in self._files.items():
            file_path = str(file_info["path"])

            # Only include TRAVEL-generated output files, exclude input files
            if not self._is_input_file(file_info["path"]):
                output_files.append(file_path)

        return output_files

    def display_output_files(self) -> None:
        """
        Display organized summary of all output files with descriptions.

        Shows files categorized by type (system files, beam evolution, beam dumps)
        with file sizes, creation times, and explanations of what each file contains.
        """

        if not self._files:
            print("No output files found.")
            return

        print("=" * 60)
        print("TRAVEL SIMULATION OUTPUT FILES")
        print("=" * 60)

        # Categorize files (excluding input files - only show TRAVEL outputs)
        system_files = []
        beam_evolution_files = []  # Cards 32-35
        beam_dumps = []  # Cards 36-39
        unknown_files = []

        for file_id, file_info in self._files.items():
            card_type = file_info["card_type"]
            file_path = file_info["path"]

            # Skip input files - display_output_files should only show TRAVEL outputs
            if self._is_input_file(file_path):
                continue
            elif card_type == "system":
                system_files.append((file_id, file_info))
            elif card_type in [32, 33, 34, 35]:
                beam_evolution_files.append((file_id, file_info))
            elif card_type in [36, 37, 38, 39] or card_type == "beam_dump":
                beam_dumps.append((file_id, file_info))
            else:
                unknown_files.append((file_id, file_info))

        # Display system files
        if system_files:
            print("\n[SYSTEM FILES]")
            print("-" * 40)
            for file_id, file_info in system_files:
                self._display_file_info(file_id, file_info)

        # Display beam evolution files (cards 32-35)
        if beam_evolution_files:
            print("\n[BEAM EVOLUTION FILES] (Cards 32-35)")
            print("-" * 40)
            for file_id, file_info in beam_evolution_files:
                self._display_file_info(file_id, file_info)

        # Display beam dumps (cards 36-39)
        if beam_dumps:
            print("\n[BEAM DUMPS] (Cards 36-39)")
            print("-" * 40)
            for file_id, file_info in beam_dumps:
                self._display_file_info(file_id, file_info)

        # Display unknown files
        if unknown_files:
            print("\n[UNKNOWN FILES]")
            print("-" * 40)
            for file_id, file_info in unknown_files:
                self._display_file_info(file_id, file_info)

        print("\n" + "=" * 60)
        # Count only output files (exclude input files)
        output_files_count = (
            len(system_files)
            + len(beam_evolution_files)
            + len(beam_dumps)
            + len(unknown_files)
        )
        print(f"Total files: {output_files_count}")

        # Calculate total size of only the displayed output files
        total_size = 0
        for file_list in [
            system_files,
            beam_evolution_files,
            beam_dumps,
            unknown_files,
        ]:
            for _, file_info in file_list:
                total_size += file_info["size"]

        print(f"Total size: {self._format_file_size(total_size)}")
        print("=" * 60)

    def _display_file_info(self, file_id: str, file_info: Dict[str, Any]) -> None:
        """Display information for a single file."""
        import datetime

        path = file_info["path"]
        filename = path.name
        size = file_info["size"]
        mtime = file_info["mtime"]
        card_type = file_info["card_type"]

        # Format modification time
        mod_time = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")

        # Get description based on card type
        description = self._get_file_description(card_type, filename)

        print(f"  * {filename}")
        print(f"      Size: {self._format_file_size(size)}")
        print(f"      Modified: {mod_time}")
        print(f"      Type: {description}")
        print()

    def _get_file_description(self, card_type: Any, filename: str) -> str:
        """Get description for a file based on its card type."""
        # Check if this is an input file first
        file_path = Path(self.results_directory) / filename
        if self._is_input_file(file_path):
            if Path(filename).suffix.lower() == ".dat":
                return "Input beam file (copied to workspace)"
            else:
                return "Input beamline file (copied to workspace)"

        if card_type == "system":
            if "TRAVEL.OUT" in filename.upper():
                return "Simulation log with RF phases and execution details"
            elif "DEADRAY.XLS" in filename.upper():
                return "Particle loss information"
            else:
                return "System file"
        elif card_type == "beam_dump":
            if "BEAMT.DAT" in filename.upper():
                return "Final beam distribution (auto-created by TRAVEL)"
            else:
                return "Beam dump file"
        elif card_type == 32:
            return "Card 32: Reference particle evolution along beamline"
        elif card_type == 33:
            return "Card 33: Average beam properties along beamline"
        elif card_type == 34:
            return "Card 34: RMS beam properties along beamline"
        elif card_type == 35:
            return "Card 35: Single particle trajectory tracking"
        elif card_type == 36:
            return "Card 36: Beam dump in Excel format"
        elif card_type == 37:
            return "Card 37: Beam dump in TRAVEL .dat format"
        elif card_type == 38:
            return "Card 38: Beam dump in PARMILAS .dst format"
        elif card_type == 39:
            return "Card 39: Beam dump in text format"
        else:
            return "Unknown file type"

    def _format_file_size(self, size_bytes: int) -> str:
        """Format file size showing raw bytes alongside human-readable units."""
        if size_bytes < 0:
            size_bytes = 0

        raw = f"{size_bytes:,} B"
        if size_bytes == 0:
            return raw

        size_float = float(size_bytes)
        units = [("KB", 1024.0), ("MB", 1024.0**2), ("GB", 1024.0**3)]
        for unit, factor in units:
            if size_float < factor * 1024 or unit == "GB":
                human = size_float / factor
                return f"{raw} ({human:.1f} {unit})"

        return raw

    def clean_outputs(
        self,
        *,
        keep_travelout_file: bool = False,
        keep_deadray_file: bool = False,
        keep_beam_dumps: bool = False,
        keep_evolution_files: bool = False,
        keep_files: list[str] = None,
        dry_run: bool = False,
        verbose: bool = False,
    ) -> dict[str, list[str]] | None:
        """
        Clean up TRAVEL output files from results directory.

        Deletes output files based on their categories, with options to preserve
        specific file types. Input files (beam and beamline files) are always
        preserved to prevent accidental deletion of original data.

        Args:
            keep_travelout_file: Preserve TRAVEL.OUT simulation log file
            keep_deadray_file: Preserve DEADRAY.XLS particle loss information file
            keep_beam_dumps: Preserve beam dump files (cards 36-39 + BEAMT.DAT: .xls, .dat, .dst, .txt dumps)
            keep_evolution_files: Preserve beam evolution files (cards 32-35: reference, avg, rms, single)
            keep_files: List of specific filenames to preserve (just filename, not full path)
            dry_run: Preview deletions without actually deleting files (always returns summary)
            verbose: Return detailed summary of operations (default: False for clean usage)

        Returns:
            Dictionary with deletion summary if dry_run=True or verbose=True, None otherwise:
            - "deleted": List of successfully deleted file paths
            - "kept": List of preserved file paths (including input files)
            - "errors": List of files that couldn't be deleted
            - "would_delete": List of files that would be deleted (dry_run mode only)
            - "would_keep": List of files that would be kept (dry_run mode only)

        Note:
            Input beam and beamline files are automatically preserved regardless
            of the keep_* parameters to prevent accidental data loss.

        Examples:
            Clean all output files (silent by default):
            >>> result = run_travel("beam.dat", "beamline.in")  # doctest: +SKIP
            >>> result.clean_outputs()  # doctest: +SKIP

            Clean with detailed feedback:
            >>> summary = result.clean_outputs(verbose=True)  # doctest: +SKIP
            >>> print(f"Deleted {len(summary['deleted'])} files")  # doctest: +SKIP

            Keep beam evolution data:
            >>> result.clean_outputs(keep_evolution_files=True)  # doctest: +SKIP

            Keep specific files by name:
            >>> result.clean_outputs(keep_files=['Output_beam.dat', 'Special_dump.txt'])  # doctest: +SKIP

            Preview cleanup without deleting:
            >>> summary = result.clean_outputs(dry_run=True)  # doctest: +SKIP
            >>> print(f"Would delete: {summary['would_delete']}")  # doctest: +SKIP

            Selective preservation:
            >>> result.clean_outputs(  # doctest: +SKIP
            ...     keep_travelout_file=True,
            ...     keep_beam_dumps=True
            ... )
        """
        deleted = []
        kept = []
        errors = []
        would_delete = []
        would_keep = []

        # Convert keep_files to a set of normalized filenames for fast lookup
        keep_files_set = set()
        if keep_files:
            for filename in keep_files:
                # Add both original case and common case variants
                keep_files_set.add(filename.lower())
                keep_files_set.add(filename.upper())
                keep_files_set.add(filename)

        for file_id, file_info in self._files.items():
            file_path = file_info["path"]
            card_type = file_info["card_type"]

            # Skip input files completely - they are preserved automatically but not reported
            if self._is_input_file(file_path):
                continue  # Don't include input files in any summary

            # Determine if file should be kept based on its category
            should_keep = False
            filename = Path(file_path).name

            # Check if file is in the keep_files list (highest priority)
            if keep_files_set and filename.lower() in keep_files_set:
                should_keep = True
            # Only delete files that TRAVEL generated - preserve all user files
            elif not self._is_travel_generated_file(file_path):
                should_keep = True  # Preserve any file not generated by TRAVEL
            elif (
                keep_travelout_file
                and card_type == "system"
                and "TRAVEL.OUT" in filename.upper()
            ):
                should_keep = True
            elif (
                keep_deadray_file
                and card_type == "system"
                and "DEADRAY.XLS" in filename.upper()
            ):
                should_keep = True
            elif keep_beam_dumps and (
                card_type in [36, 37, 38, 39] or card_type == "beam_dump"
            ):
                should_keep = True
            elif keep_evolution_files and card_type in [32, 33, 34, 35]:
                should_keep = True

            if dry_run:
                # Dry run mode - don't actually delete, just report what would happen
                if should_keep:
                    would_keep.append(str(file_path))
                else:
                    would_delete.append(str(file_path))
            else:
                # Actual deletion mode
                if should_keep:
                    kept.append(str(file_path))
                else:
                    # Attempt to delete the file
                    try:
                        if file_path.exists():
                            file_path.unlink()
                            deleted.append(str(file_path))
                        else:
                            # File already missing - report as error
                            errors.append(str(file_path))
                    except OSError as e:
                        # Permission error, file in use, etc.
                        errors.append(f"{file_path}: {e}")

        # Invalidate cached parser instances and update file registry since files may be deleted
        if not dry_run:
            self._avgout = None
            self._rmsout = None
            self._deadray = None
            self._travelout = None

            # Remove deleted files from the _files registry
            files_to_remove = []
            for file_id, file_info in self._files.items():
                file_path = str(file_info["path"])
                if file_path in deleted:
                    files_to_remove.append(file_id)

            for file_id in files_to_remove:
                del self._files[file_id]

        # Return appropriate summary based on mode and verbosity
        # Only report on output files - input files are preserved automatically
        if dry_run:
            # Always return info for dry_run - that's the point of dry_run
            return {
                "would_delete": would_delete,
                "would_keep": would_keep,
            }
        elif verbose:
            return {
                "deleted": deleted,
                "kept": kept,
                "errors": errors,
            }
        else:
            return None
