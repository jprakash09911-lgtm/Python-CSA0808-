import sqlite3

readings = [
    ("Adyar", "2026-10-01", 48.0),
    ("Guindy", "2026-10-01", 95.0),
    ("Guindy", "2026-10-03", 121.0),
    ("Adyar", "2026-10-04", 60.0)
]

con = sqlite3.connect("air_quality.db")

con.execute("""
CREATE TABLE IF NOT EXISTS aq (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")

con.execute("DELETE FROM aq")

con.executemany(
    "INSERT INTO aq VALUES (?, ?, ?)",
    readings
)

con.commit()

print("Database Records:")

for row in con.execute("SELECT * FROM aq"):
    print(row)

con.close()