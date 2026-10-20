FAT_RATE = 5
SNF_RATE = 2
DAYS = 10

def calculate_payment(fat, snf, litres):
    rate = (fat * FAT_RATE) + (snf * SNF_RATE)
    return rate, rate * litres

total = 0

for day in range(1, DAYS + 1):
    print("\nDay", day)

    fat = float(input("Enter FAT: "))
    snf = float(input("Enter SNF: "))
    litres = float(input("Enter litres: "))

    if fat < 0 or snf < 0 or litres < 0:
        print("Invalid input")
        break

    rate, amount = calculate_payment(fat, snf, litres)
    total += amount

    print("Rate per litre:", rate)
    print("Daily payment:", amount)

else:
    print("\nTen-day total payment:", total)