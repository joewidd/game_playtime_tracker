"""
Game Playtime Tracker
Joe Widdifield
Unit tests for building and exporting the text report in tracker/report.py.
Resources: Python Crash Course, 3rd Edition (Chapter 11 - Testing Your Code)
11-01-2026
"""

from datetime import date

import pytest

from tracker.library import create_default_library
from tracker.report import build_report, export_report

REPORT_DATE = date(2026, 11, 1)


@pytest.fixture
def played_library():
    """The default library with two games played and one completed."""
    library = create_default_library()
    library.get_game("Hades").add_session(2)
    library.get_game("Hades").mark_completed()
    library.get_game("Overwatch").add_session(5)
    return library


def test_report_header_includes_date(played_library):
    """The report starts with its title and the date it was generated."""
    lines = build_report(played_library, REPORT_DATE).splitlines()
    assert lines[0] == "GAME PLAYTIME REPORT"
    assert lines[1] == "Generated November 01, 2026"


def test_report_lists_most_played_first(played_library):
    """Games are listed from most to least hours played."""
    lines = build_report(played_library, REPORT_DATE).splitlines()
    assert lines[4].strip().startswith("Overwatch: 5 hours")
    assert lines[5].strip().startswith("Hades: 2 hours")


def test_report_summary(played_library):
    """The summary shows total hours, most played, and completions."""
    report = build_report(played_library, REPORT_DATE)
    assert "Total hours played: 7" in report
    assert "Most played: Overwatch" in report
    assert "Story games completed: 1 of 10" in report


def test_report_with_no_playtime():
    """A library with nothing played reports no most played game."""
    report = build_report(create_default_library(), REPORT_DATE)
    assert "Most played: None yet" in report
    assert "Total hours played: 0" in report


def test_export_report_writes_text_file(tmp_path, played_library):
    """Exporting writes the same text that build_report() returns."""
    report_path = tmp_path / "report.txt"
    returned_path = export_report(played_library, REPORT_DATE, report_path)
    assert returned_path == report_path
    assert report_path.read_text() == build_report(played_library,
                                                   REPORT_DATE)
