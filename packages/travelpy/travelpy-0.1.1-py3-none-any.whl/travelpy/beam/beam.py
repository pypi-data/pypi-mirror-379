"""Beam class for particle ensemble handling."""

import os
from pathlib import Path

import numpy as np

from travelpy.beam.conversion import dat2txt
from travelpy.exceptions import BeamFileError
from travelpy.utils.constants import SPEED_OF_LIGHT
from travelpy.utils.physics import twiss_of_ensemble


def _exit_if_file_not_found(file_path):
    """Check if file exists, raise error if not found."""
    if not Path(file_path).exists():
        raise BeamFileError(f"Beam file not found: {file_path}")


class Beam:
    """
    Represents a particle beam with 6D phase space coordinates.

    Reading a beam file and creating an object with consistent naming
    conventions aligned with AVGOUT/RMSOUT property names.

    Attributes:
        Reference Parameters:
            p_ref (float): Reference momentum [MeV/c]
            phi_ref (float): Reference phase [rad]
            freq (float): Frequency [Hz]
            m0_ref (float): Reference rest mass [MeV/c²]
            q_ref (float): Reference charge
            ekin_ref (float): Reference kinetic energy [MeV]
            n_particles (int): Number of particles in beam

        Relativistic Parameters:
            rel_gamma_ref (float): Reference relativistic gamma factor
            rel_beta_ref (float): Reference relativistic beta factor
            rel_beta_gamma_ref (float): Reference beta*gamma
            ref_beta_lambda (float): Reference beta*lambda [m]
            z_ref (float): Reference z position [m]

        Particle Coordinates (arrays):
            x (ndarray): Horizontal position [m]
            xp (ndarray): Horizontal divergence [rad]
            y (ndarray): Vertical position [m]
            yp (ndarray): Vertical divergence [rad]
            phi (ndarray): RF phase [rad]
            z (ndarray): Longitudinal position [m]
            delta (ndarray): Momentum deviation
            p (ndarray): Particle momentum [MeV/c]
            q (ndarray): Particle charge
            m0 (ndarray): Particle rest mass [MeV/c²]
            ekin (ndarray): Particle kinetic energy [MeV]

        Average Properties:
            x_avg (float): Average horizontal position [m]
            xp_avg (float): Average horizontal divergence [rad]
            y_avg (float): Average vertical position [m]
            yp_avg (float): Average vertical divergence [rad]
            ekin_avg (float): Average kinetic energy [MeV]
            phi_avg (float): Average RF phase [rad]
            p_avg (float): Average momentum [MeV/c]
            z_avg (float): Average longitudinal position [m]

        RMS Properties:
            x_rms (float): Horizontal position RMS [m]
            xp_rms (float): Horizontal divergence RMS [rad]
            y_rms (float): Vertical position RMS [m]
            yp_rms (float): Vertical divergence RMS [rad]
            ekin_rms (float): Kinetic energy RMS [MeV]
            phi_rms (float): RF phase RMS [rad]
            p_rms (float): Momentum RMS [MeV/c]

        Twiss Parameters and Emittances:
            alpha_x_xp (float): Horizontal Twiss alpha parameter
            beta_x_xp (float): Horizontal Twiss beta parameter [m/rad]
            gamma_x_xp (float): Horizontal Twiss gamma parameter [rad/m]
            emitt_unnorm_rms_x_xp (float): Horizontal unnormalized RMS emittance [m·rad]
            emitt_norm_rms_x_xp (float): Horizontal normalized RMS emittance [m·rad]
            alpha_y_yp (float): Vertical Twiss alpha parameter
            beta_y_yp (float): Vertical Twiss beta parameter [m/rad]
            gamma_y_yp (float): Vertical Twiss gamma parameter [rad/m]
            emitt_unnorm_rms_y_yp (float): Vertical unnormalized RMS emittance [m·rad]
            emitt_norm_rms_y_yp (float): Vertical normalized RMS emittance [m·rad]
    """

    def __init__(self, beam_file: str, keep_txt: bool = False):
        """
        Load beam from TRAVEL beam file (.txt or .dat format).

        If a .dat file is provided, it will be automatically converted to .txt format
        using dat2txt conversion. By default, the generated .txt file is deleted after
        reading unless keep_txt=True is specified.

        Args:
            beam_file: Path to beam file (.txt or .dat format)
            keep_txt: If True, keep the .txt file after conversion from .dat (default: False)
        """
        file_path = Path(beam_file)
        _exit_if_file_not_found(file_path)

        # Handle automatic .dat to .txt conversion
        txt_file_path = file_path
        converted_file = None

        if file_path.suffix.lower() == ".dat":
            # Create .txt filename in same directory as .dat file
            txt_file_path = file_path.with_suffix(".txt")
            converted_file = txt_file_path

            # Convert .dat to .txt
            dat2txt(str(file_path), str(txt_file_path))

        elif file_path.suffix.lower() not in [".txt", ".dat"]:
            raise BeamFileError(
                f"Unsupported beam file format '{file_path.suffix}': only .txt and .dat formats are supported"
            )

        # Read the .txt file (either original or converted)
        self._load_from_txt(txt_file_path)

        # Clean up converted file if requested
        if converted_file and not keep_txt:
            try:
                os.remove(converted_file)
            except OSError:
                # File removal failed, but continue - this is not critical
                pass

    def _load_from_txt(self, file_path: Path):
        """Load beam data from .txt format file."""
        line_count = 0
        for line in open(file_path):
            bits = line.split()
            if line_count == 2:
                p_ref = float(bits[0].replace("D", "E")) * 1e3  # in MeV/c
            elif line_count == 3:
                phi_ref = float(bits[0].replace("D", "E"))
            elif line_count == 4:
                freq = float(bits[0].replace("D", "E"))
            elif line_count == 5:
                m0_ref = float(bits[0].replace("D", "E")) * 1e3  # in MeV/c^2
            elif line_count == 6:
                q_ref = float(bits[0])
            elif line_count == 7:
                break
            line_count += 1

        B = np.loadtxt(file_path, skiprows=8)  # ignoring 8 lines

        # Reference parameters
        self.p_ref = p_ref  # reference momentum in MeV/c
        self.phi_ref = phi_ref  # reference phase in rad
        self.freq = freq  # frequency in Hz
        self.m0_ref = m0_ref  # reference rest mass in MeV/c^2
        self.q_ref = q_ref  # reference charge
        self.ekin_ref = float(np.sqrt(self.p_ref**2 + self.m0_ref**2) - self.m0_ref)
        self.n_particles = len(B)

        # Relativistic parameters
        self.rel_gamma_ref = self.ekin_ref / self.m0_ref + 1
        self.rel_beta_ref = float(np.sqrt(1 - 1 / self.rel_gamma_ref**2))
        self.rel_beta_gamma_ref = self.p_ref / self.m0_ref
        self.ref_beta_lambda = self.rel_beta_ref * SPEED_OF_LIGHT / self.freq
        self.z_ref = float(-self.ref_beta_lambda / np.pi * 0.5 * self.phi_ref)

        # Particle coordinates
        self.x = B[:, 1]  # x in m
        self.xp = B[:, 2]  # xp in rad
        self.y = B[:, 3]  # y in m
        self.yp = B[:, 4]  # yp in rad
        self.phi = B[:, 5]  # phase in rad
        self.z = -self.ref_beta_lambda / np.pi * 0.5 * self.phi
        self.delta = B[:, 6]
        self.p = self.p_ref * (self.delta + 1)  # momentum of each particle in MeV/c
        self.q = B[:, 8]  # charge of each particle
        self.m0 = B[:, 9] * 1e3  # rest mass of each particle in MeV/c^2
        self.ekin = (
            np.sqrt(self.p**2 + self.m0**2) - self.m0
        )  # kinetic energy of each particle in MeV

        # Average properties of the beam
        self.x_avg = np.mean(self.x)  # average x in m
        self.xp_avg = np.mean(self.xp)  # average xp in rad
        self.y_avg = np.mean(self.y)  # average y in m
        self.yp_avg = np.mean(self.yp)  # average yp in rad
        self.ekin_avg = np.mean(self.ekin)  # average kinetic energy in MeV
        self.phi_avg = np.mean(self.phi)  # average phase in rad
        self.p_avg = np.mean(self.p)  # average momentum in MeV/c
        self.z_avg = np.mean(self.z)  # average z in m

        # RMS properties of the beam
        self.x_rms = np.std(self.x)  # x_rms in m
        self.xp_rms = np.std(self.xp)  # xp_rms in rad
        self.y_rms = np.std(self.y)  # y_rms in m
        self.yp_rms = np.std(self.yp)  # yp_rms in rad
        self.ekin_rms = np.std(self.ekin)  # kinetic energy RMS in MeV
        self.phi_rms = np.std(self.phi)  # phase RMS in rad
        self.p_rms = np.std(self.p)  # momentum RMS in MeV/c

        # Twiss parameters and emittances
        # X-X' plane
        [
            self.alpha_x_xp,
            self.beta_x_xp,
            self.emitt_unnorm_rms_x_xp,
        ] = twiss_of_ensemble(self.x, self.xp)
        self.gamma_x_xp = (1 + self.alpha_x_xp**2) / self.beta_x_xp
        self.emitt_norm_rms_x_xp = self.emitt_unnorm_rms_x_xp * self.rel_beta_gamma_ref

        # Y-Y' plane
        [
            self.alpha_y_yp,
            self.beta_y_yp,
            self.emitt_unnorm_rms_y_yp,
        ] = twiss_of_ensemble(self.y, self.yp)
        self.gamma_y_yp = (1 + self.alpha_y_yp**2) / self.beta_y_yp
        self.emitt_norm_rms_y_yp = self.emitt_unnorm_rms_y_yp * self.rel_beta_gamma_ref
