# Copiar lista

#Utilizando slicing
A = [1,2,3,4,5]
C = A[:]

print(id(A))
print(id(C))

# Se copia la referencia de la lista A a la lista B
B = A

print(A)
print(B)

A.append(6)
print(A)
print(B)