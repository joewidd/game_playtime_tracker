"""
Game Playtime Tracker
Joe Widdifield
Unit tests for the GameLibrary class and create_default_library()
in tracker/library.py.
Resources: Python Crash Course, 3rd Edition (Chapter 11 - Testing Your Code)
10-30-2026
"""

import pytest

from tracker.exceptions import DuplicateGameError, GameNotFoundError
from tracker.library import GameLibrary, create_default_library
from tracker.models import Game, StoryGame, LiveServiceGame


@pytest.fixture
def library():
    """A small library with two games and no sessions logged."""
    library = GameLibrary()
    library.add_game(StoryGame("Hades"))
    library.add_game(LiveServiceGame("Overwatch"))
    return library


def test_get_game_ignores_case_and_spaces(library):
    """Lookups match titles regardless of capitalization or extra spaces."""
    assert library.get_game("hades").title == "Hades"
    assert library.get_game("  OVERWATCH ").title == "Overwatch"


def test_get_game_missing_raises(library):
    """Looking up a game that isn't in the library raises an error."""
    with pytest.raises(GameNotFoundError):
        library.get_game("Tetris")


def test_add_duplicate_game_raises(library):
    """Adding a second game with the same title raises DuplicateGameError."""
    with pytest.raises(DuplicateGameError):
        library.add_game(Game("HADES"))


def test_get_titles(library):
    """get_titles() lists every game in the order they were added."""
    assert library.get_titles() == ["Hades", "Overwatch"]


def test_get_total_hours(library):
    """Total hours add up sessions from every game."""
    library.get_game("Hades").add_session(3)
    library.get_game("Overwatch").add_session(1.5)
    assert library.get_total_hours() == 4.5


def test_get_most_played(library):
    """The game with the most hours is returned as most played."""
    library.get_game("Hades").add_session(3)
    library.get_game("Overwatch").add_session(5)
    assert library.get_most_played().title == "Overwatch"


def test_get_most_played_with_no_sessions(library):
    """With no sessions logged, there is no most played game."""
    assert library.get_most_played() is None


def test_default_library_uses_correct_game_types():
    """The starting library contains all 13 games with the right subclass."""
    library = create_default_library()
    assert len(library.get_titles()) == 13
    assert isinstance(library.get_game("Elden Ring"), StoryGame)
    assert isinstance(library.get_game("Deadlock"), LiveServiceGame)
