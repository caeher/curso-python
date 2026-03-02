name = "Cristian"
character = "C"
print(type(name))
print(type(character))

print("Ver el tipo en pytho se utiliza la función type()")
print("Ejemplo: print(type(name))")

name_comilla_simple = 'Cristian'
name_comilla_doble = "Cristian"
name_triple_comilla_simple = '''Cristian'''
name_triple_comilla_doble = """Cristian"""

print(type(name_comilla_simple))
print(type(name_comilla_doble))
print(type(name_triple_comilla_simple))
print(type(name_triple_comilla_doble))

print("En python usando comillas triples (simples o dobles) se pueden escribir textos en varias líneas")

sentence = """Hola
Mundo
Estudiante: Cristian
Curso: Python"""

print(sentence)

name = "Cristian"
print(name[0])

print("En python las cadenas de texto pueden ser indexadas, es decir, se puede acceder a cada uno de los caracteres que la componen utilizando corchetes [] y el índice del carácter deseado")

print("para poner en reversa un texto, la forma rápida es utilizando el slicing con un paso negativo")
print(name[::-1])

last_name = "Escalante"
print(name + " " + last_name)
print("Las cadenas de texto se pueden concatenar utilizando el operador +")

dot = "."
print(dot * 10)
print("El operador * se puede utilizar para repetir una cadena de texto un número determinado de veces")

