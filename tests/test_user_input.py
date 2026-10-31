"""
Game Playtime Tracker
Joe Widdifield
Unit tests for the input parsing functions in tracker/user_input.py.
Resources: Python Crash Course, 3rd Edition (Chapter 11 - Testing Your Code)
10-31-2026
"""

import pytest

from tracker.exceptions import InvalidHoursError
from tracker.user_input import is_quit_command, parse_hours


@pytest.mark.parametrize("text", ["q", "quit", "Q", "  QUIT  "])
def test_is_quit_command_accepts_quit_words(text):
    """'q' and 'quit' count as quitting in any case, with extra spaces."""
    assert is_quit_command(text)


@pytest.mark.parametrize("text", ["", "hades", "quitting", "5"])
def test_is_quit_command_rejects_other_text(text):
    """Anything other than 'q' or 'quit' is not a quit command."""
    assert not is_quit_command(text)


@pytest.mark.parametrize("text, expected", [("3", 3.0), ("1.5", 1.5),
                                            (" 2 ", 2.0)])
def test_parse_hours_valid(text, expected):
    """Positive whole and decimal numbers are converted to floats."""
    assert parse_hours(text) == expected


@pytest.mark.parametrize("text", ["abc", "", "0", "-4"])
def test_parse_hours_invalid(text):
    """Non-numbers, zero, and negatives raise InvalidHoursError."""
    with pytest.raises(InvalidHoursError):
        parse_hours(text)
