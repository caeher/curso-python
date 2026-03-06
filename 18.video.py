# Comprehension de listas
square = [x**2 for x in range(1,11)]
#print("Cuadrados: ", squares)

celcius = [0, 10, 20, 30, 40, 50]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
#print("Fahrenheit: ", fahrenheit)

#Numeros pares
evens = [x for x in range(1, 21) if x%2 == 0]
print("Numeros pares: ", evens)
#Numeros impares
odds = [x for x in range(1, 21) if x%2 != 0]
print("Numeros impares: ", odds)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Matriz transpuesta: ", transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print("Matriz transpuesta: ", transposed)