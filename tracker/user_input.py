"""
Game Playtime Tracker
Joe Widdifield
Functions for reading and validating what the user types. Parsing is kept
separate from prompting so the validation logic can be unit tested
without simulating keyboard input.
Resources: Python Crash Course, 3rd Edition (Chapters 7, 8, and 10)
10-31-2026
"""

from tracker.exceptions import GameNotFoundError, InvalidHoursError

QUIT_COMMANDS = ("quit", "q")


def is_quit_command(text):
    """Return True if the user typed a command to go back or quit."""
    return text.strip().lower() in QUIT_COMMANDS


def parse_hours(text):
    """
    Convert the user's text to a positive number of hours.

    Raises InvalidHoursError if the text is not a number greater than zero.
    """
    try:
        hours = float(text)
    except ValueError:
        raise InvalidHoursError(f"'{text}' is not a valid number.") from None
    if hours <= 0:
        raise InvalidHoursError("Hours played must be greater than zero.")
    return hours


def prompt_for_game(library):
    """
    Ask the user to pick a game until they enter a valid title.

    Returns the matching Game, or None if the user quits.
    """
    prompt = "\nChoose a game from your library:"
    prompt += f"\n{', '.join(library.get_titles())}"
    prompt += "\n(Enter 'q' to go back): "

    while True:
        title = input(prompt)
        if is_quit_command(title):
            return None
        try:
            return library.get_game(title)
        except GameNotFoundError as error:
            print(f"\n{error} Try again.")


def prompt_for_hours():
    """
    Ask the user how many hours they played until they enter a valid number.

    Returns the hours as a float, or None if the user quits.
    """
    prompt = "\nHow many hours did you play? (Enter 'q' to go back): "

    while True:
        text = input(prompt)
        if is_quit_command(text):
            return None
        try:
            return parse_hours(text)
        except InvalidHoursError as error:
            print(f"\n{error} Try again.")
