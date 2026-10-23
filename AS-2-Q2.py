correct_otp = "1234"
attempts = 0

while attempts < 3:
    otp = input("Enter OTP: ")

    if otp.strip() == "":
        print("Blank entry. Try again.")
        continue

    attempts += 1

    if otp == correct_otp:
        print("Login successful")
        break
    else:
        print("Wrong OTP")

else:
    print("Account locked for 30 minutes")