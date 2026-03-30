import math

def calculate_area(length, width):
    """
    Calcula el area de un rectangulo

    Parámetros:
    length (float): longitud del rectangulo
    width (float): ancho del rectangulo

    Retorna:
    float: area del rectangulo
    """
    return length * width


def calculate_area_circle(radius):
    """
    Calcula el area de un circulo

    Parámetros:
    radius (float): radio del circulo

    Retorna:
    float: area del circulo
    """
    return math.pi * radius**2

print(calculate_area(10, 20))
print(calculate_area_circle(10))