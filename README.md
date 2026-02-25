[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2WukAeYI)
# COMP 163 — Assignment 7: Course Schedule Formatter

## Overview

Write a Python program that reads raw course registration data entered by the user,
cleans every field using string methods, detects scheduling conflicts, and outputs
a professional course schedule.

Input is entered one course at a time in the format:

```
code|title|days|time|room
```

The program continues reading until the user types `DONE`.

---

## Getting Started

Your solution goes in `assignment_7.py`. The section comments are already there
to guide your development order. Do not modify `test_assignment.py`.

Run the tests locally at any time with:

```bash
python -m pytest test_assignment.py -v
```

A green checkmark in the GitHub Actions tab means that test is passing for grading.

---

## Day Code Reference

| Code | Full Name | Short Name |
|------|-----------|------------|
| M    | Monday    | Mon        |
| T    | Tuesday   | Tue        |
| W    | Wednesday | Wed        |
| R    | Thursday  | Thu        |
| F    | Friday    | Fri        |

Full names are used in the COURSE blocks. Short names are used in the FORMATTED FOR PRINTING section.

---

## Required Output Sections

Your program must produce four sections in this order:

```
=== AGGIE COURSE SCHEDULE ===

COURSE 1:
  Code:  CS 163
  Title: Intro To Programming
  Days:  Monday/Wednesday
  Time:  9:00 AM
  Room:  Ncat 101

=== SCHEDULE SUMMARY ===
Total courses: 1

=== CONFLICT REPORT ===
No conflicts detected.

=== FORMATTED FOR PRINTING ===
CS 163    Intro To Programming      Mon/Wed      9:00 AM    Ncat 101
```

---

## Formatted Printing Column Widths

The FORMATTED FOR PRINTING section must use these exact left-aligned column widths:

| Column     | Width |
|------------|-------|
| Code       | 10    |
| Title      | 26    |
| Short days | 13    |
| Time       | 11    |
| Room       | none  |

---

## Conflict Detection Format

When two courses share at least one day **and** the same time:

```
CS 163 and ENG 101 conflict on Monday, Wednesday at 9:00 AM
```

When courses share a day but not a time, or share a time but not a day, no conflict is reported.
If no conflicts exist across all courses:

```
No conflicts detected.
```

---

## Required Git Commits

Make these commits in order as you complete each step:

1. `"Step 1: Input parsing and course code formatting"`
2. `"Step 2: Title and room formatting"`
3. `"Step 3: Day code expansion"`
4. `"Step 4: Time standardization"`
5. `"Step 5: Conflict detection"`
6. `"Step 6: Complete output and formatted printing"`

---

## README Reflection Questions

Answer all four questions below. Write your answers directly in this file
beneath each question. Answers should be written in complete sentences.
Incomplete or vague answers will not receive full credit.

---

**Question 1**

The days field requires you to process the string one character at a time rather
than treating it as a whole. Why is that necessary? Could you have produced the
same result with a single string method call instead of a loop? Explain your reasoning.

*Your answer here.*

---

**Question 2**

The time field contains two distinct parts that need to be handled differently.
How did you identify where one part ends and the other begins in your program?
What would break in your solution if the input format changed — for example,
if times were given as `9am` instead of `9:00am`?

*Your answer here.*

---

**Question 3**

Conflict detection requires you to compare courses against each other after
all input has been collected. Why can't you check for conflicts as each course
is entered, before the user types DONE? What data structure did you use to store
the courses, and why was that a good choice for this comparison?

*Your answer here.*

---

**Question 4**

What is the difference between *cleaning* data and *formatting* data?
Give one specific example of each from your own program and explain
why the distinction matters.

*Your answer here.*

---

## AI Usage

Describe any AI assistance you used, or write "None."
