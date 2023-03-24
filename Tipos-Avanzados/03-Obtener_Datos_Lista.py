numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Utilizando el Indice
uno = numeros[0]
dos = numeros[1]
tres = numeros[2]
print(uno, dos, tres)

# Asignando directamente a las variables con una variable iterable obligatoria
primero, segundo, *mas, ultimo = numeros
print(primero, segundo, mas, ultimo)  # 1 2 [3, 4, 5, 6, 7] 8

# Utilizando For
for numero in numeros:
    print(numero)

# Utilizando For para obtener el dato y su índice
for indice, numero in enumerate(numeros):
    print(indice, numero)
