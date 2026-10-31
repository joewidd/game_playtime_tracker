"""
Game Playtime Tracker
Joe Widdifield
Entry point for the program. Shows the main menu, runs the option the
user picks, and saves the library after every change. Replaces the
single-script game_playtime_tracker.py from Project 1.
Resources: Python Crash Course, 3rd Edition (Chapters 8-10)
10-31-2026
"""

from tracker.exceptions import CorruptSaveFileError
from tracker.library import create_default_library
from tracker.models import StoryGame, LiveServiceGame
from tracker.storage import load_library, save_library
from tracker.user_input import is_quit_command, prompt_for_game, prompt_for_hours


def start_library():
    """Load the saved library, starting fresh if the save file is corrupt."""
    try:
        return load_library()
    except CorruptSaveFileError as error:
        print(f"\nWarning: {error}")
        print("Starting with a fresh library. The old file will be replaced "
              "the next time you save.")
        return create_default_library()


def save_changes(library):
    """Save the library, reporting a problem instead of crashing."""
    try:
        save_library(library)
    except OSError as error:
        print(f"\nCould not save your playtime: {error}")


def log_session(library):
    """Ask for a game and hours played, then record the session."""
    game = prompt_for_game(library)
    if game is None:
        return
    hours = prompt_for_hours()
    if hours is None:
        return
    game.add_session(hours)
    save_changes(library)
    print(f"\nLogged {hours:g} hours. {game.describe()}")


def show_library(library):
    """Print every game's playtime and the library-wide totals."""
    print("\n--- Your Library ---")
    for game in library.games.values():
        print(game.describe())

    print(f"\nTotal hours played: {library.get_total_hours():g}")
    most_played = library.get_most_played()
    if most_played:
        print(f"Most played: {most_played.title}")


def complete_story_game(library):
    """Mark a story game as finished."""
    game = prompt_for_game(library)
    if game is None:
        return
    if not isinstance(game, StoryGame):
        print(f"\n{game.title} doesn't have an ending to complete.")
        return
    game.mark_completed()
    save_changes(library)
    print(f"\nCongrats on finishing {game.title}!")


def update_live_service_rank(library):
    """Change the player's rank in a live service game."""
    game = prompt_for_game(library)
    if game is None:
        return
    if not isinstance(game, LiveServiceGame):
        print(f"\n{game.title} doesn't have a rank to track.")
        return

    new_rank = input("\nEnter your new rank (Enter 'q' to go back): ").strip()
    if not new_rank or is_quit_command(new_rank):
        return
    game.update_rank(new_rank)
    save_changes(library)
    print(f"\n{game.describe()}")


# Each menu choice maps to a description and the function that handles it.
MENU_OPTIONS = {
    "1": ("Log a play session", log_session),
    "2": ("View your library", show_library),
    "3": ("Mark a story game as completed", complete_story_game),
    "4": ("Update a live service game rank", update_live_service_rank),
}


def show_menu():
    """Print the main menu and return the user's choice."""
    print("\n=== Game Playtime Tracker ===")
    for choice, (description, _) in MENU_OPTIONS.items():
        print(f"{choice}. {description}")
    print("q. Quit")
    return input("Choose an option: ").strip()


def main():
    """Run the main menu loop until the user quits."""
    library = start_library()

    while True:
        choice = show_menu()
        if is_quit_command(choice):
            break
        if choice not in MENU_OPTIONS:
            print("\nThat's not a menu option. Try again.")
            continue
        _, action = MENU_OPTIONS[choice]
        action(library)

    print("\nYour playtime is saved. See you next session!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExiting. Your playtime was saved after your last change.")
