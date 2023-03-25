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

### Acceder a los elementos de la Lista
En `02-Accediendo_Listas` se utilizó la posición de sus indices para acceder a los elementos, al igual que se hizo con los [String][stringReadme].
```sh
palabras = ["Hola", "Python", "Accediendo", "Datos", "Listas", "Ejemplo"]
palabras[0] = "Cambio"  # cambiamos el nombre indicando cual es el indice
print(palabras)
print(palabras[2:])
print(palabras[-1])  # accedemos al último elemento de la lista
# escogemos los elementos de la lista, desde el índice de inicio luego todos los indices sumados el valor indicado
print(palabras[::2])
# escogemos los elementos de la lista, indicando el índice de inicio luego todos los indices sumados el valor indicado
print(palabras[1::2])
# escogemos los elementos de la lista, indicando el índice de inicio y el índice final, luego sumamos el valor indicado al índice.
print(palabras[1:4:2])

numeros = list(range(1, 21))
# obtenemos todos los números negativos desde el 5 al 15
print(numeros[4:15:2])
```

### Obtener los datos de una Lista
En `03-Obtener_Datos_Lista` se realizó las formas en cómo obtener los datos de una lista.
- Utilizando directamente el índice.
```sh
numeros = [1, 2, 3,4,5,6,7,8]
# Utilizando el Indice
uno = numeros[0]
dos = numeros[1]
tres = numeros[2]
print(uno, dos, tres)
```
- Asignando directamente a las variables en una misma línea: con una variable iterable obligatoria.
- La variable iterable tambien se usa como [parámetro en una función][parametroIterable]. 
```sh
numeros = [1, 2, 3,4,5,6,7,8]
primero, segundo, *mas,ultimo = numeros
print(primero, segundo, mas, ultimo) #1 2 [3, 4, 5, 6, 7] 8
```
- Utilizando For para obtener solo los datos.
 ```sh
 numeros = [1, 2, 3,4,5,6,7,8]
for numero in numeros:
    print(numero)
 ```
 - Utilizando For para obtener los datos con sus índices: con un 'Enumerate'.
 - El Enumerate devuelve la posición/índice de lo que se le pase en ese orden.
 ```sh
 numeros = [1, 2, 3,4,5,6,7,8]
for indice, numero in enumerate(numeros):
    print(indice, numero)
 ```

### Buscar - Agregar - Eliminar los datos de una Lista
En [`04-Buscar_Modificar_Lista`][buscarModificarLista] se realizaron algunos ejemplos:
- Buscar por el valor del elemento usando 'index': la búsqueda es de izquierda a derecha, si se repite el valor del elemento devuelve el índice del primer elemento porque al encontrarlo ya no continúa con la búsqueda.
- Buscar cuantas veces se repite un elemento.
- Buscar si existe un valor en los elementos de la lista.
```sh
# Búsqueda
palabras=["Hola", "Python", "Programación", "Ejercicios", "Practica", "Python"]
print(palabras.index("Python")) # 1
print(palabras.count("Python")) # 2
print("Hola" in palabras) # True
```
- Agregar un elemento a la lista indicando una posición.
- Agregar un elemento al final de la lista.
```sh
# Agregar
palabras=["Hola", "Python", "Programación", "Ejercicios", "Practica", "Python"]
palabras.insert(1,"Agregado") # ["Hola", "Agregado", "Python", "Programación", "Ejercicios", "Practica", "Python"]
palabras.append("Final") # ["Hola", "Agregado", "Python", "Programación", "Ejercicios", "Practica", "Python", "Final"]
```
- Eliminar de acuerdo a la palabra, empieza de izquierda a derecha.
- Eliminar la última posición
- Eliminar indicando el índice
- Eliminar todos los elementos de la lista
```sh
# Eliminar
palabras=["Hola", "Python", "Programación", "Ejercicios", "Practica", "Python"]
palabras.remove("Python") # ["Hola", "Programación", "Ejercicios", "Practica", "Python"]
palabras.pop() # ["Hola", "Python", "Programación", "Ejercicios", "Practica"]
palabras.pop(3) # ["Hola", "Python", "Programación", "Practica", "Python"]
palabras.clear() # []
```

### Ordenar los datos de una Lista
En [`05-Ordenar_Lista`][ordenarLista] se hizo ejemplos usando 'Sort' y 'Sorted':
- Sort: ordena los elementos en la misma lista.
- Sorted: crea una nueva lista ordenada a partir de otra lista.
```sh
# Usando Sort
letras = ["a", "c","e","b","d"]
letras.sort() # ordena de forma ascendente
letras.sort(reverse=True) # ordena de forma descendente
print(letras)
# Usando Sorted
numeros = [1, 2, 9, 6, 8, 3, 7, 5]
numeros2 = sorted(numeros) # ordena de forma ascendente
numeros2 = sorted(numeros, reverse=True) # ordena de forma descendente
print(numeros2)
```
- Para ordenar una lista dentro de otra lista, normalmente se ordena por la primera posición de la lista interior.
```sh
usuario = [["Python", 4], ["Ejercicio", 1], ["Ordenar", 5]]
usuario.sort()
print(usuario) # [['Ejercicio', 1], ['Ordenar', 5], ['Python', 4]]
```
- Pero para ordenar por el identificador o la segunda posición, se puede hacer creando una 'función' o utilizando 'lambda'.
```sh
usuario = [["Python", 4], ["Ejercicio", 1], ["Ordenar", 5]]
# Ordenar de forma ascendente la Lista de Lista por el número creando una función
def ordenar(elemento):
    """recibe un iterable para devolver los elementos de la posición 1"""
    return elemento[1]
usuario.sort(key=ordenar) 
print(usuario)
# Ordenar de forma descendente la Lista de Lista por el número usando Lambda
usuario.sort(key=lambda elemento: elemento[1], reverse= True)
print(usuario)
```

