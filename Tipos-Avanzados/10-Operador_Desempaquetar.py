# para obtener todos los elementos de un iterable de forma individual como si se recorriera con un For

# Listas
numero_lista = [1, 2, 3, 4]
print(*numero_lista)

numero_lista_2 = [5, 6, 7]

combinar_listas = [*numero_lista, *numero_lista_2]
print(combinar_listas)
print(*combinar_listas)

combinar_listas = ["Agregar", *numero_lista, "Python", *numero_lista_2]
print(combinar_listas)
print(*combinar_listas)

# Tuplas
numero_tupla = (1, 2)
print(*numero_tupla, 6)

print(*numero_lista, *numero_tupla)

# Diccionarios
datos = {"id": 1, "nombre": "Python"}
ubicacion = {"pais": "Peru", "codigo": 0000}
nuevo_diccionario = {**datos,
                     "ubicacion": [{**ubicacion, "numero": 1111}],
                     "descripcion": "prueba"}
print(nuevo_diccionario)
