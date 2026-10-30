"""
Game Playtime Tracker
Joe Widdifield
Unit tests for the Game, StoryGame, and LiveServiceGame classes in
tracker/models.py.
Resources: Python Crash Course, 3rd Edition (Chapter 11 - Testing Your Code)
10-30-2026
"""

import pytest

from tracker.models import Game, StoryGame, LiveServiceGame


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


def test_story_game_inherits_session_tracking():
    """StoryGame reuses Game's session methods and starts incomplete."""
    elden_ring = StoryGame("Elden Ring")
    elden_ring.add_session(10)
    assert elden_ring.get_total_hours() == 10
    assert elden_ring.completed is False


def test_story_game_mark_completed():
    """mark_completed() sets the flag and shows up in describe()."""
    elden_ring = StoryGame("Elden Ring")
    elden_ring.mark_completed()
    assert elden_ring.completed is True
    assert elden_ring.describe().endswith("- Completed")


def test_live_service_game_default_rank():
    """A LiveServiceGame starts Unranked unless a rank is given."""
    assert LiveServiceGame("Overwatch").rank == "Unranked"
    assert LiveServiceGame("Tekken", rank="Gold").rank == "Gold"


def test_live_service_game_update_rank():
    """update_rank() changes the rank shown in describe()."""
    overwatch = LiveServiceGame("Overwatch")
    overwatch.add_session(2)
    overwatch.update_rank("Diamond")
    assert overwatch.describe() == (
        "Overwatch: 2 hours over 1 session(s) - Rank: Diamond")
