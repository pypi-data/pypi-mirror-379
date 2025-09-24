"""
Physics calculation utilities for accelerator physics.

This module provides functions for calculating beam properties and
phase space parameters commonly used in accelerator physics.
"""

import math
from typing import List, Union

import numpy as np
import pandas as pd


def twiss2ellipse(alpha, beta, unnormalized_emittance, number_of_points=360):
    """
    Generate particle coordinates on RMS emittance ellipse in phase space.

    This function is the inverse of twiss_of_ensemble - it takes Twiss parameters
    and emittance and generates particle coordinates that lie on the RMS emittance
    ellipse in phase space.

    Args:
        alpha (float): Twiss alpha parameter
        beta (float): Twiss beta parameter
        unnormalized_emittance (float): Emittance
        number_of_points (int, optional): Number of points on ellipse. Defaults to 360.

    Returns:
        tuple: (var1, var2) numpy arrays of coordinates on the emittance ellipse
            - var1: Position-like coordinates
            - var2: Angle-like coordinates

    Example:
        >>> alpha, beta, emitt = 0.5, 2.0, 1e-6
        >>> x_ell, xp_ell = twiss2ellipse(alpha, beta, emitt, 360)
        >>> # Generated coordinates lie on RMS emittance ellipse
    """
    # Maximum x coordinate on ellipse
    x_max = math.sqrt(unnormalized_emittance * beta)

    # Generate angular parameter from 0 to 2π
    angles = np.linspace(0, 2.0 * math.pi, number_of_points)

    # Position coordinates (var1)
    var1 = np.array([x_max * math.cos(angle) for angle in angles])

    # Angle coordinates (var2)
    var2 = np.array(
        [
            -math.sqrt(unnormalized_emittance / beta)
            * ((alpha * math.cos(angle)) + math.sin(angle))
            for angle in angles
        ]
    )

    return var1, var2


def twiss_of_ensemble(var1, var2):
    """
    Calculate Twiss parameters from phase space coordinates.

    Takes two conjugate coordinates in phase space and returns the Twiss parameters
    and RMS emittance of the particle ensemble.

    Args:
        var1: Position-like coordinate (e.g., x for horizontal, y for vertical, z for longitudinal)
        var2: Momentum-like coordinate (e.g., xp for horizontal, yp for vertical, delta for longitudinal)

    Both arguments can be:
        - Python lists
        - NumPy arrays
        - Pandas Series

    Example usage:
        # Horizontal phase space
        alpha_x, beta_x, emit_x = twiss_of_ensemble(x, xp)

        # Vertical phase space
        alpha_y, beta_y, emit_y = twiss_of_ensemble(y, yp)


    Returns:
        tuple: (alpha, beta, unnormalized_rms_emittance)
            - alpha: Twiss alpha parameter (dimensionless)
            - beta: Twiss beta parameter (same units as var1/var2)
            - unnormalized_rms_emittance: RMS emittance (units of var1 × var2)

    Note:
        If the emittance is zero or negative, alpha and beta will be NaN.
    """
    # Convert to numpy arrays for consistent handling
    var1 = np.asarray(var1)
    var2 = np.asarray(var2)

    # Center the coordinates
    var1_centered = var1 - np.mean(var1)
    var2_centered = var2 - np.mean(var2)

    # Calculate RMS emittance
    unnormalized_rms_emittance = np.sqrt(
        np.mean(var1_centered * var1_centered) * np.mean(var2_centered * var2_centered)
        - np.mean(var1_centered * var2_centered) ** 2
    )

    # Calculate Twiss parameters
    if unnormalized_rms_emittance > 0.0:
        beta = np.mean(var1_centered * var1_centered) / unnormalized_rms_emittance
        alpha = -np.mean(var1_centered * var2_centered) / unnormalized_rms_emittance
    else:
        beta = float("nan")
        alpha = float("nan")

    return alpha, beta, unnormalized_rms_emittance


