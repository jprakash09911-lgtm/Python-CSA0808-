contacts1 = {"Arun": "9876543210", "Bala": "9876501234"}
contacts2 = {"Arun": "9876543210", "Cathy": "9876512345"}

contacts = contacts1.copy()
contacts.update(contacts2)

print("Merged Contacts:")
for name, number in contacts.items():
    print(name, ":", number)