
# Corrected program to calculate average marks

def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

marks = list(map(int, input("Enter marks: ").split()))

# Validate marks
if all(0 <= mark <= 100 for mark in marks):
    average = calculate_average(marks)
    print("Average marks =", round(average, 2))
else:
    print("Invalid marks")
