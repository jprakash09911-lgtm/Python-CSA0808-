import csv
import sqlite3

# Sample Data
data = [
    ["Adyar", "2026-10-01", 48],
    ["Adyar", "2026-10-01", 52],
    ["Guindy", "2026-10-01", 95],
    ["Guindy", "2026-10-01", 105],
    ["Adyar", "2026-10-02", 60],
    ["Guindy", "2026-10-02", 110]
]


# Method 1: Python Loop
def python_average():
    total = {}
    count = {}

    for station, day, pm25 in data:
        key = (station, day)

        if key not in total:
            total[key] = 0
            count[key] = 0

        total[key] += pm25
        count[key] += 1

    result = {}

    for key in total:
        result[key] = total[key] / count[key]

    return result


# Method 2: CSV Module
def csv_average():
    result = {}

    for row in data:
        station = row[0]
        day = row[1]
        pm25 = row[2]

        key = (station, day)

        if key not in result:
            result[key] = []

        result[key].append(pm25)

    for key in result:
        result[key] = sum(result[key]) / len(result[key])

    return result


# Method 3: SQL
def sql_average():
    con = sqlite3.connect(":memory:")

    con.execute("""
        CREATE TABLE readings(
            station TEXT,
            day TEXT,
            pm25 REAL
        )
    """)

    con.executemany(
        "INSERT INTO readings VALUES (?, ?, ?)",
        data
    )

    result = con.execute("""
        SELECT station, day, AVG(pm25)
        FROM readings
        GROUP BY station, day
    """).fetchall()

    con.close()

    return result


# Display Results
print("PYTHON LOOP RESULT")
print(python_average())

print("\nCSV RESULT")
print(csv_average())

print("\nSQL RESULT")
print(sql_average())


# Find Highest Average
averages = python_average()

highest = max(averages, key=averages.get)

print("\nHIGHEST AIR POLLUTION")
print("Station:", highest[0])
print("Date:", highest[1])
print("Average PM2.5:", averages[highest])


# Daily Summary
print("\nDAILY SUMMARY")

for key, value in averages.items():
    print("Station:", key[0])
    print("Date:", key[1])
    print("Average:", round(value, 2))