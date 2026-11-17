
# TASK 4: File and Exception Forensics

def save_returns(books):
    try:
        with open("returns.log", "a", encoding="utf-8") as log:
            for book in books:
                log.write(book + "\n")

    except OSError as e:
        with open("error.log", "a", encoding="utf-8") as error:
            error.write(str(e) + "\n")


def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as file:
            books = file.read().splitlines()

        save_returns(books)
        print(day_file, "processed successfully")

    except FileNotFoundError:
        print("Error: File not found:", day_file)

    except PermissionError:
        print("Error: Permission denied:", day_file)

    except OSError as e:
        print("File error:", e)


# Create three sample day files
for i in range(1, 4):
    with open("day" + str(i) + ".txt", "w") as f:
        f.write("Book returned on day " + str(i) + "\n")

# Process three days
for i in range(1, 4):
    process("day" + str(i) + ".txt")

# Display final log
print("\nFinal Returns Log:")
with open("returns.log", "r") as log:
    print(log.read())
