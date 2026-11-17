# Air Quality Analysis and Visualisation

# Sample Data
adyar = [48, 55, 60, 75, 90]
guindy = [95, 100, 110, 105, 121]

dates = ["Oct 1", "Oct 2", "Oct 3", "Oct 4", "Oct 5"]

temperature = [28, 29, 30, 32, 34]

# 1. PM2.5 Monthly Trend
print("MONTHLY PM2.5 TREND")

for i in range(len(dates)):
    print(dates[i], "Adyar:", adyar[i],
          "Guindy:", guindy[i])


# 2. Station Comparison
print("\nSTATION COMPARISON")

avg_adyar = sum(adyar) / len(adyar)
avg_guindy = sum(guindy) / len(guindy)

print("Adyar Average:", avg_adyar)
print("Guindy Average:", avg_guindy)


# 3. Temperature vs PM2.5
print("\nTEMPERATURE VS PM2.5")

for i in range(len(temperature)):
    print("Temperature:", temperature[i],
          "PM2.5:", adyar[i])


# 4. Worst Air Quality
print("\nWORST AIR QUALITY")

all_values = adyar + guindy

print("Highest PM2.5:", max(all_values))
print("Lowest PM2.5:", min(all_values))

for i in range(len(all_values)):
    if all_values[i] > 100:
        print("High Pollution Reading:", all_values[i])


# 5. Daily Summary Table
print("\nDAILY SUMMARY")

for station, values in [
    ("Adyar", adyar),
    ("Guindy", guindy)
]:
    print("\nStation:", station)
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Mean:", round(sum(values) / len(values), 2))
    print("Valid Readings:", len(values))