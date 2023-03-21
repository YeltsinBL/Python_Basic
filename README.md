# Python Básico
## _Iniciando en la programación con Python_
Descripción de lo realizado en este repositorio

Dentro de `Variables` se realizó:
En `01-Variables` se hizo los tipos de variables más utilizados:
- Int: representa los valores enteros.
- Float: representa todos los números decimales.
- String: representa los caracteres (letras y números) dentro de comillas simples o dobles.

> Nota: para hacer los comentarios se utilizan: el hashtag (#) para hacer comentarios en una sola línea y triple comillas simples o dobles iniciales y finales ("""texto""" ó '''texto''') para comentar en varias líneas.

En `02-Strings` se hizo la forma de Acceder a un String en su Posición:
- 'Acceder a un caracter de la posición indicada': agregando al final de la variable un corchete con el número de la posición.
- 'Acceder al caracter desde-hasta la posición indicada': agregando al final de la variable un corchete con dos números separados por los dos puntos.
- 'Acceder al caracter desde una posición inicial hasta el final': agregando al final de la variable un corchete con un número inicial y luego los dos puntos.
- 'Acceder al caracter desde el inicio hasta una posición final': agregando al final de la variable un corchete con los dos puntos y luego un número final 
- 'Acceder al caracter desde el inicio hasta el final': agregando al final de la variable un corchete con los dos puntos.


> nombre_lenguaje_programacion = "Python"
> print("Acceder al caracter desde-hasta en su posición:", nombre_lenguaje_programacion[0:2])
> print("Acceder al caracter desde una posición hasta el final:",
      nombre_lenguaje_programacion[3:])
> print("Acceder al caracter desde inicio hasta una posición:",
      nombre_lenguaje_programacion[:2])
> print("Acceder al caracter desde inicio " +
      "hasta el final de su posición:", nombre_lenguaje_programacion[:])


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

Para más ejemplos de los Métodos puede entrar [aquí][metodosString]

En `02-Strings` se hizo algunas Secuencias de Escape para agregar al String:
- Se pueden agregar comillas o doble comillas dentro del String, para ello se debe utilizar los dos tipos de comillas para diferenciarlas.
- Otra forma de hacerlo es utilizar la Secuencia de Escape '\'.
-- \": agrega la comilla dentro del String.
-- \n: hace un salto de linea.
-- \b: elimina la posición anterior donde se ha agregado..

Para más ejemplos de las Secuencias puede entrar [aquí][secuenciaescape]




[//]: # (Enlaces a la documentación)

[formatearString]: <https://docs.python.org/es/3/reference/lexical_analysis.html#formatted-string-literals>
[metodosString]: <https://docs.python.org/3/library/stdtypes.html#string-methods>
[secuenciaescape]: <https://docs.python.org/es/3/reference/lexical_analysis.html#literals>
