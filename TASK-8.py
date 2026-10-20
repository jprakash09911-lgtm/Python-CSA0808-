FAT_RATE = 5
SNF_RATE = 2
DAYS = 10

total_amount = 0

for day in range(1, DAYS + 1):
    print("Day", day)
    fat = float(input("Enter FAT: "))
    snf = float(input("Enter SNF: "))
    litres = float(input("Enter litres: "))

    rate = (fat * FAT_RATE) + (snf * SNF_RATE)
    amount = rate * litres
    total_amount += amount

    print("Daily amount:", amount)

print("Ten-day total payment:", total_amount)