> Nota: En el 'sort' con función, el parámetro 'key' recibe la indicación por cuál elemento ordenar, en este caso, la función 'ordenar' devuelve el identificador.  
En el 'sort' con lambda, al parámetro 'key' se le especifica que se utilizará la forma 'lambda', en la que el primero 'elemento' hace referencia a la lista que se quiere ordenar y el segundo elemento con el corchete hace referencia por cuál posición/índice de la lista interna se tendrá que ordenar.

### Comprensión de Listas
En [`06-Comprension_Lista`][comprensionLista] obtuvimos los valores de una lista utilizando el [For][forReadme] y la Comprensión de Lista.
- La forma que tiene una Comprensión de lista es la siguiente: [expresion for item in items].
```sh
# Obtener solo los Nombres
usuarios =[["Python", 4], ["Practica", 2], ["Comprensión", 9]]
# Usando la Comprensión de lista
nombres2 = [usuario[0] for usuario in usuarios]
print(nombres2) # ['Python', 'Practica', 'Comprensión']
# Usando la Comprensión de lista con filtrado
nombres2 = [usuario[0] for usuario in usuarios if usuario[1] > 3]
print(nombres2) # ['Python', 'Comprensión']
```
- Lo mismo que se hizo con la Comprensión de Listas se puede hacer usando las funciones de Map y Filter.
```sh
usuarios =[["Python", 4], ["Practica", 2], ["Comprensión", 9]]
# Usando Map
nombre_map = list(map(lambda usuario:usuario[0], usuarios))
print(nombre_map)
# Usando Filter
nombre_filter = list(filter(lambda usuario:usuario[1] > 3, usuarios))
print(nombre_filter)
```
> Nota: Con la comprensión de lista podemos modificar y filtar una lista.
Para la programación funcional en vez de usar la Comprensión de Listas se usa el Map y Filter. Utilizar cualquiera de las dos formas esta bien.

### Tuplas
En [`07-Tupla`][tupla] todos los ejemplos son iguales a lo que se puede hacer con una [lista][listasReadme], excepto que no se pueden modificar sus elementos, solo son de modo lectura.
- Para crear una Tupla se hace con los 'paréntesis' o llamando a la clase 'tuple'.
```sh
numeros = (1, 2, 3)
numeros_otros = tuple([0, 1, 2,3,4,5])
```
- Todas las operaciones son las mismas que una lista.
```sh
numeros_escogido = numeros[:2]
primer, segundo, *otros = numeros_otros
print(primer, segundo, otros)

for n in numeros:
    print(n)
```
- Para modificar los valores de una Tupla, se tiene que crear una lista a partir de la Tupla y modificar los valores de la lista creada.
```sh
lista_numeros = list(numeros_otros)
lista_numeros[1] = 80
print(lista_numeros)
```
> Nota: En las Tuplas no se pueden editar sus valores, solo leerlas. En las Listas si se pueden editar y leer sus valores.

[//]: # (Enlaces a la documentación)

[tiposVariables]: <https://docs.python.org/3/library/stdtypes.html#>
[formatearString]: <https://docs.python.org/es/3/reference/lexical_analysis.html#formatted-string-literals>
[metodosString]: <https://docs.python.org/3/library/stdtypes.html#string-methods>
[secuenciaescape]: <https://docs.python.org/es/3/reference/lexical_analysis.html#literals>
[moduloMath]: <https://docs.python.org/3/library/math.html>
[controlFlujo]: <https://docs.python.org/es/3/tutorial/controlflow.html>
[funciones]: <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>
[listas]: <https://docs.python.org/3/library/stdtypes.html?highlight=list#lists>

[stringReadme]: <https://github.com/YeltsinBL/Python_Basic/blob/master/README.md#strings>
[parametroIterable]: <https://github.com/YeltsinBL/Python_Basic/blob/master/README.md#funciones-con-par%C3%A1metro-iterable>
[forReadme]:<https://github.com/YeltsinBL/Python_Basic/blob/master/README.md#for>
[listasReadme]:<https://github.com/YeltsinBL/Python_Basic/blob/master/README.md#listas>

[buscarModificarLista]:<https://github.com/YeltsinBL/Python_Basic/blob/master/Tipos-Avanzados/04-Buscar_Modificar_Lista.py>
[ordenarLista]:<https://github.com/YeltsinBL/Python_Basic/blob/master/Tipos-Avanzados/05-Ordenar_Lista.py>
[comprensionLista]:<https://github.com/YeltsinBL/Python_Basic/blob/master/Tipos-Avanzados/06-Comprension_Lista.py>
[tupla]:<https://github.com/YeltsinBL/Python_Basic/blob/master/Tipos-Avanzados/07-Tupla.py>
