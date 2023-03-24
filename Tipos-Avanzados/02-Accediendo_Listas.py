"""Acceder a los datos de la lista"""

palabras = ["Hola", "Python", "Accediendo", "Datos", "Listas", "Ejemplo"]
palabras[0] = "Cambio"  # cambiamos el nombre indicando cual es el indice
print(palabras)
print(palabras[2:])
print(palabras[-1])  # accedemos al último elemento de la lista
# escogemos los elementos de la lista, desde el índice de inicio luego todos los indices sumados el valor indicado
print(palabras[::2])
# escogemos los elementos de la lista, indicando el índice de inicio luego todos los indices sumados el valor indicado
print(palabras[1::2])
# escogemos los elementos de la lista, indicando el índice de inicio y el índice final, luego sumamos el valor indicado al índice.
print(palabras[1:4:2])

numeros = list(range(1, 21))
# obtenemos todos los numeros negativos desde el 5 al 15
print(numeros[4:15:2])
