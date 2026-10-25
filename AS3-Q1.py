rainfall = list(map(int, input().split()))

print("Rainfall:", rainfall)
print("First 3 days:", rainfall[:3])
print("Last 3 days:", rainfall[-3:])
print("Total rainfall:", sum(rainfall))