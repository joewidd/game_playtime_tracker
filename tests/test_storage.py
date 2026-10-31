"""
Game Playtime Tracker
Joe Widdifield
Unit tests for saving and loading the library in tracker/storage.py.
Every test writes to pytest's tmp_path so the real save file is untouched.
Resources: Python Crash Course, 3rd Edition (Chapter 11 - Testing Your Code)
10-31-2026
"""

import json

import pytest

from tracker.exceptions import CorruptSaveFileError
from tracker.library import create_default_library
from tracker.models import StoryGame, LiveServiceGame
from tracker.storage import game_from_dict, load_library, save_library


@pytest.fixture
def save_path(tmp_path):
    """A path for a save file inside a temporary test directory."""
    return tmp_path / "playtime_data.json"


@pytest.fixture
def played_library():
    """The default library with some playtime, a completion, and a rank."""
    library = create_default_library()
    hades = library.get_game("Hades")
    hades.add_session(3)
    hades.add_session(1.5)
    hades.mark_completed()
    library.get_game("Tekken").update_rank("Gold")
    return library


def test_story_game_to_dict():
    """A StoryGame's dictionary includes its type and completion status."""
    hades = StoryGame("Hades")
    hades.add_session(2)
    assert hades.to_dict() == {"type": "StoryGame", "title": "Hades",
                               "sessions": [2], "completed": False}


def test_game_from_dict_rebuilds_correct_subclass():
    """The saved "type" decides which class is rebuilt."""
    game = game_from_dict({"type": "LiveServiceGame", "title": "Deadlock",
                           "sessions": [1, 2], "rank": "Archon"})
    assert isinstance(game, LiveServiceGame)
    assert game.get_total_hours() == 3
    assert game.rank == "Archon"


def test_save_writes_json_file(save_path, played_library):
    """Saving creates a JSON file with one entry per game."""
    save_library(played_library, save_path)
    games_data = json.loads(save_path.read_text())
    assert len(games_data) == 13
    assert games_data[0]["title"] == "Hades"


def test_save_then_load_round_trip(save_path, played_library):
    """Loading a saved library restores every game's data."""
    save_library(played_library, save_path)
    loaded = load_library(save_path)

    hades = loaded.get_game("Hades")
    assert hades.get_total_hours() == 4.5
    assert hades.get_session_count() == 2
    assert hades.completed is True
    assert loaded.get_game("Tekken").rank == "Gold"
    assert loaded.get_titles() == played_library.get_titles()


def test_load_missing_file_returns_default_library(save_path):
    """On the first run, with no save file, the starting games are used."""
    library = load_library(save_path)
    assert library.get_titles() == create_default_library().get_titles()
    assert library.get_total_hours() == 0


@pytest.mark.parametrize("bad_contents", [
    "{not valid json",
    '[{"title": "Hades"}]',
    '[{"type": "Arcade", "title": "Pac-Man", "sessions": []}]',
    "42",
])
def test_load_corrupt_file_raises(save_path, bad_contents):
    """Unreadable or incomplete save data raises CorruptSaveFileError."""
    save_path.write_text(bad_contents)
    with pytest.raises(CorruptSaveFileError):
        load_library(save_path)
