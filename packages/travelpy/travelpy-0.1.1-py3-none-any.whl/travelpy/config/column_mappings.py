"""
Column mappings for TRAVEL output files to travelpy property names.

This file defines the mapping between verbose TRAVEL column names and
user-friendly property names for easy data access. Users can modify
property names here and regenerate properties using the code generation script.

Generated from: travelpy_column_property_mapping.md
"""

# AVGOUT File (Card 33) - Average Beam Properties
AVGOUT_MAPPINGS = {
    "Card Number": {
        "property": "card_number",
        "units": "-",
        "description": "Card sequence number",
    },
    "Card Type": {
        "property": "card_type",
        "units": "-",
        "description": "TRAVEL card type",
    },
    "Length [m]": {
        "property": "z",
        "units": "m",
        "description": "Longitudinal position along beamline",
    },
    "Alive [%]": {
        "property": "transmission",
        "units": "%",
        "description": "Beam transmission percentage",
    },
    "x Average [m]": {
        "property": "x_avg",
        "units": "m",
        "description": "Average x position",
    },
    "x' Average [rad]": {
        "property": "xp_avg",
        "units": "rad",
        "description": "Average x divergence",
    },
    "y Average [m]": {
        "property": "y_avg",
        "units": "m",
        "description": "Average y position",
    },
    "y' Average [rad]": {
        "property": "yp_avg",
        "units": "rad",
        "description": "Average y divergence",
    },
    "Phase Average [rad]": {
        "property": "phi_avg",
        "units": "rad",
        "description": "Average RF phase",
    },
    "Momentum Average [GeV/c]": {
        "property": "p_avg",
        "units": "GeV/c",
        "description": "Average momentum",
    },
    "Kinetic Energy Average [GeV]": {
        "property": "ekin_avg",
        "units": "GeV",
        "description": "Average kinetic energy",
    },
    "Rest Energy Average [GeV]": {
        "property": "rest_energy_avg",
        "units": "GeV",
        "description": "Average rest energy",
    },
    "RF Phase [deg]": {
        "property": "rf_phase",
        "units": "deg",
        "description": "RF phase at gaps",
    },
    "Power loss [watt]": {
        "property": "power_loss",
        "units": "W",
        "description": "Power loss",
    },
}

