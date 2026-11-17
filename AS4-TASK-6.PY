
import os

# Create input and output folders
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

departments = ["ECE", "CSE", "AIDS", "EEE", "MECH"]

# Create sample department files
sample_data = {
    "ECE.txt": [
        "101,Jaya,ECE,jaya@gmail.com,Dance;Singing",
        "102,Ravi,ECE,ravi@gmail.com,Singing;Drama"
    ],
    "CSE.txt": [
        "103,Kumar,CSE,kumar@gmail.com,Drama;Music",
        "101,Jaya,CSE,jaya@gmail.com,Dance"
    ],
    "AIDS.txt": [
        "104,Arun,AIDS,arunmail.com,Music",
        "105,Mani,AIDS,mani@gmail.com,Dance"
    ],
    "EEE.txt": [
        "106,Ram,EEE,ram@gmail.com"
    ]
}

for filename, records in sample_data.items():
    with open("input/" + filename, "w") as f:
        for record in records:
            f.write(record + "\n")


# Email validation
def valid_email(email):
    return (
        "@" in email
        and "." in email
        and email.index("@") < email.rindex(".")
        and not email.startswith("@")
        and not email.endswith(".")
    )


# Process registrations
def process_registration():

    seen = set()
    master = []
    events = {}
    errors = []

    for dept in departments:

        filename = "input/" + dept + ".txt"

        try:
            with open(filename, "r", encoding="utf-8") as file:

                for line_no, line in enumerate(file, 1):

                    try:
                        parts = line.strip().split(",", 4)

                        if len(parts) != 5:
                            raise ValueError("Damaged record")

                        reg, name, department, email, event_text = parts

                        if not all([reg, name, department, email, event_text]):
                            raise ValueError("Empty field")

                        if not valid_email(email):
                            raise ValueError("Invalid email")

                        if reg in seen:
                            raise ValueError("Duplicate registration")

                        chosen_events = event_text.split(";")

                        if any(not event.strip() for event in chosen_events):
                            raise ValueError("Invalid event")

                        seen.add(reg)
                        master.append(line.strip())

                        for event in chosen_events:
                            event = event.strip()
                            events.setdefault(event, []).append(
                                reg + "," + name + "," + department
                            )

                    except ValueError as e:
                        errors.append(
                            filename + " Line " +
                            str(line_no) + ": " + str(e)
                        )

        except FileNotFoundError:
            errors.append(filename + ": File not found")

        except PermissionError:
            errors.append(filename + ": Permission denied")

        except UnicodeDecodeError:
            errors.append(filename + ": Encoding error")

        except OSError as e:
            errors.append(filename + ": " + str(e))

    # Save master list
    with open("output/master.txt", "w") as f:
        for record in master:
            f.write(record + "\n")

    # Save event-wise files
    for event, participants in events.items():

        with open("output/" + event + ".txt", "w") as f:
            for participant in participants:
                f.write(participant + "\n")

    # Save summary report
    with open("output/summary.txt", "w") as f:
        f.write("COLLEGE FEST SUMMARY\n")
        f.write("Total Registrations: " + str(len(master)) + "\n")
        f.write("Total Events: " + str(len(events)) + "\n")

        for event, participants in events.items():
            f.write(event + ": " + str(len(participants)) + "\n")

    # Save error log
    with open("output/error.log", "w") as f:
        for error in errors:
            f.write(error + "\n")

    print("\nCOLLEGE FEST PROCESSING")
    print("Valid Registrations:", len(master))
    print("Total Events:", len(events))
    print("Rejected Records:", len(errors))
    print("All reports saved successfully!")


# Main program
process_registration()
