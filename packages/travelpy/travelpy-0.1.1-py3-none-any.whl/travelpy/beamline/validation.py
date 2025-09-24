"""
Input validation utilities for travelpy Beamline class.

Provides validation functions for line insertion, card syntax,
and other beamline operations.
"""

import re
from typing import List, Tuple

from .exceptions import InvalidLineFormatError


def validate_line_for_insertion(line: str) -> None:
    """
    Validate a line before insertion into beamline.

    Args:
        line: Line content to validate

    Raises:
        InvalidLineFormatError: If line format is invalid

    Validation rules:
        - Comments (starting with c/C): Allow anything except SENTINEL
        - Cards: Must end with ';', have quoted name, start with number
        - FORBIDDEN: Lines starting with 'sentinel' (case-insensitive)
    """
    stripped = line.strip()

    if not stripped:
        # Empty lines are OK
        return

    # Check for forbidden SENTINEL insertion
    if stripped.upper().startswith("SENTINEL") or stripped.upper().startswith(
        "CSENTINEL"
    ):
        raise InvalidLineFormatError(
            "Cannot insert SENTINEL lines. Use move_sentinel() method instead."
        )

    # Check if it's a comment line
    if stripped.upper().startswith("C"):
        # Comments are generally OK, just check for SENTINEL content
        if "SENTINEL" in stripped.upper() and not stripped.upper().startswith("C"):
            raise InvalidLineFormatError(
                "Cannot insert lines containing uncommented SENTINEL. "
                "Use move_sentinel() method instead."
            )
        return

    # If not a comment, validate as a TRAVEL card
    _validate_card_syntax(stripped)


def _validate_card_syntax(line: str) -> None:
    """
    Validate TRAVEL card syntax.

    Args:
        line: Card line to validate

    Raises:
        InvalidLineFormatError: If card syntax is invalid
    """
    stripped = line.strip()

    # Must end with semicolon
    if not stripped.endswith(";"):
        raise InvalidLineFormatError(
            f"TRAVEL cards must end with semicolon (;). Got: {stripped}"
        )

    # Must start with a number (card type)
    if not re.match(r"^\d+", stripped):
        raise InvalidLineFormatError(
            f"TRAVEL cards must start with card number. Got: {stripped}"
        )

    # Must have quoted name
    if not re.search(r'"[^"]*"', stripped):
        raise InvalidLineFormatError(
            f"TRAVEL cards must have quoted name. Got: {stripped}"
        )


def find_sentinel_lines(lines: List[str]) -> List[Tuple[int, str]]:
    """
    Find all SENTINEL lines in beamline (case-insensitive).

    Args:
        lines: List of beamline lines

    Returns:
        List of (line_index, line_content) tuples for SENTINEL lines
    """
    sentinel_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip().upper()
        # Check for uncommented SENTINEL
        if stripped.startswith("SENTINEL") and not stripped.startswith("C"):
            sentinel_lines.append((i, line))

    return sentinel_lines


def find_named_cards(lines: List[str]) -> dict:
    """
    Find all named cards in beamline (including commented cards).

    Args:
        lines: List of beamline lines

    Returns:
        Dictionary mapping card names to list of line indices
    """
    named_cards = {}

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            continue

        # Skip SENTINEL (commented or not)
        if stripped.upper().startswith("SENTINEL") or stripped.upper().startswith(
            "CSENTINEL"
        ):
            continue

        # For commented lines, check if they contain a card
        working_line = stripped
        if stripped.upper().startswith("C"):
            # Remove comment prefix to check for card content
            working_line = stripped[1:].strip()

        # Skip if it's just a comment with no card content
        if not working_line or not re.match(r"^\d+", working_line):
            continue

        # Extract quoted name
        name_match = re.search(r'"([^"]*)"', working_line)
        if name_match:
            name = name_match.group(1)
            if name not in named_cards:
                named_cards[name] = []
            named_cards[name].append(i)

    return named_cards


def validate_card_parameter_index(
    parameter_index: int, max_parameters: int = None
) -> None:
    """
    Validate card parameter index.

    Args:
        parameter_index: 0-based parameter index to validate
        max_parameters: Maximum allowed parameter index (optional)

    Raises:
        CardParameterError: If parameter index is invalid
    """
    from .exceptions import CardParameterError

    if parameter_index < 0:
        raise CardParameterError(
            f"Invalid parameter index: must be >= 0, got {parameter_index}"
        )

    if parameter_index == 0:
        raise CardParameterError(
            "Cannot modify parameter index 0: card number modification would change element type"
        )

    if max_parameters is not None and parameter_index > max_parameters:
        raise CardParameterError(
            f"Parameter index {parameter_index} exceeds maximum {max_parameters}"
        )


def extract_card_parameters(line: str) -> List[str]:
    """
    Extract parameters from a TRAVEL card line.

    Args:
        line: TRAVEL card line

    Returns:
        List of parameter strings (including card number as first parameter)
    """
    stripped = line.strip()

    # Find the first semicolon that's not inside quotes - this marks the end of parameters
    semicolon_pos = None
    in_quotes = False
    for i, char in enumerate(stripped):
        if char == '"':
            in_quotes = not in_quotes
        elif char == ";" and not in_quotes:
            semicolon_pos = i
            break

    # Extract only the part before the semicolon
    if semicolon_pos is not None:
        stripped = stripped[:semicolon_pos]

    # Split on whitespace, but preserve quoted strings
    parts = []
    current_part = ""
    in_quotes = False

    for char in stripped:
        if char == '"':
            in_quotes = not in_quotes
            current_part += char
        elif char.isspace() and not in_quotes:
            if current_part:
                parts.append(current_part)
                current_part = ""
        else:
            current_part += char

    if current_part:
        parts.append(current_part)

    return parts


def reconstruct_card_line(parameters: List[str]) -> str:
    """
    Reconstruct TRAVEL card line from parameters.

    Args:
        parameters: List of parameter strings

    Returns:
        Reconstructed card line with semicolon
    """
    return " ".join(parameters) + ";"