def make_phase_near(
    phase: Union[float, int, List, np.ndarray, pd.Series], phase0: Union[float, int]
) -> Union[float, int, List, np.ndarray, pd.Series]:
    """
    Adjust phase values to be near a reference phase by adding/subtracting 360° periods.

    This function unwraps phase values by finding the equivalent angle closest to a
    reference phase. This is useful for adjusting phase data to a specific reference.

    Args:
        phase: Phase value(s) to adjust (in degrees). Can be:
            - float: Single phase value, returns float
            - int: Single phase value, returns int
            - list: List of phase values, returns list
            - np.ndarray: NumPy array of phase values, returns np.ndarray
            - pd.Series: Pandas Series of phase values, returns pd.Series
        phase0: Reference phase value (in degrees) to get close to

    Returns:
        Phase value(s) adjusted to be near phase0, preserving input type.
        Each returned phase will be within ±180° of phase0.

    Examples:
        Single values:
        >>> make_phase_near(370.0, 10.0)
        10.0
        >>> make_phase_near(370, 10)  # int input returns int
        10

        Array inputs (type preserved):
        >>> phases = [10, 370, 730, -350]
        >>> make_phase_near(phases, 0)
        [10, 10, 10, 10]

        >>> import numpy as np
        >>> phases = np.array([10, 370, 730])
        >>> result = make_phase_near(phases, 0)
        >>> type(result)
        <class 'numpy.ndarray'>

    Note:
        This function adjusts each phase independently to the same reference.
        For smoothing phase arrays where each element should be close to the
        previous one, use smooth_phase_array() instead.
    """
    # Handle array-like inputs recursively
    if isinstance(phase, (list, np.ndarray, pd.Series)):
        if isinstance(phase, list):
            return [make_phase_near(phi, phase0) for phi in phase]
        elif isinstance(phase, np.ndarray):
            return np.array([make_phase_near(phi, phase0) for phi in phase])
        elif isinstance(phase, pd.Series):
            return pd.Series(
                [make_phase_near(phi, phase0) for phi in phase],
                index=phase.index,
                name=phase.name,
            )

    # Handle scalar inputs (float/int)
    n = (phase - phase0) // 360  # Number of 360° periods between phase and phase0

    # Check adjacent periods to find the closest match
    n_correction = 0
    distance = abs(phase - n * 360 - phase0)

    for i in [-1, 0, 1]:  # Check n-1, n, n+1 periods
        distance_i = abs(phase - (n + i) * 360 - phase0)
        if distance_i < distance:
            n_correction = i
            distance = distance_i

    result = phase - (n + n_correction) * 360

    # Preserve input type for scalars
    if isinstance(phase, int) and isinstance(result, (int, float)):
        return int(result)
    return result


def smooth_phase_array(
    array: Union[List, np.ndarray, pd.Series]
) -> Union[List, np.ndarray, pd.Series]:
    """
    Smooth phase array by unwrapping discontinuities between consecutive values.

    This function applies phase unwrapping to an array of phase values by making each
    phase value close to the previous one using make_phase_near(). This removes
    discontinuous jumps caused by 2π periodicity while preserving the underlying
    phase evolution.

    Args:
        array: Array of phase values (in degrees). Can be:
            - list: List of phase values, returns list
            - np.ndarray: NumPy array of phase values, returns np.ndarray
            - pd.Series: Pandas Series of phase values, returns pd.Series

    Returns:
        Smoothed phase array with same type as input. The first element remains
        unchanged as it serves as the reference point for unwrapping.

    Examples:
        Basic phase unwrapping:
        >>> phases = [10, 15, 380, 385, 720]  # Has 360° jumps
        >>> smooth_phase_array(phases)
        [10, 15, 20, 25, 360]  # Smooth progression

        NumPy array (type preserved):
        >>> import numpy as np
        >>> phases = np.array([0, 10, 370, 380])
        >>> result = smooth_phase_array(phases)
        >>> result
        array([  0,  10,  10,  20])
        >>> type(result)
        <class 'numpy.ndarray'>

        Pandas Series (preserves index and name):
        >>> import pandas as pd
        >>> phases = pd.Series([45, 50, 410, 415], name='rf_phase')
        >>> smooth_phase_array(phases)
        0     45
        1     50
        2     50
        3     55
        Name: rf_phase, dtype: int64

        Real-world TRAVEL RF phase data:
        >>> rf_phases = [0, 30, 60, 420, 450]  # 420° = 60° + 360°
        >>> smoothed = smooth_phase_array(rf_phases)
        >>> # Result: [0, 30, 60, 60, 90] - continuous evolution

    Note:
        - The first element is used as the starting reference and remains unchanged
        - Order matters: the function processes elements sequentially
        - Particularly useful for TRAVEL simulation output where RF phases
          may have 360° discontinuities that need to be unwrapped for analysis
    """
    # Handle different input types
    if isinstance(array, list):
        result = list(array)  # Copy the input list
        for i in range(1, len(result)):
            result[i] = make_phase_near(result[i], result[i - 1])
        return result

    elif isinstance(array, np.ndarray):
        result = array.copy()
        for i in range(1, len(result)):
            result[i] = make_phase_near(result[i], result[i - 1])
        return result

    elif isinstance(array, pd.Series):
        result = array.copy()
        for i in range(1, len(result)):
            result.iloc[i] = make_phase_near(result.iloc[i], result.iloc[i - 1])
        return result

    else:
        raise TypeError(
            f"Unsupported array type '{type(array).__name__}': supported types are list, np.ndarray, pd.Series"
        )
