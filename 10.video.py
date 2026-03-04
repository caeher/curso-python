# listas en python

todo = ["Dirigirnos al hotel", "Almorzar", "Visitar un museo", "Volver al hotel"]
print(todo)
print(type(todo))

mix = ["String", 1, 2.5, True, [2, 4]]
print(mix)

print("Ver el número de elementos de una lista se utiliza la función len()")
print(len(mix))

print("Acceder a los elementos de una lista se utiliza el índice del elemento deseado")
print(mix[0])
print(mix[1])
print(mix[-1]) // para acceder al último elemento de la lista
print(mix[0:3]) // para acceder a los elementos desde el índice 0 hasta el 3
print(mix[1:]) // para acceder a los elementos desde el índice 1 hasta el final
print(mix[:3]) // para acceder a los elementos desde el inicio hasta el índice 3
print(mix[::2]) // para acceder a los elementos desde el inicio hasta el final con un paso de 2
print(mix[::-1]) // para acceder a los elementos desde el final hasta el inicio

print("Añadir un elemento: append()")
mix.append(False)
print(mix)

print("insertar un elemento en un índice específico: insert()")
mix.insert(0, "Nuevo String")
print(mix)

print("Encontrar la primera aparicion de un elemento: index()")
print(mix.index("Nuevo String")

print("Ecnontrar el mayor elemento de la lista: max()"))
print(max(mix))

print("Encontrar el menor elemento de la lista: min()")
print(min(mix))

print("Eliminar elemento por indice")
del mix[0]

print("Eliminar una porción de la lista: del")
del mix[0:2]

print("Eliminar la lista: del")
del mix

