# Ejemplos de iterador

#Crear una lista
my_list = [1, 2, 3, 4, 5]

#Obtener el iterador
my_iter = iter(my_list)

#User el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


#Iterar en cadenas
text = "Hello, World!" # cadena de texto
iter_text = iter(text) # obtener el iterador

#Iterar en la cadena
for char in iter_text:
    print(char)


# Crear un iterador para los numeros impares

#limite
limit = 10

# Crear el iterador
odd_itter = iter(range(1, limit + 1, 2))

# usar el iterador
for num in odd_itter:
    print(num)


def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


# Fibonacci
def fibonacci(limit):
    a, b = 0, 1 # asignacion de variables en una sola linea
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)


# Generador para ver numeros pares
limit = 10
odd_itter = iter(range(0, limit + 1, 2))

# usar el iterador
for num in odd_itter:
    print(num)

# Generador para ver numeros impares
limit = 10
odd_itter = iter(range(1, limit + 1, 2))

# usar el iterador
for num in odd_itter:
    print(num)
