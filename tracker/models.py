"""
Game Playtime Tracker
Joe Widdifield
Defines the Game class, which stores a game's title and the play
sessions (in hours) the user has logged for it.
Resources: Python Crash Course, 3rd Edition (Chapter 9 - Classes)
10-30-2026
"""


class Game:
    """A video game and the play sessions logged for it."""

    def __init__(self, title):
        """Initialize the game with a title and no logged sessions."""
        self.title = title
        self.sessions = []

    def add_session(self, hours):
        """
        Log a play session of the given number of hours.

        Raises ValueError if hours is not greater than zero.
        """
        if hours <= 0:
            raise ValueError("Hours played must be greater than zero.")
        self.sessions.append(hours)

    def get_total_hours(self):
        """Return the total hours played across all sessions."""
        return sum(self.sessions)

    def get_session_count(self):
        """Return how many sessions have been logged."""
        return len(self.sessions)

    def describe(self):
        """Return a short summary of the game's playtime."""
        return (f"{self.title}: {self.get_total_hours()} hours "
                f"over {self.get_session_count()} session(s)")
