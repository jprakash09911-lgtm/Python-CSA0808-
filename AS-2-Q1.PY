
units = int(input("Enter electricity units: "))
ration = input("Ration card (yes/no): ").lower()
elderly = input("Member above 80 years (yes/no): ").lower()

if units <= 100:
    print("Full subsidy")

elif 101 <= units <= 200:
    if ration == "yes":
        print("Partial subsidy")
    else:
        print("No subsidy")

elif units > 200 and elderly == "yes":
    print("Special subsidy")

else:
    print("No subsidy")