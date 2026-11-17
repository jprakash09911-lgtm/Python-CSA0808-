
# File Processing Program

# Create and write a file
file = open("student.txt", "w")
file.write("Name: Jaya\n")
file.write("Department: ECE\n")
file.write("Subject: Python Programming\n")
file.close()

# Read the file
file = open("student.txt", "r")
print("File Contents:")
print(file.read())
file.close()

# Add new information
file = open("student.txt", "a")
file.write("Status: Completed\n")
file.close()

print("File updated successfully!")
