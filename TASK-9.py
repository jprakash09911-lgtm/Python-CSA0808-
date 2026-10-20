FAT_RATE = 5
SNF_RATE = 2
DAYS = 10

total_payment = 0

for day in range(1, DAYS + 1):
    print("\nDay", day)

    fat = float(input("Enter FAT: "))
    snf = float(input("Enter SNF: "))
    litres = float(input("Enter litres: "))

    fat_steps = fat / 0.1
    snf_steps = snf / 0.1

    rate = (fat * FAT_RATE) + (snf * SNF_RATE)
    amount = rate * litres

    total_payment += amount

    print("FAT steps:", fat_steps)
    print("SNF steps:", snf_steps)
    print("Rate per litre:", rate)
    print("Daily amount:", amount)

print("\nTen-day total payment:", total_payment)