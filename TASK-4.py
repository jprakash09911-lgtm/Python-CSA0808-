FAT_STEP = 0.1
SNF_STEP = 0.1

fat = float(input("Enter FAT value: "))
snf = float(input("Enter SNF value: "))
litres = float(input("Enter litres: "))

fat_steps = fat / FAT_STEP
snf_steps = snf / SNF_STEP

rate = (fat * 5) + (snf * 2)
amount = rate * litres

print("FAT steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", rate)
print("Total amount:", amount)