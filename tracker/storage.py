"""
Game Playtime Tracker
Joe Widdifield
Saves the game library to a JSON file and loads it back, so logged
playtime persists between runs of the program.
Resources: Python Crash Course, 3rd Edition (Chapter 10 - Files and
Exceptions, Storing Data)
10-31-2026
"""

import json
from pathlib import Path

from tracker.exceptions import CorruptSaveFileError
from tracker.library import GameLibrary, create_default_library
from tracker.models import Game, StoryGame, LiveServiceGame

DEFAULT_SAVE_PATH = Path("playtime_data.json")

# Maps the "type" saved in each game's dictionary back to its class.
GAME_CLASSES = {
    "Game": Game,
    "StoryGame": StoryGame,
    "LiveServiceGame": LiveServiceGame,
}


def game_from_dict(game_data):
    """Rebuild the correct kind of Game object from a saved dictionary."""
    game_class = GAME_CLASSES[game_data["type"]]
    game = game_class(game_data["title"])
    game.update_from_dict(game_data)
    return game


def save_library(library, path=DEFAULT_SAVE_PATH):
    """Write every game in the library to a JSON file at path."""
    games_data = [game.to_dict() for game in library.games.values()]
    path.write_text(json.dumps(games_data, indent=4))


def load_library(path=DEFAULT_SAVE_PATH):
    """
    Load the library saved at path.

    Returns the default starting library if no save file exists yet.
    Raises CorruptSaveFileError if the file can't be read as playtime data.
    """
    try:
        contents = path.read_text()
    except FileNotFoundError:
        return create_default_library()

    try:
        games_data = json.loads(contents)
        library = GameLibrary()
        for game_data in games_data:
            library.add_game(game_from_dict(game_data))
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise CorruptSaveFileError(
            f"Could not read save file '{path}'.") from error
    return library
