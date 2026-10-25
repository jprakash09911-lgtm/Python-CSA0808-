complaints = {
    "Water": 10,
    "Seeds": 15,
    "Fertilizer": 8,
    "Weather": 12
}

print("Farmer Complaints:", complaints)

total = sum(complaints.values())
print("Total Complaints:", total)

for key, value in complaints.items():
    print(key, ":", value)

highest = max(complaints, key=complaints.get)
print("Highest Complaints:", highest)