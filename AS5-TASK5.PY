POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}

def score(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()

    total = 0

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
    "Roads are clean and the bus was fast.",
    "Smoke from the factory, air is bad.",
    "The staff were not helpful.",
    "Not bad, service improved."
]

for c in complaints:
    print(label(c), "|", c)


# Extractive Summariser
from collections import Counter

def summarise(text):
    sentences = text.split(".")

    words = text.lower().split()
    frequency = Counter(words)

    best = max(
        sentences,
        key=lambda s: sum(frequency[w.lower()] for w in s.split()),
        default=""
    )

    return best.strip()


text = "Air is dirty. Air pollution is bad. Roads are clean."

print("Summary:", summarise(text))