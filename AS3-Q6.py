trains = {
    "Chennai Express": ["Chennai", "10:00 AM"],
    "Pandian Express": ["Madurai", "11:30 AM"],
    "Kovai Express": ["Coimbatore", "01:00 PM"]
}

for train, details in trains.items():
    print("Train:", train)
    print("Destination:", details[0])
    print("Departure:", details[1])