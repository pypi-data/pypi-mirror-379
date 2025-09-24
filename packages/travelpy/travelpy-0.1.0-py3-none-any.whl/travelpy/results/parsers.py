"""
Output file parsers for TRAVEL simulation results.

Provides standalone parser classes for AVGOUT, RMSOUT, and DEADRAY files
with dataframe property for easy data access.
"""

from pathlib import Path
from typing import Optional

import pandas as pd

from ._generated_properties import AvgOutGenerated, RmsOutGenerated


class BaseOutputParser:
    """
    Base class for TRAVEL output file parsers.

    Provides common functionality for parsing tab-separated TRAVEL output files
    with lazy loading and caching of DataFrames.
    """

    def __init__(self, file_path: str):
        """
        Initialize parser with file path.

        Args:
            file_path: Path to the TRAVEL output file
        """
        self.file_path = Path(file_path)
        self._dataframe: Optional[pd.DataFrame] = None

    @property
    def dataframe(self) -> pd.DataFrame:
        """
        Get parsed data as pandas DataFrame with lazy loading.

        Returns:
            DataFrame containing the parsed output file data

        Raises:
            FileNotFoundError: If the output file doesn't exist
        """
        if self._dataframe is None:
            # Handle empty or invalid file paths
            if not str(self.file_path) or str(self.file_path) == ".":
                raise FileNotFoundError(f"Output file not found: {self.file_path}")
            if self.file_path.is_dir():
                raise IsADirectoryError(
                    f"Expected file path but got directory: {self.file_path}"
                )
            if not self.file_path.exists():
                raise FileNotFoundError(f"Output file not found: {self.file_path}")
            self._dataframe = self._load_dataframe()
        return self._dataframe

    def _load_dataframe(self) -> pd.DataFrame:
        """
        Load and parse the output file into a DataFrame.

        All TRAVEL output files use tab-separated format.

        Returns:
            Parsed DataFrame with original column names
        """
        return pd.read_csv(self.file_path, sep="\t")


class AvgOut(AvgOutGenerated, BaseOutputParser):
    """
    Parser for AVGOUT files (Card 33 output).

    AVGOUT files contain average beam properties along the beamline including:
    - Average positions and angles (x, x', y, y')
    - Average phase and energy
    - Transmission percentage
    - RF phase information

    Example usage:
        avgout = AvgOut('AVGOUT.TXT')

        # New property-based access (with autocomplete!)
        z_positions = avgout.z
        x_average = avgout.x_avg
        transmission = avgout.transmission

        # Original dataframe access still works
        df = avgout.dataframe
        z_positions = df['Length [m]']
        x_avg = df['x Average [m]']
    """

    pass  # All properties inherited from AvgOutGenerated


class RmsOut(RmsOutGenerated, BaseOutputParser):
    """
    Parser for RMSOUT files (Card 34 output).

    RMSOUT files contain RMS beam properties and beam optics parameters including:
    - RMS beam sizes (x, y)
    - Emittances (100%, 90%, RMS)
    - Twiss parameters (alpha, beta)
    - Halo parameters
    - Phase space correlations

    Example usage:
        rmsout = RmsOut('RMSOUT.TXT')

        # New property-based access (with autocomplete!)
        z_positions = rmsout.z
        x_rms_size = rmsout.x_rms
        x_emittance = rmsout.emit_rms_x_xp
        beta_x_twiss = rmsout.beta_x

        # Original dataframe access still works
        df = rmsout.dataframe
        z_positions = df['Length [m]']
        x_rms = df['x RMS [m]']
        emitt_x = df["(X,BGX') RMS-Emittance [m.rad]"]
    """

    pass  # All properties inherited from RmsOutGenerated


class Deadray(BaseOutputParser):
    """
    Parser for DEADRAY files (particle loss information).

    DEADRAY files contain information about lost particles including:
    - Particle number and position where lost
    - Particle coordinates (x, x', y, y', phase, energy)
    - Cause of death (aperture, momentum, etc.)
    - Card number where loss occurred

    Note: DEADRAY files often have .XLS extension but are tab-separated text files.

    Example usage:
        deadray = Deadray('DEADRAYS.XLS')
        df = deadray.dataframe
        loss_positions = df['z [m]']
        causes = df['Cause of Death']
    """

    pass  # Uses base class _load_dataframe() method


