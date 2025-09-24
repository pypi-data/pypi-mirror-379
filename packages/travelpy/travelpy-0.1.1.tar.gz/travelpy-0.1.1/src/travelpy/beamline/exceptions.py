"""
Custom exceptions for travelpy Beamline class operations.

These exceptions provide clear, actionable error messages for beamline
manipulation operations.
"""


class TravelpyBeamlineError(Exception):
    """Base exception for beamline operations."""

    pass


class MultipleSentinelError(TravelpyBeamlineError):
    """Multiple SENTINEL cards found in beamline file."""

    def __init__(self, count: int):
        super().__init__(
            f"Found {count} SENTINEL cards in beamline file. "
            f"Only one SENTINEL card is allowed per file. "
            f"Use move_sentinel() to manage SENTINEL position."
        )


class MultipleCardsFoundError(TravelpyBeamlineError):
    """Multiple cards found when single card expected."""

    def __init__(self, card_name: str, count: int):
        super().__init__(
            f"Found {count} cards named '{card_name}'. "
            f"Use apply_to_all=True if you want to modify all cards with this name."
        )


class CardParameterError(TravelpyBeamlineError):
    """Invalid card parameter modification attempted."""

    def __init__(self, message: str):
        super().__init__(message)


class CardNotFoundError(TravelpyBeamlineError):
    """Card with specified name not found in beamline."""

    def __init__(self, card_name: str):
        super().__init__(f"No cards found with name '{card_name}' in beamline.")


class InvalidSentinelOperationError(TravelpyBeamlineError):
    """Invalid SENTINEL operation attempted."""

    def __init__(self, message: str):
        super().__init__(message)


class InvalidLineFormatError(TravelpyBeamlineError):
    """Invalid line format for insertion."""

    def __init__(self, message: str):
        super().__init__(message)


class InvalidBeamlineFileError(TravelpyBeamlineError):
    """Invalid beamline file format."""

    def __init__(self, message: str):
        super().__init__(message)
