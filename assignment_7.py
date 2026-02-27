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
courses = []

print("Enter course data (format: code|title|days|time|room): write 'DONE' to finish: ")  # Prompt the user for input

while True:
    line = input()                                      # Read a line of input from the user
    if line.strip().upper() == "DONE":
        break                                           # Exit the loop if the user is done entering data
    
    fields = line.split("|")                            # Split the input line 
    if len(fields) != 5:
        continue                                        # Skip invalid input lines
    
# ============================================================


# ============================================================
# Step 2: Title and Room Formatting

code = fields[0].strip().upper()                                                                # Extract and clean course code
title = fields[1].strip().title()                                                               # Extract and clean course title
days_raw = fields[2].strip().upper()                                                            # Extract and clean day code
time_raw = fields[3].strip().lower().replace(" ", "")                                           # Extract
room = fields[4].strip().title()                                                                # Extract and clean room name

code = code.upper().replace(" ", "")                                                            # Ensure course code is uppercase and has no spaces
title = title.title()                                                                           # Ensure course title is in title case
room = room.title()                                                                             # Ensure room name is in title case

# ============================================================


# ============================================================
# Step 3: Day Code Expansion

day_input = {
    "M": "Monday",
    "T": "Tuesday",
    "W": "Wednesday",
    "R": "Thursday",
    "F": "Friday"
}

day_abbr = {
    "M": "Mon",
    "T": "Tue",
    "W": "Wed",
    "R": "Thu",
    "F": "Fri"
}

full_days_str = "/".join(full_day_list)                        # Create a list of full day names based on the day code
abbr_days_str = "/ ".join(abbr_day_list)                       # Create a list of abbreviated day names based on the day code

# ============================================================


# ============================================================
# Step 4: Time Standardization

time_clean = time_raw.replace("am", " AM").replace("pm", " PM").upper()  # Standardize time input to uppercase for AM/PM
room_name = fields[4].strip().title()                                    # Extract and clean room name

courses.append({
    "code": code,
    "title": title,
    "days": full_day_list,
    "days_str": full_days_str,
    "days_abbr": abbr_days_str,
    "time": time_clean,
    "room": room_name
})                                                                      # Append the processed course information to the course list

# ============================================================


# ============================================================
# Step 5: Conflict Detection

conflicts = []
for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]
        
        shared_days = [d for d in "mtwrf" if d in c1['days'] and d in c2['days']]  # Check for shared days

        if c1['time'] == c2['time'] and shared_days:  # Check for time conflict on shared days
            day_names = [day_input[d] for d in shared_days]  # Get full day names for the conflict
            days_out = ",".join(day_names)  
            conflicts.append(f"{c1['code']} and {c2['code']} conflict on {days_out} at {c1['time']}")  # Record the conflict

        if not conflicts:
            print("No conflicts detected.")  # Print if no conflicts are found
        else:
            for conflict in conflicts:
                print(conflict)  # Print each detected conflict

# ============================================================


# ============================================================
# Step 6: Full Output & Formatted Printing

print("\n=== AGGIE COURSE SCHEDULE ===")  # Header for the course schedule
for i, c in enumerate(course, 1):
    print(f"COURSE {i}:")
    print(f"  Code: {c['code']}")           # Print course code
    print(f"  Title: {c['title']}")         # Print course title
    print(f"  Days: {c['days_str']}")       # Print full day
    print(f"  Time: {c['time']}")           # Print time
    print(f"  Room: {c['room']}\n")         # Print room name

print("=== SCHEDULE SUMMARY ===")  # Header for the schedule summary
print(f"Total Courses: {len(courses)}\n")  # Print total number of courses

print("=== CONFLICTS REPORT ===")  # Header for conflicts

print("\n=== FORMATTED FOR PRINTING ===")  # Footer for the schedule
for c in courses:
    print(f"{c['code']:<12} {c['title']:<20} {c['days_abbr']:<25} at {c['time']:<10} in {c['room']}")  # Print formatted course information

# ============================================================
