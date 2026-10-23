def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    if len(reg) != 9 and len(reg) != 10:
        return False

    if not reg[:2].isalpha():
        return False
    if not reg[2:4].isdigit():
        return False
    if not reg[4:-4].isalpha():
        return False
    if not reg[-4:].isdigit():
        return False

    return True


num = input("Enter vehicle number: ")
num = normalise(num)

print("Normalised:", num)

if is_valid(num):
    print("Valid")
    print("Receipt:", num[:2], num[2:4], num[4:-4], num[-4:])
else:
    print("Invalid")