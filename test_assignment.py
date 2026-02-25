"""
COMP 163 - Assignment 7: Course Schedule Formatter
Automated Test Cases

DO NOT MODIFY THIS FILE.
Run locally with: python -m pytest test_assignment.py -v
"""

import subprocess
import sys
import os

SCRIPT = os.path.join(os.path.dirname(__file__), "assignment_7.py")


def run_program(input_data):
    """Run the student's script with the given stdin input and return stdout."""
    result = subprocess.run(
        [sys.executable, SCRIPT],
        input=input_data,
        capture_output=True,
        text=True,
        timeout=10
    )
    return result.stdout


# ============================================================
# Step 1 — Course Code Formatting (8 pts, 4 pts each)
# ============================================================

def test_code_lowercase():
    """Lowercase code 'cs 163' must become 'CS 163'."""
    output = run_program("cs 163|intro to programming|mw|9:00am|ncat 101\nDONE\n")
    assert "Code:  CS 163" in output, (
        f"Input 'cs 163' should produce 'Code:  CS 163'.\n"
        f"Got:\n{output}"
    )

def test_code_mixedcase():
    """Mixed-case code 'Eng 101' must become 'ENG 101'."""
    output = run_program("Eng 101|english composition|mwf|2:00pm|gibbs 305\nDONE\n")
    assert "Code:  ENG 101" in output, (
        f"Input 'Eng 101' should produce 'Code:  ENG 101'.\n"
        f"Got:\n{output}"
    )


# ============================================================
# Step 2 — Title and Room Formatting (8 pts, 2 pts each)
# ============================================================

def test_title_lowercase():
    """Lowercase title must be converted to title case."""
    output = run_program("CS 163|intro to programming|mw|9:00am|ncat 101\nDONE\n")
    assert "Title: Intro To Programming" in output, (
        f"Lowercase title 'intro to programming' should become 'Intro To Programming'.\n"
        f"Got:\n{output}"
    )

def test_title_uppercase():
    """All-caps title must be converted to title case."""
    output = run_program("MATH 231|CALCULUS I|tr|11:00am|marteena hall 200\nDONE\n")
    assert "Title: Calculus I" in output, (
        f"All-caps title 'CALCULUS I' should become 'Calculus I'.\n"
        f"Got:\n{output}"
    )

def test_room_lowercase():
    """Lowercase room must be converted to title case."""
    output = run_program("CS 163|intro to programming|mw|9:00am|ncat 101\nDONE\n")
    assert "Room:  Ncat 101" in output, (
        f"Lowercase room 'ncat 101' should become 'Ncat 101'.\n"
        f"Got:\n{output}"
    )

def test_room_multiword():
    """Multi-word room name must be fully title cased."""
    output = run_program("MATH 231|calculus i|tr|11:00am|marteena hall 200\nDONE\n")
    assert "Room:  Marteena Hall 200" in output, (
        f"Room 'marteena hall 200' should become 'Marteena Hall 200'.\n"
        f"Got:\n{output}"
    )


# ============================================================
# Step 3 — Day Code Expansion (12 pts, 3 pts each)
# ============================================================

def test_days_mw():
    """'mw' must expand to 'Monday/Wednesday'."""
    output = run_program("CS 163|Test Course|mw|9:00am|Room 101\nDONE\n")
    assert "Days:  Monday/Wednesday" in output, (
        f"'mw' should expand to 'Monday/Wednesday'.\n"
        f"Got:\n{output}"
    )

def test_days_tr():
    """'TR' must expand to 'Tuesday/Thursday'."""
    output = run_program("CS 163|Test Course|TR|9:00am|Room 101\nDONE\n")
    assert "Days:  Tuesday/Thursday" in output, (
        f"'TR' should expand to 'Tuesday/Thursday'.\n"
        f"Got:\n{output}"
    )

def test_days_mwf():
    """'MWF' must expand to 'Monday/Wednesday/Friday'."""
    output = run_program("CS 163|Test Course|MWF|9:00am|Room 101\nDONE\n")
    assert "Days:  Monday/Wednesday/Friday" in output, (
        f"'MWF' should expand to 'Monday/Wednesday/Friday'.\n"
        f"Got:\n{output}"
    )

def test_days_single():
    """Single day 'm' must expand to 'Monday'."""
    output = run_program("CS 163|Test Course|m|9:00am|Room 101\nDONE\n")
    assert "Days:  Monday" in output, (
        f"Single day 'm' should expand to 'Monday'.\n"
        f"Got:\n{output}"
    )


# ============================================================
# Step 4 — Time Standardization (8 pts, 2 pts each)
# ============================================================

