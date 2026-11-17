POSITIVE = {
    "good", "clean", "fast", "helpful", "improved"
}

NEGATIVE = {
    "bad", "dirty", "slow", "rude", "smoke", "broken"
}

NEGATORS = {"not", "never", "no"}


def score(text):

    words = text.lower().replace(".", " ").replace(",", " ").split()

    total = 0

    # TODO 1
    for i, word in enumerate(words):

        value = 0

        if word in POSITIVE:
            value = 1

        elif word in NEGATIVE:
            value = -1

        if i > 0 and words[i - 1] in NEGATORS:
            value = -value

        total += value

    return total


def label(text):

    s = score(text)

    if s > 0:
        return "positive"

    elif s < 0:
        return "negative"

    else:
        return "neutral"


complaints = [
    "The roads are clean and buses are fast.",
    "The air is bad and full of smoke.",
    "The service is helpful.",
    "The road is dirty.",
    "The transport system is improved.",
    "The factory smoke is bad.",
    "The staff are not helpful.",
    "The roads are clean.",
    "The buses are slow.",
    "The environment is good."
] * 5


# Sentiment Analysis
for complaint in complaints:
    print(label(complaint), "|", complaint)


# Agreement Calculation
actual = [
    "positive", "negative", "positive", "negative",
    "positive", "negative", "negative", "positive",
    "negative", "positive"
] * 5

predicted = [label(c) for c in complaints]

correct = 0

for i in range(len(actual)):
    if actual[i] == predicted[i]:
        correct += 1

accuracy = (correct / len(actual)) * 100

print("Total Complaints:", len(complaints))
print("Correct Labels:", correct)
print("Agreement:", accuracy, "%")


# Extractive Summariser
from collections import Counter

def summarise(text):

    sentences = text.split(".")

    words = text.lower().split()

    frequency = Counter(words)

    if not sentences:
        return ""

    return max(
        sentences,
        key=lambda s: sum(
            frequency[word.lower()]
            for word in s.split()
        )
    ).strip()


sample = """
Air pollution is increasing.
Air quality is bad.
People need clean air.
The city needs better transport.
"""

print("Summary:", summarise(sample))


# Database Index Performance
import sqlite3
import time

con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE aq (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")

data = [
    (f"Station{i % 120}", f"2026-10-{i % 28 + 1:02d}", float(i % 200))
    for i in range(100000)
]

con.executemany(
    "INSERT INTO aq VALUES (?, ?, ?)",
    data
)

con.commit()

query = """
SELECT AVG(pm25)
FROM aq
WHERE station = ? AND day = ?
"""

# Without Index
start = time.perf_counter()

con.execute(query, ("Station10", "2026-10-01")).fetchone()

without_index = time.perf_counter() - start

# Create Index
con.execute("""
CREATE INDEX idx_station_day
ON aq(station, day)
""")

# With Index
start = time.perf_counter()

con.execute(query, ("Station10", "2026-10-01")).fetchone()

with_index = time.perf_counter() - start

print("Without Index:", without_index)
print("With Index:", with_index)

con.close()