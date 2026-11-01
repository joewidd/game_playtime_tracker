"""
Game Playtime Tracker
Joe Widdifield
Builds a plain-text summary of the user's playtime and writes it to a
.txt file that can be opened or shared outside the program.
Resources: Python Crash Course, 3rd Edition (Chapter 10 - Writing to a File)
11-01-2026
"""

from pathlib import Path

from tracker.models import StoryGame

DEFAULT_REPORT_PATH = Path("playtime_report.txt")


def build_report(library, report_date):
    """Return the playtime report for the library as a string."""
    games_by_hours = sorted(library.games.values(),
                            key=lambda game: game.get_total_hours(),
                            reverse=True)
    story_games = [game for game in library.games.values()
                   if isinstance(game, StoryGame)]
    completed_count = sum(1 for game in story_games if game.completed)
    most_played = library.get_most_played()

    lines = [
        "GAME PLAYTIME REPORT",
        f"Generated {report_date:%B %d, %Y}",
        "",
        "Games by hours played:",
    ]
    lines += [f"  {game.describe()}" for game in games_by_hours]
    lines += [
        "",
        f"Total hours played: {library.get_total_hours():g}",
        f"Most played: {most_played.title if most_played else 'None yet'}",
        f"Story games completed: {completed_count} of {len(story_games)}",
    ]
    return "\n".join(lines) + "\n"


def export_report(library, report_date, path=DEFAULT_REPORT_PATH):
    """Write the playtime report to a text file and return its path."""
    path.write_text(build_report(library, report_date))
    return path
