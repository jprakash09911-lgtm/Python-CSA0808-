
# From Requirement to File-Processing Design

# Step 1: Get user requirements
name = input("Enter student name: ")
reg_no = input("Enter register number: ")
department = input("Enter department: ")

# Step 2: Store data in a file
with open("student.txt", "w") as file:
    file.write("Student Details\n")
    file.write("Name: " + name + "\n")
    file.write("Register Number: " + reg_no + "\n")
    file.write("Department: " + department + "\n")

# Step 3: Read the file
with open("student.txt", "r") as file:
    data = file.read()

# Step 4: Display the result
print("\n--- FILE CONTENTS ---")
print(data)

print("File processing completed successfully!")
