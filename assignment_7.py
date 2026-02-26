"""
COMP 163 - Introduction to Programming
Assignment: Chapter 7 - Course Schedule Formatter
Name: Kennedi Colvin
GitHub Username: Kscolvin
Date: 02/26/2026
Description: This program takes a list of course schedules in a specific format and processes them to produce a more readable and standardized output.
AI Usage: I used AI to assist with breaking down the problem into manageable steps and providing guidance on how to implement each step. 
"""

# ============================================================
# Step 1: Input Parsing & Course Code Formatting

# --- Setup ---

day_setup = {"M": "Monday", "T": "Tuesday", "W": "Wednesday", "R": "Thursday", "F": "Friday"} # Dictionary to map day codes to full names
day_abbr = {"M": "Mon", "T": "Tue", "W": "Wed", "R": "Thu", "F": "Fri"} # Dictionary to map day codes to abbreviations

# --- Data Collection ---

courses = []

while True:
    line = input("Enter course data (format: code|title|days|time|room): write 'DONE' to finish: ").strip()  # Read input line and remove leading/trailing whitespace
    if line.strip().upper() == "DONE":
        break  # Exit the loop if the user is done entering data
    
    fields = line.split("|")                                                                        # Split the input line 
    if len(fields) != 5:
        continue                                                                                    # Skip invalid input lines

# --- Data Extraction & Cleaning ---

    raw_input = fields[0].strip().upper()                                                           # Extract and clean course code
    course_code = "".join(raw_input.split())                                                        # Remove any whitespace from the course code
    course_title = fields[1].strip().title()                                                        # Extract and clean course title

    day_code = fields[2].strip().upper()                                                            # Extract and clean day code
    time_input = fields[3].strip().upper().lower().replace("am", "AM").replace("pm", "PM")          # Extract and clean time input, standardize to uppercase for AM/PM
    room_name = {fields[4].strip().title()}                                                         # Extract and clean room name

    full_day_list = [day_setup[char] for char in day_code if char in day_setup]                     # Create a list of full day names based on the day code
    abbr_day_list = [day_abbr[char] for char in day_code if char in day_abbr]                       # Create a list of abbreviated day names based on the day code

    joined_full_days = "/ ".join(full_day_list)                                                     # Join the full day names with a separator
    joined_abbr_days = "/ ".join(abbr_day_list)                                                     # Join the abbreviated day names with a separator

    courses.append({"code": course_code, "title": course_title, "days": full_day_list, "days_str": joined_full_days, "days_abbr": joined_abbr_days, "time": time_input, "room": fields[4].strip().title()})    # Store the processed course information in a list


# --- Conflict Detection ---

    conflict = []                                                                                   # List to keep track of any scheduling conflicts

    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            c1 = courses[i]
            c2 = courses[j]

            shared_days = [d for d in c1['days'] if d in c2['days']]                                            # Check for shared days
            if shared_days and c1['time'] == c2['time']:  
                conflict.append(f"{c1['code']} and {c2['code']} conflict on {shared_days[0]} at {c1['time']}")  # Record the conflict

# --- Output ---

print("\n=== AGGIE COURSE SCHEDULE ===")  # Header for the course schedule
for i, c in enumerate(courses, 1):
    print(f"COURSE {i}:")
    print(f"  Code: {c['code']}")  # Print course code
    print(f"  Title: {c['title']}")  # Print course title
    print(f"  Days: {c['days_str']}")  # Print full day
    print(f"  Time: {c['time']}")  # Print time
    print(f"  Room: {c['room']}\n")  # Print room name

print("\n=== SCHEDULE SUMMARY ===")  # Header for the schedule summary
print(f"Total Courses: {len(courses)}\n")  # Print total number of courses

print("=== CONFLICTS REPORT ===")  # Header for conflicts
conflicts_found = False
for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]

        shared = [d for d in c1['days'] if d in c2['days']]  # Check for shared days
        if shared and c1['time'] == c2['time']:
            conflicts_found = True
            day_string = "/ ".join(shared)  # Join shared days into a string
            print(f"{c1['code']} and {c2['code']} conflict on {day_string} at {c1['time']}")  # Print the conflict
        if not conflicts_found:
            print("No conflicts detected.")  # Print if no conflicts are found

print("\n=== FORMATTED FOR PRINTING ===")  # Footer for the schedule
for c in courses:
    print(f"{c['code']:<10} {c['title']:<25} {c['days_abbr']:<20} at {c['time']:<10} in {c['room']}")  # Print formatted course information

# ============================================================


# ============================================================
# Step 2: Title and Room Formatting
# ============================================================


# ============================================================
# Step 3: Day Code Expansion
# ============================================================


# ============================================================
# Step 4: Time Standardization
# ============================================================


# ============================================================
# Step 5: Conflict Detection
# ============================================================


# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
