a = (10, 20, 30, 40)

print("Original tuple:", a)
print("First element:", a[0])
print("Last two elements:", a[-2:])

b = list(a)
b[0] = 100

c = tuple(b)

print("Modified tuple:",c)
print("Original tuple:", a)