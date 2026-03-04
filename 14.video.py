# Diccionarios en python
numbers = {1: "one", "2": "two", 3: "three", 4: "four", 5: "five"}
print(numbers)

print(numbers[1])
print(numbers["2"])

data = {
    "name": "Cristian",
    "age": 20,
    "city": "Sensuntepeque"
}

del data["city"]

claves = data.keys()
print(claves)

valores = data.values()
print(valores)

pares = data.items()
print(pares)


contactos = {
    "Carla": {
        "apellido": "Florida", 
        "altura": 1.7, 
        "edad": 30
        },
    "Diego": {
        "apellido": "Antesana", 
        "altura": 1.75, 
        "edad": 32
    }
}
print(contactos["Carla"])