add = lambda a, b: a + b
print(add(1, 2))

multiply = lambda a, b: a * b
print(multiply(2, 3))

substract = lambda a, b: a - b
print(substract(5, 3))

divide = lambda a, b: a / b
print(divide(10, 2))


#Cuadrado de cada numero
numbers = range(1, 11)
squares = list(map(lambda x: x**2, numbers))
print(squares)
# lambda viene siendo como una funcion anonima

#Pages
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)

#Impares
odd_numbers = list(filter(lambda x: x%2 != 0, numbers))
print(odd_numbers)