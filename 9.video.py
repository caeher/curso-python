# Entrada de datos
name = input("Ingrese su name: ")
print(name)

age = input("Ingrese su age: ")
print(age)

print(r"Hola {}, su age es {}".format(name, age))

print(type(name))
print(type(age))

# Casting de datos (cambiar su tipo de dato)

age = int(age)