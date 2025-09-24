"""Custom exceptions for travelpy."""


class TravelpyError(Exception):
    """Base exception for all travelpy errors."""

    pass


class TravelNotFoundError(TravelpyError):
    """Raised when TRAVEL executable cannot be found."""

    pass


class SimulationError(TravelpyError):
    """Raised when TRAVEL simulation fails."""

    pass


class BeamFileError(TravelpyError):
    """Raised when beam file cannot be read or is invalid."""

    pass


class BeamlineFileError(TravelpyError):
    """Raised when beamline file cannot be read or is invalid."""

    pass


class ConfigurationError(TravelpyError):
    """Raised when configuration is invalid or missing."""

    pass


# Import beamline exceptions for convenience
