"""Métodos"""

class Decorador:
    """Clase"""

    def __init__(self, nombre) -> None:
        self.__nombre = self.__metodo_privado(nombre)

    def __metodo_privado(self, nombre) -> str:
        return nombre.upper()

    @property
    def nombre(self):
        """Uso de la property para obtener el valor del atributo privada"""
        return self.__nombre

    # se usa para actualizar el valor del atributo privado
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = self.__metodo_privado(valor)

clase = Decorador("python")
print(clase.nombre)
clase.nombre = "Nuevo nombre"
print(clase.nombre)