class RFGaps:
    """
    Container for RF gap data extracted from TRAVEL.OUT files.

    Provides property-based access to RF gap information including
    card numbers, gap names, and RF phases.
    """

    def __init__(self, card_numbers: list, gap_names: list, rf_phases: list):
        """
        Initialize RFGaps with parsed data.

        Args:
            card_numbers: List of TRAVEL card numbers
            gap_names: List of gap names (e.g., 'CCL_T1_G1')
            rf_phases: List of RF phases in degrees
        """
        import pandas as pd

        self._dataframe = pd.DataFrame(
            {
                "Card Number": card_numbers,
                "Gap Name": gap_names,
                "RF Phase [deg]": rf_phases,
            }
        )

    @property
    def dataframe(self) -> pd.DataFrame:
        """
        Get RF gap data as pandas DataFrame.

        Returns:
            DataFrame with columns: 'Card Number', 'Gap Name', 'RF Phase [deg]'
        """
        return self._dataframe.copy()

    @property
    def card_number(self) -> pd.Series:
        """TRAVEL card numbers for each RF gap."""
        return self._dataframe["Card Number"]

    @property
    def gap_name(self) -> pd.Series:
        """Gap names (e.g., 'CCL_T1_G1', 'CCL_T1_G2')."""
        return self._dataframe["Gap Name"]

    @property
    def rf_phase(self) -> pd.Series:
        """RF phases in degrees (raw values from TRAVEL.OUT)."""
        return self._dataframe["RF Phase [deg]"]


class TravelOut:
    """
    Parser for TRAVEL.OUT files (simulation log files).

    TRAVEL.OUT files contain simulation logs with RF phase information,
    execution details, and particle statistics. This parser extracts
    RF gap data from the unstructured log text.

    Example usage:
        travel_out = TravelOut('TRAVEL.OUT')
        gaps = travel_out.gaps

        # Access RF gap data
        gaps.dataframe          # Full DataFrame
        gaps.card_number        # Card numbers
        gaps.gap_name          # Gap names
        gaps.rf_phase          # RF phases
    """

    def __init__(self, file_path: str):
        """
        Initialize TravelOut parser with file path.

        Args:
            file_path: Path to the TRAVEL.OUT file
        """
        self.file_path = Path(file_path)
        self._gaps = None
        self._parsed = False

    def _parse_file(self):
        """Parse the TRAVEL.OUT file to extract RF gap information."""
        if self._parsed:
            return

        if not self.file_path.exists():
            raise FileNotFoundError(f"TRAVEL.OUT file not found: {self.file_path}")

        card_numbers = []
        gap_names = []
        rf_phases = []

        with open(self.file_path, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            # Look for RF PHASE IS lines
            if "RF PHASE IS" in line:
                # Extract phase value
                parts = line.split()
                if len(parts) >= 4:
                    phase_str = parts[3].replace("D", "E")  # Handle FORTRAN D notation
                    try:
                        phase = float(phase_str)

                        # Look for corresponding card info in previous lines
                        card_number = None
                        gap_name = None

                        for j in range(
                            i - 1, max(i - 10, 0), -1
                        ):  # Look back up to 10 lines
                            if "GO THROUGH TYPE 22" in lines[j] and "(" in lines[j]:
                                # Extract card number and gap name from pattern like:
                                # "> CARD    8 GO THROUGH TYPE 22 (CCL_T1_G1)"
                                if "CARD" in lines[j]:
                                    card_parts = lines[j].split()
                                    try:
                                        card_idx = card_parts.index("CARD")
                                        if card_idx + 1 < len(card_parts):
                                            card_number = int(card_parts[card_idx + 1])
                                    except (ValueError, IndexError):
                                        pass

                                # Extract gap name from parentheses
                                start = lines[j].find("(")
                                end = lines[j].find(")")
                                if start != -1 and end != -1:
                                    gap_name = lines[j][start + 1 : end]
                                    break

                        if card_number is not None and gap_name:
                            card_numbers.append(card_number)
                            gap_names.append(gap_name)
                            rf_phases.append(phase)

                    except ValueError:
                        continue  # Skip invalid phase values

        self._gaps = RFGaps(card_numbers, gap_names, rf_phases)
        self._parsed = True

    @property
    def gaps(self) -> RFGaps:
        """
        Get RF gap data container.

        Returns:
            RFGaps object with card_number, gap_name, rf_phase properties
        """
        self._parse_file()
        return self._gaps
