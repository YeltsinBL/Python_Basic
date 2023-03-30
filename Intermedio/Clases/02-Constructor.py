"""Clases"""

class PrimeraClase:
    """Clase con constructor sin parámetros"""
    # Este constructor sirve para inicializar los atributos de la clase
    def __init__(self) -> None:
        self.nombre = "Python"

primera = PrimeraClase()
print(primera.nombre)

class SegundaClase:
    """Clase con constructor con parámetros obligatorio y opcional"""
    # Constructor de la clase para pasarle datos si los necesitara
    # también pueden ser opcionales

    def __init__(self, nombre, apellido="") -> None:
        self.nombre = nombre
        self.apellido = apellido

c = SegundaClase("Python")
print("Nombre:", c.nombre)
print("Apellido:", "Vacio" if c.apellido == "" else c.apellido)
c = SegundaClase("Python", "Opcional")
print("Nombre:", c.nombre)
print("Apellido:", "Vacio" if c.apellido == "" else c.apellido)
