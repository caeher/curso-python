numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []

for number in numbers:
    square = number ** 2
    squares.append(square)

print(squares)

# Usando list comprehension
numbers = range(1, 11)

squares = [number ** 2 for number in numbers]
print(squares)