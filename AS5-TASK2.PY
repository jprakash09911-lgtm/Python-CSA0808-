import statistics

data = [48, 95, 121, 60]

# Min-Max Normalisation
minimum = min(data)
maximum = max(data)

normalised = [(x - minimum) / (maximum - minimum) for x in data]

print("Min-Max:", [round(x, 3) for x in normalised])

# Z-Score Standardisation
mean = statistics.mean(data)
std = statistics.stdev(data)

z_score = [(x - mean) / std for x in data]

print("Z-Score:", [round(x, 3) for x in z_score])