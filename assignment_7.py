"""
COMP 163 - Introduction to Programming
Assignment: Chapter 7 - Course Schedule Formatter
Name: Kennedi Colvin
GitHub Username: Kscolvin
Date: 02/26/2026
Description: This program takes a list of course schedules in a specific format and processes them to produce a more readable and standardized output.
AI Usage: I used AI to assist with breaking down the problem into manageable steps and providing guidance on how to implement each step. 
"""

# --- Setup ---
courses = []
day_map_full = {'m': 'Monday', 't': 'Tuesday', 'w': 'Wednesday', 'r': 'Thursday', 'f': 'Friday'}
day_map_short = {'m': 'Mon', 't': 'Tue', 'w': 'Wed', 'r': 'Thu', 'f': 'Fri'}

# ============================================================
# Step 1: Input Parsing & Course Code Formatting

while True:
    user_input = input("Enter course data (format: code|title|days|time|room): ")
    
    if user_input.strip().upper() == "DONE":
        break

    fields = user_input.split("|")
    if len(fields) != 5:
        continue 

    # Extract and clean fields using required string methods
    raw_code = fields[0].strip() 
    raw_title = fields[1].strip()
    raw_days = fields[2].strip().lower() # Normalize to lowercase for mapping
    raw_time = fields[3].strip()
    raw_room = fields[4].strip()
    
    # Standardize course code to uppercase
    clean_code = raw_code.upper()

    # ============================================================
    # Step 2: Title and Room Formatting
    
    clean_title = raw_title.title() # Clean to title case
    clean_room = raw_room.title()   # Clean to title case

    # ============================================================
    # Step 3: Day Code Expansion
    
    full_days = [day_map_full[d] for d in raw_days if d in day_map_full]
    short_days = [day_map_short[d] for d in raw_days if d in day_map_short]
        
    display_days_string = "/".join(full_days) 
    print_days = "/".join(short_days)         # Abbreviated version for print section

    # ============================================================
    # Step 4: Time Standardization
    
    # Normalize '9:00am' to '9:00 AM'
    time_temp = raw_time.upper().replace(" ", "")
    clean_time = time_temp.replace("AM", " AM").replace("PM", " PM").strip()

    courses.append({
        "code": clean_code,
        "title": clean_title,
        "days_full": full_days,
        "display_days": display_days_string,
        "print_days": print_days,
        "time": clean_time,
        "room": clean_room
    })

# ============================================================
# Step 6: Full Output (Aggie Course Schedule)

print("\n=== AGGIE COURSE SCHEDULE ===")

for i, c in enumerate(courses, 1):
    print(f"\nCOURSE {i}:")
    print(f"  Code:  {c['code']}")
    print(f"  Title: {c['title']}")
    print(f"  Days:  {c['display_days']}")
    print(f"  Time:  {c['time']}")
    print(f"  Room:  {c['room']}")

print("\n=== SCHEDULE SUMMARY ===")
print(f"Total courses: {len(courses)}")

# ============================================================
# Step 5: Conflict Detection

print("\n=== CONFLICT REPORT ===")
conflicts_found = False

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]
            
        # Check if they share at least one day AND the same time
        shared_days = set(c1["days_full"]).intersection(set(c2["days_full"]))

        if shared_days and c1["time"] == c2["time"]:
            conflicts_found = True
            # Sort shared days in M/T/W/R/F order using full names
            order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            sorted_shared_days = [d for d in order if d in shared_days] 
            days_str = ", ".join(sorted_shared_days)

            print(f'"{c1["code"]} and {c2["code"]} conflict on {days_str} at {c1["time"]}"')

if not conflicts_found:
    print("No conflicts detected.")   

# ============================================================
# Step 6 Continued: Formatted For Printing

print("\n=== FORMATTED FOR PRINTING ===")
for c in courses:
    print(f"{c['code']:<10}{c['title']:<26}{c['print_days']:<13}{c['time']:<11}{c['room']}")     

# ============================================================