"""
Game Playtime Tracker
Joe Widdifield
Unit tests for the Game class in tracker/models.py.
Resources: Python Crash Course, 3rd Edition (Chapter 11 - Testing Your Code)
10-30-2026
"""

import pytest

from tracker.models import Game


@pytest.fixture
def hades():
    """A Game instance with no sessions logged."""
    return Game("Hades")


def test_new_game_has_no_sessions(hades):
    """A newly created game starts with zero hours and zero sessions."""
    assert hades.title == "Hades"
    assert hades.get_total_hours() == 0
    assert hades.get_session_count() == 0


def test_add_session_updates_totals(hades):
    """Logging sessions increases the total hours and session count."""
    hades.add_session(2)
    hades.add_session(3.5)
    assert hades.get_total_hours() == 5.5
    assert hades.get_session_count() == 2


@pytest.mark.parametrize("bad_hours", [0, -1, -0.5])
def test_add_session_rejects_non_positive_hours(hades, bad_hours):
    """Zero or negative hours raise a ValueError and are not logged."""
    with pytest.raises(ValueError):
        hades.add_session(bad_hours)
    assert hades.get_session_count() == 0


def test_describe(hades):
    """describe() summarizes the title, total hours, and session count."""
    hades.add_session(4)
    assert hades.describe() == "Hades: 4 hours over 1 session(s)"