# RMSOUT File (Card 34) - RMS Beam Properties
RMSOUT_MAPPINGS = {
    # Basic Properties
    "Card Number": {
        "property": "card_number",
        "units": "-",
        "description": "Card sequence number",
    },
    "Card Type": {
        "property": "card_type",
        "units": "-",
        "description": "TRAVEL card type",
    },
    "Length [m]": {
        "property": "z",
        "units": "m",
        "description": "Longitudinal position along beamline",
    },
    "Aperture x [m]": {
        "property": "aperture_x",
        "units": "m",
        "description": "X aperture",
    },
    "Aperture y [m]": {
        "property": "aperture_y",
        "units": "m",
        "description": "Y aperture",
    },
    # RMS Beam Sizes
    "x RMS [m]": {"property": "x_rms", "units": "m", "description": "RMS x beam size"},
    "x' RMS [rad]": {
        "property": "xp_rms",
        "units": "rad",
        "description": "RMS x divergence",
    },
    "y RMS [m]": {"property": "y_rms", "units": "m", "description": "RMS y beam size"},
    "y' RMS [rad]": {
        "property": "yp_rms",
        "units": "rad",
        "description": "RMS y divergence",
    },
    "Phase RMS [rad]": {
        "property": "phi_rms",
        "units": "rad",
        "description": "RMS phase spread",
    },
    # Energy Properties
    "Momentum RMS [GeV/c]": {
        "property": "p_rms",
        "units": "GeV/c",
        "description": "RMS momentum",
    },
    "Kinetic Energy RMS [GeV]": {
        "property": "ekin_rms",
        "units": "GeV",
        "description": "RMS kinetic energy",
    },
    "Rest Energy RMS [GeV]": {
        "property": "rest_energy_rms",
        "units": "GeV",
        "description": "RMS rest energy",
    },
    "Momentum Standard Deviation [GeV/c]": {
        "property": "p_std",
        "units": "GeV/c",
        "description": "Momentum standard deviation",
    },
    "Kinetic Energy Standard Deviation [GeV]": {
        "property": "ekin_std",
        "units": "GeV",
        "description": "Kinetic energy standard deviation",
    },
    # Emittances - Transverse
    "(X,BGX') 100%-Emittance [m.rad]": {
        "property": "emitt_norm_100_x_xp",
        "units": "m·rad",
        "description": "X emittance (100%)",
    },
    "(X,BGX') 90%-Emittance [m.rad]": {
        "property": "emitt_norm_90_x_xp",
        "units": "m·rad",
        "description": "X emittance (90%)",
    },
    "(X,BGX') RMS-Emittance [m.rad]": {
        "property": "emitt_norm_rms_x_xp",
        "units": "m·rad",
        "description": "X RMS emittance",
    },
    "(Y,BGY') 100%-Emittance [m.rad]": {
        "property": "emitt_norm_100_y_yp",
        "units": "m·rad",
        "description": "Y emittance (100%)",
    },
    "(Y,BGY') 90%-Emittance [m.rad]": {
        "property": "emitt_norm_90_y_yp",
        "units": "m·rad",
        "description": "Y emittance (90%)",
    },
    "(Y,BGY') RMS-Emittance [m.rad]": {
        "property": "emitt_norm_rms_y_yp",
        "units": "m·rad",
        "description": "Y RMS emittance",
    },
    # Emittances - Longitudinal
    "(PHI,dE) 100%-Emittance [deg.MeV]": {
        "property": "emitt_100_phi_ekin",
        "units": "deg·MeV",
        "description": "Longitudinal emittance (100%)",
    },
    "(PHI,dE) 90%-Emittance [deg.MeV]": {
        "property": "emitt_90_phi_ekin",
        "units": "deg·MeV",
        "description": "Longitudinal emittance (90%)",
    },
    "(PHI,dE) RMS-Emittance [deg.MeV]": {
        "property": "emitt_rms_phi_ekin",
        "units": "deg·MeV",
        "description": "Longitudinal RMS emittance",
    },
    "(PHI,dP) 100%-Emittance [deg.MeV/c]": {
        "property": "emitt_100_phi_p",
        "units": "deg·MeV/c",
        "description": "Momentum-phase emittance (100%)",
    },
    "(PHI,dP) 90%-Emittance [deg.MeV/c]": {
        "property": "emitt_90_phi_p",
        "units": "deg·MeV/c",
        "description": "Momentum-phase emittance (90%)",
    },
    "(PHI,dP) RMS-Emittance [deg.MeV/c]": {
        "property": "emitt_rms_phi_p",
        "units": "deg·MeV/c",
        "description": "Momentum-phase RMS emittance",
    },
    # Twiss Parameters - Transverse
    "(X,X') Alpha [1]": {
        "property": "alpha_x",
        "units": "-",
        "description": "X Twiss alpha",
    },
    "(X,X') Beta [m/rad]": {
        "property": "beta_x",
        "units": "m/rad",
        "description": "X Twiss beta",
    },
    "(Y,Y') Alpha [1]": {
        "property": "alpha_y",
        "units": "-",
        "description": "Y Twiss alpha",
    },
    "(Y,Y') Beta [m/rad]": {
        "property": "beta_y",
        "units": "m/rad",
        "description": "Y Twiss beta",
    },
    # Twiss Parameters - Longitudinal
    "(PHI,dE) Alpha [1]": {
        "property": "alpha_z",
        "units": "-",
        "description": "Longitudinal Twiss alpha",
    },
    "(PHI,dE) Beta [deg/MeV]": {
        "property": "beta_z",
        "units": "deg/MeV",
        "description": "Longitudinal Twiss beta",
    },
    "(PHI,dP) Alpha [1]": {
        "property": "alpha_phi_p",
        "units": "-",
        "description": "Momentum-phase Twiss alpha",
    },
    "(PHI,dP) Beta [deg.c/MeV]": {
        "property": "beta_phi_p",
        "units": "deg·c/MeV",
        "description": "Momentum-phase Twiss beta",
    },
    # Halo Parameters
    "Halo(X,BGX')": {
        "property": "halo_x",
        "units": "-",
        "description": "X halo parameter",
    },
    "Halo(Y,BGY')": {
        "property": "halo_y",
        "units": "-",
        "description": "Y halo parameter",
    },
    "Halo(Z,Z')": {
        "property": "halo_z",
        "units": "-",
        "description": "Z halo parameter",
    },
    # Cross-Plane Correlations
    "(X,Y) Alpha [1]": {
        "property": "alpha_x_y",
        "units": "-",
        "description": "X-Y correlation alpha",
    },
    "(X,Y) Beta [1]": {
        "property": "beta_x_y",
        "units": "-",
        "description": "X-Y correlation beta",
    },
    "(X,Y') Alpha [1]": {
        "property": "alpha_x_yp",
        "units": "-",
        "description": "X-Y' correlation alpha",
    },
    "(X,Y') Beta [m/rad]": {
        "property": "beta_x_yp",
        "units": "m/rad",
        "description": "X-Y' correlation beta",
    },
    "(X',Y) Alpha [1]": {
        "property": "alpha_xp_y",
        "units": "-",
        "description": "X'-Y correlation alpha",
    },
    "(X',Y) Beta [rad/m]": {
        "property": "beta_xp_y",
        "units": "rad/m",
        "description": "X'-Y correlation beta",
    },
    "(X',Y') Alpha [1]": {
        "property": "alpha_xp_yp",
        "units": "-",
        "description": "X'-Y' correlation alpha",
    },
    "(X',Y') Beta [1]": {
        "property": "beta_xp_yp",
        "units": "-",
        "description": "X'-Y' correlation beta",
    },
    # Wanted Emittance (User-defined emittance limits)
    "(X, BGX') Wanted Emittance [m.rad]": {
        "property": "wanted_emitt_norm_x_xp",
        "units": "m·rad",
        "description": "User-defined X emittance",
    },
    "(Y, BGY') Wanted Emittance [m.rad]": {
        "property": "wanted_emitt_norm_y_yp",
        "units": "m·rad",
        "description": "User-defined Y emittance",
    },
    "(PHI, dE) Wanted Emittance [deg.MeV]": {
        "property": "wanted_emitt_phi_ekin",
        "units": "deg·MeV",
        "description": "User-defined Z emittance",
    },
    "(PHI, dP) Wanted Emittance [deg.MeV/c]": {
        "property": "wanted_emitt_phi_p",
        "units": "deg·MeV/c",
        "description": "User-defined momentum-phase emittance",
    },
    # Wanted Emittance Beam Sizes
    " x beam size in wanted emittance [m]": {
        "property": "wanted_x_size",
        "units": "m",
        "description": "X beam size in wanted emittance",
    },
    " x' beam size in wanted emittance [rad]": {
        "property": "wanted_xp_size",
        "units": "rad",
        "description": "X' beam size in wanted emittance",
    },
    " y beam size in wanted emittance [m]": {
        "property": "wanted_y_size",
        "units": "m",
        "description": "Y beam size in wanted emittance",
    },
    " y' beam size in wanted emittance [rad]": {
        "property": "wanted_yp_size",
        "units": "rad",
        "description": "Y' beam size in wanted emittance",
    },
    " Phase beam size in wanted emittance [rad]": {
        "property": "wanted_phi_size",
        "units": "rad",
        "description": "Phase beam size in wanted emittance",
    },
    " Energy beam size in wanted emittance [GeV]": {
        "property": "wanted_energy_size",
        "units": "GeV",
        "description": "Energy beam size in wanted emittance",
    },
    # Additional Correlations
    "(X,Y) RMS-Emitt [m2]": {
        "property": "emitt_rms_x_y",
        "units": "m²",
        "description": "X-Y RMS emittance",
    },
    "(X,Y') RMS-Emitt [m2.rad2]": {
        "property": "emitt_rms_x_yp",
        "units": "m²·rad²",
        "description": "X-Y' RMS emittance",
    },
    "(X',Y) RMS-Emitt [m2.rad2]": {
        "property": "emitt_rms_xp_y",
        "units": "m²·rad²",
        "description": "X'-Y RMS emittance",
    },
    "(X',Y') RMS-Emitt [rad2]": {
        "property": "emitt_rms_xp_yp",
        "units": "rad²",
        "description": "X'-Y' RMS emittance",
    },
    # Phase-Space Correlations
    "(X,PH) Alpha [1]": {
        "property": "alpha_x_phi",
        "units": "-",
        "description": "X-Phase correlation alpha",
    },
    "(X,PH) Beta [m/deg]": {
        "property": "beta_x_phi",
        "units": "m/deg",
        "description": "X-Phase correlation beta",
    },
    "(X,PH)RMS-Emittance [m.deg]": {
        "property": "emitt_rms_x_phi",
        "units": "m·deg",
        "description": "X-Phase RMS emittance",
    },
    "(Y,PH) Alpha [1]": {
        "property": "alpha_y_phi",
        "units": "-",
        "description": "Y-Phase correlation alpha",
    },
    "(Y,PH) Beta [m/deg]": {
        "property": "beta_y_phi",
        "units": "m/deg",
        "description": "Y-Phase correlation beta",
    },
    "(Y,PH)RMS-Emittance [m.deg]": {
        "property": "emitt_rms_y_phi",
        "units": "m·deg",
        "description": "Y-Phase RMS emittance",
    },
}
