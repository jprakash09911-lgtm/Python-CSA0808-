def calculate_fat_steps(fat):
    return fat / 0.1

def calculate_snf_steps(snf):
    return snf / 0.1

def calculate_rate(fat, snf):
    return (fat * 5) + (snf * 2)

def calculate_amount(rate, litres):
    return rate * litres

fat = float(input("Enter FAT value: "))
snf = float(input("Enter SNF value: "))
litres = float(input("Enter milk quantity: "))

fat_steps = calculate_fat_steps(fat)
snf_steps = calculate_snf_steps(snf)
rate = calculate_rate(fat, snf)
amount = calculate_amount(rate, litres)

print("FAT steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", rate)
print("Total amount:", amount)