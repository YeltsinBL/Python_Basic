numeros = (1, 2, 3)
numeros_otros = tuple([0, 1, 2,3,4,5])

numeros_escogido = numeros[:2]
primer, segundo, *otros = numeros_otros
print(primer, segundo, otros)

for n in numeros:
    print(n)

# crear lista apartir de una tupla para modificar los valores
lista_numeros = list(numeros_otros)
lista_numeros[1] = 80
print(lista_numeros)
