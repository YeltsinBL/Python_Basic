# Obtener solo los Nombres
usuarios =[["Python", 4], ["Practica", 2], ["Comprensión", 9]]

# Usando For
nombres =[]
for usuario in usuarios:
    nombres.append(usuario[0])

#print(nombres)

# Usando la Comprensión de lista: [expresion for item in items]
nombres2 = [usuario[0] for usuario in usuarios]
print(nombres2)

# Usando la Comprensión de lista: [expresion for item in items] con filtrado
nombres2 = [usuario[0] for usuario in usuarios if usuario[1] > 3]
print(nombres2)


# Usando Map
nombre_map = list(map(lambda usuario:usuario[0], usuarios))
print(nombre_map)
# Usando Filter
nombre_filter = list(filter(lambda usuario:usuario[1] > 3, usuarios))
print(nombre_filter)
