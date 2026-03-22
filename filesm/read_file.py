# leer un archivo linea por linea
"""
with open('files.txt', 'r') as file:
    for line in file:
        print(line)
"""
# Leer todas las lineas en una lista
"""
with open('files.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
"""

# Escribir en un archivo
with open('files.txt', 'a') as file:
    file.write("This is a new line")
