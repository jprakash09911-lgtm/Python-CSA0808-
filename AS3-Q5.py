readings = list(map(int, input().split()))

cleaned = [x for x in readings if x >= 0]

print("Cleaned Readings:", cleaned)