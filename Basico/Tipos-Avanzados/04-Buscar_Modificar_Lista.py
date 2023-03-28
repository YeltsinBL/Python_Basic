# Buscar en lista

palabras=["Hola", "Python", "Programación", "Ejercicios", "Practica", "Python"]

# obtenemos la posición de izquierda a derecha y se detiene en la primera palabra que encuentre
print(palabras.index("Python"))

# cuantas veces se repite una palabra en la lista
print(palabras.count("Python"))

# Existe esta palabra en la lista
print("Hola" in palabras)


#Agregar un elemento a la Lista

#Indicamos en qué posición queremos agregar el nuevo elemento
palabras.insert(1,"Agregado")
# Agregamos el elemento al final de la lista
palabras.append("Final")


# Eliminar elementos de la lista

# Eliminar de acuerdo a la palabra, empieza de izquierda a derecha
palabras.remove("Python")
# Eliminar la última posición
palabras.pop()
# Eliminar indicando el índice
palabras.pop(3)
#Eliminar todos los elementos de la lista
palabras.clear()
print(palabras)
