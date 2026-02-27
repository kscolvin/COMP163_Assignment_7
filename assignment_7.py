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

from operator import index


courses = []

print("Enter course data (format: code|title|days|time|room): write 'DONE' to finish: ")  # Prompt the user for input

while True:
    user_input = input()  # Read user input
    
    if user_input.strip().upper() == "DONE":  # Check for termination condition
        break

    fields = user_input.split("|")
    if len(fields) != 5:
        print("Invalid input format. Please enter data in the format: code|title|days|time|room")
        continue  # Skip to the next iteration if the input format is incorrect

    code = fields[0].strip().upper()  # Extract and clean course code

    raw_code = fields[0].strip()  # Get the raw code for later use
    raw_title = fields[1].strip()  # Get the raw title for later use
    raw_days = fields[2].strip()  # Get the raw days for later use
    raw_time = fields[3].strip()  # Get the raw time for later use
    raw_room = fields[4].strip()  # Get the raw room for later use
    
    clean_code = raw_code.upper()  # Convert code to uppercase for standardization

# ============================================================


# ============================================================
# Step 2: Title and Room Formatting

clean_title = raw_title.title()  # Convert title to title case
clean_room = raw_room.title()  # Convert room to title case for standardization

# ============================================================


# ============================================================
# Step 3: Day Code Expansion

day_input = {
    "m": ("Monday", "Mon"),
    "t": ("Tuesday", "Tue"),
    "w": ("Wednesday", "Wed"),
    "r": ("Thursday", "Thu"),
    "f": ("Friday", "Fri")
}

full_days_list = []
short_days_list = []

for char in raw_days:
    if char in day_input:
        full_day, short_day = day_input[char]  # Get the full and short names for the day code
        full_days_list.append(full_day)  # Expand day codes to full names
        short_days_list.append(short_day)  # Get abbreviated day names

display_days_string = "/".join(full_days_list)  # Create a string of full day names separated by slashes
print_days = "/".join(short_days_list)  # Create a string of abbreviated day names separated by slashes

# ============================================================


# ============================================================
# Step 4: Time Standardization

time_temp = raw_time.lower().replace(" ", "")  # Convert time to lowercase for easier processing

if "am" in time_temp:
        period = "AM"
        time_digits = time_temp.replace("am", "").strip()  # Remove am and clean up
elif "pm" in time_temp:
        period = "PM"
        time_digits = time_temp.replace("pm", "").strip()  # Remove pm and clean
else:
    time_digits = time_temp

clean_time = f"{time_digits} {period}".strip()  # Format time in standard format


course_data = {
    "code": clean_code,
    "title": clean_title,
    "days_string": display_days_string,
    "days_full": full_days_list,
    "time": format_time,
    "room": clean_room
}
courses.append(course_data)  # Add the processed course data to the courses list

# ============================================================

# ============================================================
# Step 6: Full Output & Formatted Printing

print("\n=== AGGIE COURSE SCHEDULE ===\n")

for i, c in enumerate(courses, 1):
    print(f"\nCOURSE {i}:")
    print(f"Code:  {c['code']}")
    print(f"Title: {c['title']}")
    print(f"Days:  {c['days_string']}")
    print(f"Time:  {c['time']}")
    print(f"Room:  {c['room']}")

print("\n=== SCHEDULE SUMMARY ===")
print(f"Total courses: {len(courses)}")

# ============================================================

# ============================================================
# Step 5: Conflict Detection

print("\n=== CONFLICTS REPORT ===")
conflicts_found = False

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]
            
        shared_days = set(c1["days_full"]).intersection(c2["days_full"])  # Find shared days between courses

        if shared_days and c1["time"] == c2["time"]:
             conflicts_found = True
             order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
             sorted_shared_days = [d for d in order if d in shared_days] 
             days_str = ", ".join(sorted_shared_days)  # Create a string of shared days

             print(f"{c1['code']} and {c2['code']} conflict on {days_str} at {c1['time']}")  # Print conflict details
                
if not conflicts_found:
    print("No conflicts detected.")  # Print if no conflicts are found

# ============================================================

# ============================================================

# Step 6 Continued: Full Output & Formatted Printing

print("\n=== FORMATTED FOR PRINTING ===")
for c in courses:
     print(f"{c['code']:<10}{c['title']:<26} {c['days_string']:<13} {c['time']:<11} {c['room']}")

# ============================================================
