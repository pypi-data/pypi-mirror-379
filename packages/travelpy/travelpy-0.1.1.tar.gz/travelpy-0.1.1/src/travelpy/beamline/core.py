"""
Core Beamline class implementation for travelpy.

Provides safe, intuitive methods for modifying TRAVEL beamline files
while maintaining compatibility with tp.run_travel() workflows.
"""

import copy
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from .exceptions import (
    CardNotFoundError,
    InvalidSentinelOperationError,
    MultipleCardsFoundError,
    MultipleSentinelError,
)
from .validation import (
    extract_card_parameters,
    find_named_cards,
    find_sentinel_lines,
    reconstruct_card_line,
    validate_card_parameter_index,
    validate_line_for_insertion,
)


class Beamline:
    """
    TRAVEL beamline file manipulation class.

    Provides safe, intuitive methods for modifying TRAVEL beamline files
    while maintaining compatibility with tp.run_travel() workflows.

    Examples:
        >>> bl = Beamline('beamline.in')
        >>> bl.update_card(card_name="Q1", parameter_index=2, new_value=125.0)
        >>> bl.write("modified_beamline.in")
        >>> result = tp.run_travel("beam.dat", "modified_beamline.in")
    """

    def __init__(self, beamline_file: Union[str, Path]):
        """
        Initialize Beamline object from file.

        Args:
            beamline_file: Path to TRAVEL beamline file

        Raises:
            FileNotFoundError: If beamline file doesn't exist
            MultipleSentinelError: If multiple SENTINEL cards found
            InvalidBeamlineFileError: If file format is invalid
        """
        self._file_path = Path(beamline_file)

        if not self._file_path.exists():
            raise FileNotFoundError(f"Beamline file not found: {self._file_path}")

        # Load file content
        try:
            with open(self._file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            # Try with different encoding
            with open(self._file_path, "r", encoding="latin-1") as f:
                content = f.read()

        # Track if original file ended with newline
        self._original_ends_with_newline = content.endswith("\n")

        # Split into lines, preserving empty lines
        if content:
            self._lines = content.splitlines(keepends=True)
            # Ensure all lines have newlines for internal consistency
            self._lines = [
                line if line.endswith("\n") else line + "\n" for line in self._lines
            ]
        else:
            self._lines = []

        # Store initial state for restore()
        self._initial_lines = copy.deepcopy(self._lines)

        # Validate SENTINEL cards
        self._validate_sentinel_cards()

        # Build named card index
        self._named_cards = find_named_cards(self._lines)

        # Track modifications (for future features)
        self._modifications_log = []

    def _validate_sentinel_cards(self) -> None:
        """Validate that file has at most one SENTINEL card."""
        sentinel_lines = find_sentinel_lines(self._lines)

        if len(sentinel_lines) > 1:
            raise MultipleSentinelError(len(sentinel_lines))

        # Store sentinel information
        self._sentinel_indices = [idx for idx, _ in sentinel_lines]

    def write(self, filename: Union[str, Path]) -> None:
        """
        Write current beamline state to file.

        Args:
            filename: Output file path

        Examples:
            >>> bl.write("modified_beamline.in")
            >>> result = tp.run_travel("beam.dat", "modified_beamline.in")
        """
        output_path = Path(filename)

        # Use Windows CRLF line endings for TRAVEL compatibility
        with open(output_path, "w", encoding="utf-8", newline="\r\n") as f:
            for i, line in enumerate(self._lines):
                # Strip existing line endings and let Python add CRLF
                line_content = line.rstrip("\r\n")

                # For the last line, respect original file ending behavior
                if i == len(self._lines) - 1 and not self._original_ends_with_newline:
                    # Write without newline for last line if original didn't have it
                    f.write(line_content)
                else:
                    # Write with newline (Python will add CRLF)
                    f.write(line_content + "\n")

    def restore(self) -> None:
        """
        Restore beamline to original loaded state.

        Examples:
            >>> bl.update_card(card_name="Q1", parameter_index=2, new_value=999.0)
            >>> bl.restore()  # Back to original state
        """
        self._lines = copy.deepcopy(self._initial_lines)
        self._named_cards = find_named_cards(self._lines)
        self._validate_sentinel_cards()
        self._modifications_log.clear()

        # Restore original ending behavior (already preserved in _initial_lines)

    def update_card(
        self,
        card_name: str,
        parameter_index: int,
        new_value: Union[str, float],
        apply_to_all: bool = False,
    ) -> None:
        """
        Update Travel card parameter by name.

        Args:
            card_name: Name of card to update (e.g., "Q1", "Drift1")
            parameter_index: 0-based parameter index (0=card number forbidden, 1+=allowed)
            new_value: New parameter value
            apply_to_all: If True, update all cards with this name. Default False.

        Raises:
            MultipleCardsFoundError: Multiple cards found and apply_to_all=False
            CardParameterError: Invalid parameter index or forbidden modification
            CardNotFoundError: No cards found with specified name

        Examples:
            >>> bl.update_card(card_name="Q1", parameter_index=2, new_value=125.0)
            >>> bl.update_card(card_name="Drift1", parameter_index=1, new_value=0.5, apply_to_all=True)
        """
        # Validate parameter index
        validate_card_parameter_index(parameter_index)

        # Find cards with this name
        if card_name not in self._named_cards:
            raise CardNotFoundError(card_name)

        indices = self._named_cards[card_name]

        # Check for multiple cards
        if len(indices) > 1 and not apply_to_all:
            raise MultipleCardsFoundError(card_name, len(indices))

        # Update each matching card
        for idx in indices:
            self._update_card_at_index(idx, parameter_index, new_value)

        # Log modification
        self._modifications_log.append(
            f"Updated {card_name} parameter_index {parameter_index} to {new_value}"
        )

    def _update_card_at_index(
        self, line_index: int, parameter_index: int, new_value: Union[str, float]
    ) -> None:
        """Update card parameter at specific line index."""
        line = self._lines[line_index]
        parameters = extract_card_parameters(line)

        # Ensure we have enough parameters
        while len(parameters) <= parameter_index:
            parameters.append("0")  # Default value for missing parameters

        # Update the parameter (already 0-based index)
        parameters[parameter_index] = str(new_value)

        # Reconstruct line
        self._lines[line_index] = reconstruct_card_line(parameters) + "\n"

    def comment_card(self, card_name: str, apply_to_all: bool = False) -> None:
        """
        Comment card by name.

        Args:
            card_name: Name of card to comment
            apply_to_all: If True, comment all cards with this name. Default False.

        Raises:
            MultipleCardsFoundError: Multiple cards found and apply_to_all=False
            CardNotFoundError: No cards found with specified name

        Examples:
            >>> bl.comment_card(card_name="OldQuad")
            >>> bl.comment_card(card_name="TempElement", apply_to_all=True)
        """
        if card_name not in self._named_cards:
            raise CardNotFoundError(card_name)

        indices = self._named_cards[card_name]

        if len(indices) > 1 and not apply_to_all:
            raise MultipleCardsFoundError(card_name, len(indices))

        # Comment each matching card
        for idx in indices:
            line = self._lines[idx]
            if not line.strip().upper().startswith("C"):
                self._lines[idx] = "c" + line

        # Log modification
        self._modifications_log.append(f"Commented card {card_name}")

    def uncomment_card(self, card_name: str, apply_to_all: bool = False) -> None:
        """
        Uncomment card by name.

        Args:
            card_name: Name of card to uncomment
            apply_to_all: If True, uncomment all cards with this name. Default False.

        Raises:
            MultipleCardsFoundError: Multiple cards found and apply_to_all=False
            CardNotFoundError: No cards found with specified name

        Examples:
            >>> bl.uncomment_card(card_name="RestoredQuad")
        """
        if card_name not in self._named_cards:
            raise CardNotFoundError(card_name)

        indices = self._named_cards[card_name]

        if len(indices) > 1 and not apply_to_all:
            raise MultipleCardsFoundError(card_name, len(indices))

        # Uncomment each matching card
        for idx in indices:
            line = self._lines[idx]
            stripped = line.strip()
            if stripped.upper().startswith("C"):
                # Remove the 'c' or 'C' prefix, preserving newline
                if line.endswith("\n"):
                    self._lines[idx] = line[1:]
                else:
                    self._lines[idx] = line[1:] + "\n"

        # Log modification
        self._modifications_log.append(f"Uncommented card {card_name}")

    def insert_line(
        self,
        line: str,
        before: Optional[str] = None,
        after: Optional[str] = None,
        apply_to_all: bool = False,
    ) -> None:
        """
        Insert line before/after named card.

        Args:
            line: Line content to insert
            before: Insert before this card name
            after: Insert after this card name
            apply_to_all: If True, insert at all matching card positions

        Raises:
            ValueError: If both before and after specified, or neither specified
            InvalidLineFormatError: If line format is invalid
            MultipleCardsFoundError: Multiple cards found and apply_to_all=False
            CardNotFoundError: Target card not found

        Examples:
            >>> bl.insert_line("c This is a comment", before="Q1")
            >>> bl.insert_line('5 0.1 150.0 10.0 0 0 0 0 "NewQuad";', after="Q1")
        """
        # Validate arguments
        if (before is None) == (after is None):
            raise ValueError(
                "Invalid insertion position: specify exactly one of 'before' or 'after'"
            )

        # Validate line format
        validate_line_for_insertion(line)

        # Determine target card name and position
        target_name = before if before is not None else after
        insert_before = before is not None

        # Find target card
        if target_name not in self._named_cards:
            raise CardNotFoundError(target_name)

        indices = self._named_cards[target_name]

        if len(indices) > 1 and not apply_to_all:
            raise MultipleCardsFoundError(target_name, len(indices))

        # Insert at each position (reverse order to maintain indices)
        for idx in sorted(indices, reverse=True):
            insert_idx = idx if insert_before else idx + 1
            self._lines.insert(insert_idx, line + "\n")

        # Rebuild named cards index (indices have changed)
        self._named_cards = find_named_cards(self._lines)

        # Log modification
        position = "before" if insert_before else "after"
        self._modifications_log.append(f"Inserted line {position} {target_name}")

    def move_sentinel(
        self,
        before: Optional[str] = None,
        after: Optional[str] = None,
        end: bool = False,
    ) -> None:
        """
        Move SENTINEL card to specified position.

        Args:
            before: Move before this card name (must be unique)
            after: Move after this card name (must be unique)
            end: Move to end of file

        Raises:
            ValueError: If multiple or no position arguments specified
            InvalidSentinelOperationError: If target has multiple cards
            CardNotFoundError: Target card not found

        Note: NO apply_to_all option - target must be unambiguous

        Examples:
            >>> bl.move_sentinel(before="FinalQuad")
            >>> bl.move_sentinel(end=True)
        """
        # Validate arguments
        position_args = [before is not None, after is not None, end]
        if sum(position_args) != 1:
            raise ValueError(
                "Invalid SENTINEL position: specify exactly one of 'before', 'after', or 'end'"
            )

        # Find current SENTINEL
        sentinel_lines = find_sentinel_lines(self._lines)
        if not sentinel_lines:
            raise InvalidSentinelOperationError("No SENTINEL card found to move")

        sentinel_idx, sentinel_content = sentinel_lines[0]

        # For non-end moves, validate target BEFORE making any modifications
        if not end:
            target_name = before if before is not None else after

            # Find target card using current index (before SENTINEL removal)
            if target_name not in self._named_cards:
                raise CardNotFoundError(target_name)

            indices = self._named_cards[target_name]

            # SENTINEL operations must be unambiguous
            if len(indices) > 1:
                raise InvalidSentinelOperationError(
                    f"Cannot move SENTINEL: found {len(indices)} cards named '{target_name}', target must be unique"
                )

        # ALL validation passed - now safe to modify
        # Remove current SENTINEL
        del self._lines[sentinel_idx]

        if end:
            # Add to end of file
            self._lines.append(sentinel_content)
        else:
            # Find target position after SENTINEL removal
            insert_before = before is not None

            # Rebuild index since we removed a line (SENTINEL)
            # All line indices after the removed SENTINEL are now shifted
            self._named_cards = find_named_cards(self._lines)

            # Find target again (indices may have shifted)
            indices = self._named_cards[target_name]
            target_idx = indices[0]  # We already validated it's unique
            insert_idx = target_idx if insert_before else target_idx + 1
            self._lines.insert(insert_idx, sentinel_content)

        # Rebuild indices
        self._named_cards = find_named_cards(self._lines)
        self._validate_sentinel_cards()

        # Log modification
        if end:
            self._modifications_log.append("Moved SENTINEL to end of file")
        else:
            position = "before" if insert_before else "after"
            self._modifications_log.append(f"Moved SENTINEL {position} {target_name}")

    def print_lines(
        self,
        lines_range: Optional[range] = None,
        max_lines: int = 50,
    ) -> None:
        """
        Display beamline content with console output.

        Args:
            lines_range: Specific range to display
            max_lines: Maximum lines for console display

        Examples:
            >>> bl.print_lines()  # Show lines with pagination
            >>> bl.print_lines(range(10, 20))  # Show specific lines
            >>> bl.print_lines(max_lines=100)  # Show more lines
        """
        if lines_range is not None:
            # Show specific range
            self._print_range_to_console(lines_range)
            return

        # Always use console display
        self._print_to_console(max_lines)

    def _print_range_to_console(self, lines_range: range) -> None:
        """Print specific line range to console."""
        print("Line# -> Content")
        print("-" * 50)
        for i in lines_range:
            if 0 <= i < len(self._lines):
                print(f"{i:4d} -> {self._lines[i].rstrip()}")

    def _print_to_console(self, max_lines: int) -> None:
        """Print lines to console with limit."""
        print("Line# -> Content")
        print("-" * 50)
        for i, line in enumerate(self._lines[:max_lines]):
            print(f"{i:4d} -> {line.rstrip()}")

        if len(self._lines) > max_lines:
            print(f"... ({len(self._lines) - max_lines} more lines)")
            print("Use print_lines(max_lines=999999) for full view")

    def get_card_info(self, card_name: str) -> List[Dict[str, Any]]:
        """
        Get card information by name.

        Args:
            card_name: Name of card to get info for

        Returns:
            List of dictionaries with card information (one dict per card found)

        Raises:
            CardNotFoundError: Card not found

        Examples:
            >>> infos = bl.get_card_info(card_name="Q1")  # Always returns list
            >>> print(f"Found {len(infos)} cards named 'Q1'")
            >>> if infos:
            ...     print(f"First card type: {infos[0]['card_type']}")
        """
        if card_name not in self._named_cards:
            raise CardNotFoundError(card_name)

        indices = self._named_cards[card_name]

        cards = []
        for idx in indices:
            line = self._lines[idx]
            parameters = extract_card_parameters(line)
            is_commented = line.strip().upper().startswith("C")

            # For commented cards, extract the card type from the comment prefix
            card_type = None
            if parameters:
                if is_commented:
                    # Handle different comment formats:
                    # c3, C3 -> card type 3 (attached)
                    # c 3, C 3, c    3 -> card type 3 (separated)
                    first_param = parameters[0].upper()
                    if first_param.startswith("C"):
                        # Remove 'C' prefix and any remaining spaces
                        card_number_str = first_param[1:].strip()
                        if card_number_str:
                            # Format: c3, C3
                            try:
                                card_type = int(card_number_str)
                            except ValueError:
                                card_type = None
                        else:
                            # Format: c 3, C 3 - card number is in second parameter
                            if len(parameters) > 1:
                                try:
                                    card_type = int(parameters[1])
                                except ValueError:
                                    card_type = None
                else:
                    # For non-commented cards, first parameter is the card type
                    try:
                        card_type = int(parameters[0])
                    except ValueError:
                        card_type = None

            cards.append(
                {
                    "card_name": card_name,
                    "line_index": idx,
                    "line_content": line.strip(),
                    "card_type": card_type,
                    "parameters": parameters,
                    "is_commented": is_commented,
                }
            )

        return cards

    def get_duplicate_names(self) -> Dict[str, int]:
        """
        Get cards with non-unique names.

        Returns:
            Dictionary mapping card names to occurrence counts

        Examples:
            >>> duplicates = bl.get_duplicate_names()
            >>> if duplicates:
            ...     print("Cards with duplicate names:", duplicates)
        """
        return {
            name: len(indices)
            for name, indices in self._named_cards.items()
            if len(indices) > 1
        }

    @property
    def line_count(self) -> int:
        """Get total number of lines in beamline."""
        return len(self._lines)

    @property
    def card_count(self) -> int:
        """Get total number of named cards in beamline."""
        return sum(len(indices) for indices in self._named_cards.values())

    @property
    def card_names(self) -> List[str]:
        """Get list of all card names in beamline."""
        return list(self._named_cards.keys())

    def __repr__(self) -> str:
        return f"Beamline('{self._file_path.name}', {self.line_count} lines, {self.card_count} cards)"
