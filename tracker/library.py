"""
Game Playtime Tracker
Joe Widdifield
Defines the GameLibrary class, which holds the user's collection of
Game objects and answers questions about it (lookups, totals, most played).
Resources: Python Crash Course, 3rd Edition (Chapter 9 - Classes)
10-30-2026
"""

from tracker.models import StoryGame, LiveServiceGame

STORY_GAME_TITLES = ("Hades", "Stardew Valley", "Elden Ring",
                     "Monster Hunter", "Resident Evil", "Kingdom Hearts",
                     "Bloodborne", "Pokemon", "Persona", "Gex")
LIVE_SERVICE_GAME_TITLES = ("Deadlock", "Overwatch", "Tekken")


class GameLibrary:
    """A collection of games the user can log playtime for."""

    def __init__(self):
        """Initialize an empty library."""
        # Keys are lowercase titles so lookups ignore capitalization.
        self.games = {}

    def add_game(self, game):
        """
        Add a Game to the library.

        Raises ValueError if a game with the same title already exists.
        """
        key = game.title.lower()
        if key in self.games:
            raise ValueError(f"{game.title} is already in the library.")
        self.games[key] = game

    def get_game(self, title):
        """Return the game matching title (any case), or None if missing."""
        return self.games.get(title.strip().lower())

    def get_titles(self):
        """Return a list of every game title in the library."""
        return [game.title for game in self.games.values()]

    def get_total_hours(self):
        """Return the hours played across every game in the library."""
        return sum(game.get_total_hours() for game in self.games.values())

    def get_most_played(self):
        """Return the game with the most hours, or None if none are played."""
        played_games = [game for game in self.games.values()
                        if game.get_total_hours() > 0]
        if not played_games:
            return None
        return max(played_games, key=lambda game: game.get_total_hours())


def create_default_library():
    """Return a GameLibrary filled with the program's starting games."""
    library = GameLibrary()
    for title in STORY_GAME_TITLES:
        library.add_game(StoryGame(title))
    for title in LIVE_SERVICE_GAME_TITLES:
        library.add_game(LiveServiceGame(title))
    return library