def test_time_lowercase_am():
    """'9:00am' must become '9:00 AM'."""
    output = run_program("CS 163|Test Course|mw|9:00am|Room 101\nDONE\n")
    assert "Time:  9:00 AM" in output, (
        f"'9:00am' should become '9:00 AM'.\n"
        f"Got:\n{output}"
    )

def test_time_uppercase_am():
    """'11:30AM' must become '11:30 AM'."""
    output = run_program("CS 163|Test Course|mw|11:30AM|Room 101\nDONE\n")
    assert "Time:  11:30 AM" in output, (
        f"'11:30AM' should become '11:30 AM'.\n"
        f"Got:\n{output}"
    )

def test_time_lowercase_pm():
    """'2:00pm' must become '2:00 PM'."""
    output = run_program("CS 163|Test Course|mw|2:00pm|Room 101\nDONE\n")
    assert "Time:  2:00 PM" in output, (
        f"'2:00pm' should become '2:00 PM'.\n"
        f"Got:\n{output}"
    )

def test_time_uppercase_pm():
    """'2:00PM' must become '2:00 PM'."""
    output = run_program("CS 163|Test Course|mw|2:00PM|Room 101\nDONE\n")
    assert "Time:  2:00 PM" in output, (
        f"'2:00PM' should become '2:00 PM'.\n"
        f"Got:\n{output}"
    )


# ============================================================
# Step 5 — Conflict Detection (16 pts, 4 pts each)
# ============================================================

def test_conflict_same_days_same_time():
    """Two courses sharing all days and same time must be flagged."""
    output = run_program(
        "CS 163|Intro to Programming|mw|9:00am|Ncat 101\n"
        "ENG 101|English Composition|mw|9:00am|Gibbs 305\n"
        "DONE\n"
    )
    assert "CS 163 and ENG 101 conflict on Monday, Wednesday at 9:00 AM" in output, (
        f"CS 163 and ENG 101 both meet MW at 9:00 AM — conflict expected.\n"
        f"Got:\n{output}"
    )

def test_conflict_same_days_different_time():
    """Same days but different times must produce no conflict."""
    output = run_program(
        "CS 163|Intro to Programming|mw|9:00am|Ncat 101\n"
        "ENG 101|English Composition|mw|11:00am|Gibbs 305\n"
        "DONE\n"
    )
    assert "No conflicts detected." in output, (
        f"Same days but different times should produce 'No conflicts detected.'.\n"
        f"Got:\n{output}"
    )

def test_conflict_different_days_same_time():
    """Different days must produce no conflict even if times match."""
    output = run_program(
        "CS 163|Intro to Programming|mw|9:00am|Ncat 101\n"
        "ENG 101|English Composition|tr|9:00am|Gibbs 305\n"
        "DONE\n"
    )
    assert "No conflicts detected." in output, (
        f"Different days should produce 'No conflicts detected.' even if times match.\n"
        f"Got:\n{output}"
    )

def test_conflict_partial_day_overlap():
    """Partial day overlap at same time must conflict on shared days only."""
    output = run_program(
        "CS 163|Intro to Programming|mwf|9:00am|Ncat 101\n"
        "ENG 101|English Composition|m|9:00am|Gibbs 305\n"
        "DONE\n"
    )
    assert "CS 163 and ENG 101 conflict on Monday at 9:00 AM" in output, (
        f"MWF and M at same time should conflict on Monday only.\n"
        f"Got:\n{output}"
    )


# ============================================================
# Step 6 — Formatted Printing Alignment (8 pts, 4 pts each)
# ============================================================

def test_formatted_single_course():
    """Formatted line must use exact column widths for a single course."""
    output = run_program(
        "cs 163|intro to programming|mw|9:00am|ncat 101\n"
        "DONE\n"
    )
    expected = f"{'CS 163':<10}{'Intro To Programming':<26}{'Mon/Wed':<13}{'9:00 AM':<11}{'Ncat 101'}"
    assert expected in output, (
        f"Formatted line does not match expected column widths.\n"
        f"Expected: '{expected}'\n"
        f"Got:\n{output}"
    )

def test_formatted_multiword_fields():
    """Formatted line must align correctly when title and room are multi-word."""
    output = run_program(
        "MATH 231|calculus i|tr|11:30AM|marteena hall 200\n"
        "DONE\n"
    )
    expected = f"{'MATH 231':<10}{'Calculus I':<26}{'Tue/Thu':<13}{'11:30 AM':<11}{'Marteena Hall 200'}"
    assert expected in output, (
        f"Formatted line does not match expected column widths.\n"
        f"Expected: '{expected}'\n"
        f"Got:\n{output}"
    )
