student1 = set(input().split())
student2 = set(input().split())

print("Student 1 Electives:", student1)
print("Student 2 Electives:", student2)

clash = student1.intersection(student2)

if clash:
    print("Clashing Electives:", clash)
else:
    print("No Clash")