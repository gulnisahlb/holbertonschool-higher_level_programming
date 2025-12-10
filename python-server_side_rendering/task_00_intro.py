# task_00_intro.py

import os

def generate_invitations(template, attendees):
    # --- 1. Input type check ---
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # --- 2. Empty input check ---
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # --- 3. Process each attendee ---
    for index, attendee in enumerate(attendees, start=1):
        # Prepare a copy of template for each attendee
        invitation = template
        
        # Replace placeholders, if missing replace with "N/A"
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))
        
        # --- 4. Generate output file ---
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
