numbers = [1, 2, 3, 4, 5, 6]

print("::".join(str(item) for item in numbers))

print("::".join(map(str, numbers)))