# Son una colección de datos que se encuentran agrupados por una clave:valor (json)

datos = {"id": 1, "nombre": "Python", "otros": [{"ubicacion": "Peru"}]}
print(datos)
# acceder al valor mediante la palabra clave
print(datos["otros"])
# print(datos["estado"]) # si no existe muestra error
# agregar
datos["descripcion"] = "Agregar"
print(datos)
# verificar si existe la palabra clave
print("ciudad" in datos)

# otra forma de acceder al valor
print(datos.get("estado"))  # si no existe muestra 'None'
# si no existe la palabra clave muestrar mensaje por defecto
print(datos.get("estado", "No existe"))

# acceder a la clave y valor mediante iteracción

# acceder solo a las claves
for valor in datos:
    print(valor)
# Acceder a la clave:valor en forma de tuplas
for valor in datos.items():
    print(valor)
# Acceder a la clave:valor por separado
for clave,valor in datos.items():
    print(clave,valor)

# Lista de diccionarios
usuarios = [
    {"id": 1, "nombre": "Python"},
    {"id": 2, "nombre": "Practica"},
    {"id": 3, "nombre": "Iterar"},
]
# Iterando una lista de diccionarios para obtener los nombres
for usuario in usuarios:
    print(usuario["nombre"])
