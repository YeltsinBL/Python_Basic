# Python Básico
## _Iniciando en la programación con Python_
Descripción de lo realizado en este repositorio


## Variables

### Tipos
En `01-Tipos` se hizo los tipos de variables más utilizados:
- Int: representa los valores enteros.
- Float: representa todos los números decimales.
- String: representa los caracteres (letras y números) dentro de comillas simples o dobles.

> Nota: para hacer los comentarios se utilizan: el hashtag (#) para hacer comentarios en una sola línea y triple comillas simples o dobles iniciales y finales ("""texto""" ó '''texto''') para comentar en varias líneas.

Para más ejemplos de los Tipos de Variables puede entrar [aquí][tiposVariables]

### Strings

En `02-Strings` se hizo la forma de Acceder a un String en su Posición:
- 'Acceder a un caracter de la posición indicada': agregando al final de la variable un corchete con el número de la posición.
- 'Acceder al caracter desde-hasta la posición indicada': agregando al final de la variable un corchete con dos números separados por los dos puntos.
- 'Acceder al caracter desde una posición inicial hasta el final': agregando al final de la variable un corchete con un número inicial y luego los dos puntos.
- 'Acceder al caracter desde el inicio hasta una posición final': agregando al final de la variable un corchete con los dos puntos y luego un número final 
- 'Acceder al caracter desde el inicio hasta el final': agregando al final de la variable un corchete con los dos puntos.

```sh
nombre_lenguaje_programacion = "Python"
print("Acceder al caracter desde-hasta en su posición:", nombre_lenguaje_programacion[0:2])
print("Acceder al caracter desde una posición hasta el final:",
      nombre_lenguaje_programacion[3:])
print("Acceder al caracter desde inicio hasta una posición:",
      nombre_lenguaje_programacion[:2])
print("Acceder al caracter desde inicio " +
      "hasta el final de su posición:", nombre_lenguaje_programacion[:])
```

En `02-Strings` se hizo la forma de Formatear los String:
- Para concatenar o unir dos string se puede usar el '+'.
- Otra forma es usando el Operador de Formateo de String 'f'.
-- Se agrega al inicio de la asignación de valor a una variable la 'f' seguido de comillas y dentro de ellas se agrega unas llaves para que allí se haga las operaciones.

```sh
nombre_completo_otra_forma = f"{nombre} {apellido}"
uso_formateo_string =  f"{nombre[0]} {2 + 3}"
```

Para más ejemplos del Formateador puede entrar [aquí][formatearString]

En `02-Strings` se hizo agregó algunos Métodos de String:
- upper: convertir todo a matúsculas.
- lower: convertir todo a minúsculas.
- capitalize: la primera letra del string a mayúscula y lo demás en minúscula.
- title: todas las primeras letras de cada palabra en el String en mayúscula.
- strip: elimina los espacios iniciales y finales del string.
- lstrip: elimina solo los espacios del inicio del string.
- rstrip: elimina solo los espacios del final del string.
- find: busca la palabra ingresada dentro del string y devuelve la posición inicial.
- Replace: reemplaza la palabra del ingresada del lado izquierdo por una nueva ingresada del lado derecho separadas por una coma.
- in: verifica si existe la palabra ingresada dentro del String y devuelve un booleano.
- not in: verifica si no existe la palabra ingresada dentro del String y devuelve un booleano.

```sh
print("de" in metodo_String)
print("uso" not in metodo_String)
```

Para más ejemplos de los Métodos puede entrar [aquí][metodosString]

En `02-Strings` se hizo algunas Secuencias de Escape para agregar al String:
- Se pueden agregar comillas o doble comillas dentro del String, para ello se debe utilizar los dos tipos de comillas para diferenciarlas.
- Otra forma de hacerlo es utilizar la Secuencia de Escape '\'.
-- \": agrega la comilla dentro del String.
-- \n: hace un salto de linea.
-- \b: elimina la posición anterior donde se ha agregado..

```sh
eliminar_En_String = "Python \b\"Básico\""
print("Eliminar lo que hay en una posición atrás:",eliminar_En_String)
```

Para más ejemplos de las Secuencias puede entrar [aquí][secuenciaescape]

### Números

En `03-Numeros`  se hizo los operadores matemáticos con notación:

| Operadores con Notación | Descripción |
| ------ | ------ |
| += | suma ( 2 += 2) |
| -= | resta ( 2 -= 2) |
| *= | multiplicación ( 2 *= 2) |
| /= | división ( 2 /= 2) |
| //= | división entera ( 2 //= 2) |
| **= | potencia ( 2 **= 2) |
| %=  | módulo-residuo de división ( 2 %= 2) |

En `03-Numeros`  se utilizó algunas funciones nativas y del módulo 'Math':
- Nativas:
-- Round: redondeda el número.
-- Abs: devuelve el valor obsoluto del número.
- Módulo Math:
-- ceil: devuelve el número superior entero más cercano: 2.
-- floor: devuelve el número inferior entero más cercano: 1.
-- isnan: acepta solo número reales y devuelve un boolean negandolo.
-- pow: eleva a la potencia.
-- sqrt: devuelve la raíz cuadrada.

```sh
print(math.ceil(1.1)) # 2
print(math.floor(1.99)) # 1
print(math.isnan(7)) # false
print(math.pow(10,2)) # 100
print(math.sqrt(9)) # 3
```

Para más ejemplos de Funciones usando el Módulo Math puede entrar [aquí][moduloMath]


### Boolean

En `04-Boolean` se hizo las converiones para saber cuando se obtienen False y True:
- Solo devuelve False cuando son de tipo: "", None, 0.

```sh
print(bool("")) # False
print(bool("0")) # True
print(bool(None)) # False
print(bool(" ")) # True
print(bool(0)) # False
```

## Control-Flujo

Para saber más sobre Control de Flujo puede entrar [aquí][controlFlujo]

### Comparadores Lógicos

| Comparadores | Descripción |
| ------ | ------ |
| > |print(1 > 2) # False |
| < |print(1 < 2) # True |
| >= |print(1 >= 2) # False |
| <= |print(1 <= 2) # True |
| == |print(1 == 2) # False |
| != |print(1 != 2) # True |
| !=  |print(1 != "1") # True |

### IF y Operador Termario

En `02-IFyOperadorTermario` se hizo el flujo del IF y un Operador Termario:
- IF: es muy habitual usarlo.
- Operador Termario: solo se usa en ciertas ocasiones.

```sh
edad = 24

# IF
if edad > 60:
    print("Accedió al adulto mayor")
elif edad >17:
    print ("Ya es mayor de edad")
else: print("Aún es menor de edad")

# Operador Termario
mensaje = "Es mayor de edad" if edad > 17 else "Es menor de edad"
print(mensaje)
```

### Operadores Lógicos

En `03-Operadores_Logicos` se hizo un ejemplo usando: and, or y not

| Operadores Lógicos | Descripción |
| ------ | ------ |
| And | todos en la evaluación son verdaderos.  |
| Or | solo uno de la evaluación debe de ser verdadero. |
| Not | niega el valor de la variable que le sigue, si es True lo cambia a Falso o viceversa pero solo en la evaluación. |

```sh
persona, animal, cosa = True, False, False
if not cosa and (persona or animal):
    print("Ingresó al IF")
else : print("No toda la evaluación es True")
```

### FOR

En `04-For` se hizo un ejemplo de como usarlo:
- Sirve para poder iterar, buscar y más dentro de una lista y/o string.

```sh

buscar = 2

# el Range es un iterable
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado")
        break
else:
    print("No encontrado")

```
- El ELSE al final del For se debe de utilizar con un Break, porque al termina de recorrer la lista lo ejecutará igualmente, en cambio; con el Break termina la secuencia y no lo ejecuta.


### WHILE

En `05-While` se hizo un ejemplo de como usarlo:
- También es un Loop al igual que el For 
pero se ejecuta siempre y cuando se cumpla la condición.

```sh
numero = 1
while numero < 10:
    print(numero)
    numero *= 2
    if numero == 4:
        break
```
- Al igual que en el For, el break corta la ejecución y no se utiliza el ELSE al final, mayormente se utilizan en 'While Infinitos'.

```sh
numero = 1
while True:
    comando = input("$ ")
    if comando.lower() == "salir":
        break
```

### Loop Anidado

En `06-Loop_Anidado` se hizo un ejemplo usando un For dentro de otro For:
- El primero For no continuará hasta que el for de adentro termine de iterar.

```sh
for x in range(6):
    for j in range(2):
        print(x,j)
```

## FUNCIONES

Para saber más sobre Funciones puede entrar [aquí][funciones]

### Funciones sin/con parámetros y opcionales
En `01-Funcion` se hizo un ejemplos de funciones:
- Para crear una función se utiliza la palabra reservada 'def' seguida por el 'nombre de la función' con 'paréntesis'  y terminando con 'doble punto'.
- Función sin parametro:

```sh
def hola():
    """Mostrar un simple Hola"""
    print("Hola")

hola()
```
- Función con Parámetro Obligatorio.

```sh
def hola_nombre(nombre):
    """Mostrar un Hola pasandole un dato"""
    print(f"Hola {nombre}")

hola_nombre("Yeltsin")
```
- Función con Parámetro Opcional.

```sh
def hola_nombre_opcional(nombre, apellido = "Baltodano"):
    """Mostrar un Hola pasandole un dato opcional"""
    print(f"Hola {nombre} {apellido}")

hola_nombre_opcional("Yeltsin")
hola_nombre_opcional("Yeltsin", "León")
```
- Utilización de la función nombrando sus parámetros.

```sh
hola_nombre_opcional(apellido="BL",nombre="Guillermo")
```

### Funciones con parámetro Iterable
En `02-Xargs`  se llama así por "X" argumentos-parámetros que tendrá la función;
- En este ejemplo se se utiliza el For para recorrerlo:

```sh
def suma(*numeros):
    """esta es una función con un parámetro iterable, 
        no se especifica cuantos parámetros tendrá por lo cual se utiliza
        el For para recorrerlo"""
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2,3,1)
suma(2,3,)
suma(2,3,1,5)
```

### Funciones con parámetro de Diccionario
En `03-KWargs` se llama así "KW" por "KeyWord-Palabra clave", porque al momento de llamar a la función se le debe de pasar el parámetro con su nombre.
-  Al pasar el parámetro con su nombre, este parámetro dentro de la función es un "Diccionario de datos" ({nombre=valor}).

```sh
def get_product(**datos):
    """Cuando hay dos asteriscos en el parámetro, significa que 
        se utilizará el 'KW' (keyWord-palabra clave) del parámetro
    """
    print(datos) # este parámetro será un diccionario de datos: {nombre:valor}
    print(datos["id"], datos["nombre"]) # acceder a los datos del diccionario


 # para utilizar esta función, se debe de dar un nombre al parámetro
 # sino no funcionará
get_product(id=21, nombre="Python", desc="Función usando KWargs.")
```
> Nota: para acceder a los valores de los parámetros dentro de la función, se puede acceder utilizando los corchetes e ingresando el nombre del parámetro que es el "KW". Si los nombres no son iguales o no lo has enviado a la función, esta te dará un error.


### Función que devuelva un dato
En `04-Return` se hizo una función que después de operar devuelve un valor.
- La palabra reservada Return dentro de una función, se usa para devolver un valor.

```sh
def suma(a, b):
    """Con la palabra reservada Return, se puede devolver un valor desde la función"""
    return a + b

c = suma(5,1)

print(c)

```

### Función accediendo a una variable global
En `05-Variablle_Global` se hizo un ejemplo de como acceder a una variable fuera de la función.
- Para acceder a la variable se debe de usar la palabra reservada 'global' seguido del 'nombre de la variable'.

```sh
inicio = 8

def sumar():
    """acceder al una variable global"""
    global inicio 
    inicio +=1

print(inicio)
sumar()
print(inicio)
```
> Nota: se debe de tener un exigente cuidado al usar esta forma, debido a que las variables no son fuertemente tipadas y se puede cambiar facilmente el tipo de dato, dándose cuenta si hubo un error solo al momento de ejecutar el código.

```sh
inicio = 8

def sumar():
    global inicio 
    inicio +=1

print(inicio)
sumar()
print(inicio)

def cuidado():
    global inicio
    inicio = "Cambio de valor"

cuidado()
print(inicio)
sumar()
print(inicio)
```

## TIPOS AVANZADOS

### Listas
En `01-Listas` se hizo los tipos de listas en que se pueden crear.
- Para crear una lista solo vasta usar los corchetas y agregar datos dentros.

```sh
lista_vacia = []
numeros = [0, 1, 2, 3]
letras = ["a", "b", "c"]
palabras = ["hola", "python", "listas"]
booleanos = [True, False, False, True]
matriz = [[0, 1], [1, 0]]
ceros = [0] * 5  # repite la cantidad de la lista por el número indicado
letra_a = ["a"] * 5
```
- También se puede crear listas usando la clase integrada 'list' que acepta como parámetros datos iterables:
```sh
rango = list(range(1, 11))
unir_cero_a = list(ceros + letra_a)
numero_list=list([0,1,2,3])
caracteres= list("caracteres") # obtenemos todas las letras separadas
```

Para saber más sobre Listas puede entrar [aquí][listas]


[//]: # (Enlaces a la documentación)

[tiposVariables]: <https://docs.python.org/3/library/stdtypes.html#>
[formatearString]: <https://docs.python.org/es/3/reference/lexical_analysis.html#formatted-string-literals>
[metodosString]: <https://docs.python.org/3/library/stdtypes.html#string-methods>
[secuenciaescape]: <https://docs.python.org/es/3/reference/lexical_analysis.html#literals>
[moduloMath]:<https://docs.python.org/3/library/math.html>
[controlFlujo]:<https://docs.python.org/es/3/tutorial/controlflow.html>
[funciones]:<https://docs.python.org/3/tutorial/controlflow.html#defining-functions>
[listas]:<https://docs.python.org/3/library/stdtypes.html?highlight=list#lists>
