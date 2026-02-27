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

def main():
    courses = []

day_map_full = {'m': 'Monday', 't': 'Tuesday', 'w': 'Wednesday', 'r': 'Thursday', 'f': 'Friday'}
day_map_short = {'m': 'Mon', 't': 'Tue', 'w': 'Wed', 'r': 'Thu', 'f': 'Fri'}

while True:
    user_input = input("Enter course data (format: code|title|days|time|room): write 'DONE' to finish: ")  # Read user input
    if user_input.strip().upper() == "DONE":  # Check for termination condition
        break

    fields = user_input.split("|")
    if len(fields) != 5:
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

full_days = [day_map_full[d] for d in raw_days if d in day_map_full]
short_days = [day_map_short[d] for d in raw_days if d in day_map_short]
        
display_days = "/".join(full_days)  # Create a string of full day names separated by slashes
display_days_string = display_days  # Store the full day names string for later use
print_days = "/".join(short_days)

# ============================================================


# ============================================================
# Step 4: Time Standardization

time_val = raw_time.replace(" ", "").replace("AM", " AM").replace("PM", " PM")
clean_time = time_val.strip()

courses.append({
            "code": clean_code,
            "title": clean_title,
            "days_list": full_days,
            "display_days": display_days,
            "print_days": print_days,
            "time": clean_time,
            "room": clean_room
        })

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
