"""Métodos"""

class Metodo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def sin_parametro(self) -> str:
        """Método con parámetro"""
        return "Método sin parámetro"

    def con_parametro(self, nomb) -> str:
        """Método con parámetro"""
        return nomb + " " + self.nombre
    def __metodo_privado(self) -> int:
        return 1
    def uso_metodo_privado(self) -> str:
        return f"Valor del método privado: {self.__metodo_privado()}"


clase = Metodo("Python")
conPara = clase.con_parametro("Uso")
print(conPara)
sinPara = clase.sin_parametro()
print(sinPara)
# error de acceso por método privado, solo se usa en la clase
# privado = clase.__metodo_privado()
# print(privado)
uso_privado = clase.uso_metodo_privado()
print(uso_privado)
