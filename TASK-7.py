import ratecard

fat = float(input("Enter FAT: "))
snf = float(input("Enter SNF: "))
litres = float(input("Enter litres: "))

print("FAT steps:", ratecard.fat_steps(fat))
print("SNF steps:", ratecard.snf_steps(snf))

r = ratecard.rate(fat, snf)
print("Rate per litre:", r)
print("Total amount:", ratecard.amount(r, litres))