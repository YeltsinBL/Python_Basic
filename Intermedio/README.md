# Python Intermedio
## Continuando con la programación en Python_

Descripción de lo realizado en cada uno de los archivos que contienen las carpetas.

## Clases
### Clase
En [`01-Clase`][clase] se creó una clase con sus atributos.

```sh
class PrimeraClase:
    """Primera clase de prueba"""
    # Atributos de la clase
    id = 1
    nombre = "Python"
    descripcion = "Primera clase"
    activo = True
```

> Nota: debido a las buenas practicas, el nombre de las clases deben usar la notación de PascalCase.

- En [`02-Constructor`][constructor] se creó 2 clase para mostrar el 'init' con/sin parámetros.

```sh
class PrimeraClase:
    """Clase con constructor sin parámetros"""
    def __init__(self) -> None:
        self.nombre = "Python"
        self.__descripcion = "Atributo pribado"

class SegundaClase:
    """Clase con constructor con parámetros: obligatorio y opcional"""
    def __init__(self, nombre, apellido="") -> None:
        self.nombre = nombre
        self.apellido = apellido
```
> Nota: el contructor sirve para pasarle datos a la clase cuando sea llamado y esta haga la lógica que tenga. Si los atributos de las clases no tienen un valor de inicio, se pueden crear directamente en el constructor. Los atributos privados inician con 'doble guión bajo' (__) antes de la palabra.
- En [`03-Metodo`][metodo] se crearon diferentes tipos de métodos que pueden existir.
```sh
class Metodo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def sin_parametro(self) -> str:
        """Método sin parámetro"""
        return "Método sin parámetro"

    def con_parametro(self, nomb) -> str:
        """Método con parámetro"""
        return nomb + " " + self.nombre
    def __metodo_privado(self) -> int:
        """Método privado"""
        return 1
    def uso_metodo_privado(self) -> str:
        return f"Valor del método privado: {self.__metodo_privado()}"
    @staticmethod
    def valor_pi():
        """Método Estático"""
        return 3.1416
```
> Nota: mos métodos son funciones, pero aquí es obligatorio llevar la palabra reservada 'self' para poder acceder a los atributos de la clase. Al igual que los atributos, también hay métodos privados.

- En [`04-Decorador_Property`][decoradorProperty] se trabajó solo con el atributo privado.
```sh
class Decorador:
    def __init__(self, nombre) -> None:
        self.__nombre = self.__metodo_privado(nombre)
    def __metodo_privado(self, nombre) -> str:
        return nombre.upper()
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = self.__metodo_privado(valor)
```
> Nota: el decorador property solo trabaja con los atributos privados para poder obtener y actualizar su valor

[//]: # (Enlaces a la documentación)

[clase]: <https://github.com/YeltsinBL/Todo_Python/blob/master/Intermedio/Clases/01-Clase.py>
[constructor]: <https://github.com/YeltsinBL/Todo_Python/blob/master/Intermedio/Clases/02-Constructor.py>
[metodo]: <https://github.com/YeltsinBL/Todo_Python/blob/master/Intermedio/Clases/03-Metodo.py>
[decoradorProperty]: <https://github.com/YeltsinBL/Todo_Python/blob/master/Intermedio/Clases/04-Decorador_Property.py>