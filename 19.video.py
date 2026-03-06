# Funcion sin parametro
def greet():
    print("Hello, World!")
greet()

# Funcion con parametro
def greetname(name):
    print("Hello, " + name + "!")
greetname("Cristian")


def greeting(name, lastname):
    print("Hello, " + name + " " + lastname + "!")
greeting("Cristian", "Escalante")


def plus(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

def calculator():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Multiplicación")
        print("3. División")
        print("4. Resta")
        print("5. Salir")
        choice = input("Ingrese su elección: ")
        if choice == "5":
            break
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        if choice == "1":
            print(plus(a, b))
        elif choice == "2":
            print(multiply(a, b))
        elif choice == "3":
            print(divide(a, b))
        elif choice == "4":
            print(subtract(a, b))
        elif choice == "5":
            print("Saliendo del programa")
            break
        else:
            print("Operación no válida")
calculator()