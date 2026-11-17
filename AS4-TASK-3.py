
try:
    # Get file name
    filename = input("Enter file name: ")

    # Open and read the file
    file = open(filename, "r")

    data = file.read()

    print("\nFile Content:")
    print(data)

    file.close()

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")

except Exception as e:
    print("Error occurred:", e)

finally:
    print("File processing completed.")
