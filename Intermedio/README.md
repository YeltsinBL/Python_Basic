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
class SegundaClase:
    """Clase con constructor con parámetros: obligatorio y opcional"""
    def __init__(self, nombre, apellido="") -> None:
        self.nombre = nombre
        self.apellido = apellido
```
> Nota: el contructor sirve para pasarle datos a la clase cuando sea llamado y esta haga la lógica que tenga. Si los atributos de las clases no tienen un valor de inicio, se pueden crear directamente en el constructor.


[//]: # (Enlaces a la documentación)

[clase]: <https://github.com/YeltsinBL/Todo_Python/blob/master/Intermedio/Clases/01-Clase.py>
[constructor] : <https://github.com/YeltsinBL/Todo_Python/blob/master/Intermedio/Clases/02-Constructor.py>