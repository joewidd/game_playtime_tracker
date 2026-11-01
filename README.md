[Video Presentation (YouTube)](PASTE_YOUTUBE_LINK_HERE)

[Slide Deck](PASTE_SLIDE_DECK_LINK_HERE)

# game_playtime_tracker

A command-line program for logging how many hours you play your games.
Playtime is saved between runs, story games can be marked as completed,
live service games track your rank, and you can export a text report of
your stats.

Originally built for Project 1 as a single script. It was refactored for
Project 2 into a package with classes, JSON storage, error handling, and
automated tests (all Project 2 commits start with `p2:`).

## Features

- Log play sessions for 13 games, with input checking for game titles and hours
- View your library with total hours and your most played game
- Mark story games (Hades, Elden Ring, Persona, ...) as completed
- Update your rank in live service games (Deadlock, Overwatch, Tekken)
- Export a playtime report to `playtime_report.txt`
- Progress is saved automatically to `playtime_data.json` after every change

## Setup

Requires Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Program

```bash
python main.py
```

## Running the Tests

```bash
pytest -v
```

## Project Structure

```
main.py                 Menu loop and program entry point
tracker/
    models.py           Game, StoryGame, and LiveServiceGame classes
    library.py          GameLibrary class and the starting game list
    user_input.py       Prompting for and validating user input
    storage.py          Saving and loading the library as JSON
    report.py           Building and exporting the text report
    exceptions.py       Custom exceptions for the tracker
tests/
    test_models.py      Tests for the game classes
    test_library.py     Tests for GameLibrary
    test_user_input.py  Tests for input parsing
    test_storage.py     Tests for saving and loading
    test_report.py      Tests for the text report
```

## Design Decisions

- **Inheritance for game types:** `StoryGame` and `LiveServiceGame` inherit
  session tracking from `Game` and each add only what that kind of game
  needs: a completion status, or a rank.
- **Composition for the library:** `GameLibrary` holds `Game` objects
  instead of inheriting from `Game`, because a library *has* games but is
  not itself a game.
- **Custom exceptions:** every tracker error inherits from `TrackerError`,
  so the menu can show a friendly message for expected problems while real
  bugs still surface.
- **Logic separate from input and output:** functions such as
  `parse_hours()` and `build_report()` return values instead of printing,
  which lets them be unit tested without typing into the program.

## Resources

- *Python Crash Course, 3rd Edition* by Eric Matthes (Chapters 8-11)
