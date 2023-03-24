"""Funciones"""

# Función Simple

def hola():
    """Mostrar un simple Hola"""
    print("Hola")

hola()

# Función con Parámetros

def hola_nombre(nombre):
    """Mostrar un Hola pasandole un dato"""
    print(f"Hola {nombre}")

hola_nombre("Yeltsin")

# Función con Parámetros Opcionales

def hola_nombre_opcional(nombre, apellido = "Baltodano"):
    """Mostrar un Hola pasandole un dato opcional"""
    print(f"Hola {nombre} {apellido}")

hola_nombre_opcional("Yeltsin")
hola_nombre_opcional("Yeltsin", "León")

# Utilizar la función nombrando sus parámetros

hola_nombre_opcional(apellido="BL",nombre="Guillermo")
