# Listas en python
print("Listas en python, son mutables, es decir, se pueden modificar")
print("Ejemplo: lista = [1, 2, 3, 4, 5]")
# Iterar datos
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print("Tipo de dato: ", type(matrix))

print("Para iterar una matriz se utiliza un bucle for anidado")

for row in matrix:
        for element in row:
            print(element)

print(matrix[0][0])
print(matrix[0][1])
print(matrix[2][2])

# Tuplas en python
print("Tuplas en python, son inmutables, es decir, no se pueden modificar")
print("Ejemplo: tupla = (1, 2, 3, 4, 5)")

tupla = (1, 2, 3, 4, 5)
print(tupla)
print("Tipo de dato: ", type(tupla))

print("Acceder a los elementos de una tupla se utiliza el índice del elemento deseado")
print(tupla[0])
print(tupla[1])
print(tupla[2])