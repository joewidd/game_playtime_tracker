"""
Game Playtime Tracker
Joe Widdifield
Custom exceptions raised by the tracker so the menu can catch the
program's own errors separately from unexpected Python errors.
Resources: Python Crash Course, 3rd Edition (Chapter 10 - Exceptions)
10-30-2026
"""


class TrackerError(Exception):
    """Base class for every error raised by the playtime tracker."""


class InvalidHoursError(TrackerError):
    """Raised when hours played is not a positive number."""


class GameNotFoundError(TrackerError):
    """Raised when a title does not match any game in the library."""


class DuplicateGameError(TrackerError):
    """Raised when adding a game whose title is already in the library."""
