# Manejo de Excepciones y Errores en Python

# try:
#     divisor = int(input("Ingrese un numero divisor: "))
#     result = 100 / divisor
#     print("El resultado de la división es: ", result)
# except:
#     print("Error: El divisor no puede ser cero.")



# try:
#     divisor = int(input("Ingrese un numero divisor: "))
#     result = 100 / divisor
#     print("El resultado de la división es: ", result)
# except ZeroDivisionError:
#     print("Error: El divisor no puede ser cero.")
# except ValueError:
#     print("Error: El divisor debe ser un numero entero.")



try:
    divisor = int(input("Ingrese un numero divisor: "))
    result = 100 / divisor
    print("El resultado de la división es: ", result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero.")
    print("Ha ocurrido un error: ", e)
except ValueError:
    print("Error: El divisor debe ser un numero entero.")


def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + str(exception_class))
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 2)

print_exception_hierarchy(Exception)
