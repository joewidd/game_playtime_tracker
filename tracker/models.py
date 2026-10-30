"""
Game Playtime Tracker
Joe Widdifield
Defines the Game class, which stores a game's title and the play
sessions (in hours) the user has logged for it, along with the
StoryGame and LiveServiceGame subclasses for games that do and do not
have an ending.
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


class StoryGame(Game):
    """A game with an ending that the player can complete."""

    def __init__(self, title):
        """Initialize the game as not yet completed."""
        super().__init__(title)
        self.completed = False

    def mark_completed(self):
        """Record that the player has finished the game."""
        self.completed = True

    def describe(self):
        """Return the playtime summary plus the completion status."""
        status = "Completed" if self.completed else "In progress"
        return f"{super().describe()} - {status}"


class LiveServiceGame(Game):
    """An ongoing multiplayer game with no ending, tracked by rank."""

    def __init__(self, title, rank="Unranked"):
        """Initialize the game with the player's current rank."""
        super().__init__(title)
        self.rank = rank

    def update_rank(self, new_rank):
        """Set the player's current rank."""
        self.rank = new_rank

    def describe(self):
        """Return the playtime summary plus the player's rank."""
        return f"{super().describe()} - Rank: {self.rank}"
