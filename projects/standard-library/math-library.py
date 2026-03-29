import math

# Calculadora

# Nota: math no tiene funciones add, subtract, multiply, divide
# Estas operaciones se hacen con operadores nativos de Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

print(math.sqrt(16))
print(math.pow(2, 3))
print(math.pi)
print(math.e)

# Area de un circulo r = pi * r^2
def area_circle(radius):
    return math.pi * radius**2

print(area_circle(10))

