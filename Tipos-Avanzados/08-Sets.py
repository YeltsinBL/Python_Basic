# Colección de datos que no se pueden repetir, no esta ordenada ni se puede acceder a sus datos por el índice

numeros = {1, 2, 2, 3, 3, 4}
mas_numeros = {3, 4, 4, 5, 5, 6, 7}
otra_forma = set([1, 2, 3, 4, 5])

print(numeros)

# print(numeros[0]) # error

numeros.add(5)  # agregar
numeros.remove(4)  # eliminar

# iterar
for numero in numeros:
    print(numero)


# Operadores de los Sets

# unión de dos Sets
print(numeros | mas_numeros)
# intersección de dos Sets
print(numeros & mas_numeros)
# diferencia: muestra los datos de la primera Tupla y
# elimina los valores de la primera tupla si es que ya existe en la segunda
print(numeros - mas_numeros)
# diferencia Simétrica: muestra los datos que no intersectan entre la primera y segunda Tupla
print(numeros ^ mas_numeros)
