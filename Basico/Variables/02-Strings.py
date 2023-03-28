"""String"""

nombre_lenguaje_programacion = "Python"
descripcion_realizado = """
Todo lo que se puede hacer con 
el tipo String
"""

print(nombre_lenguaje_programacion, descripcion_realizado)

# Función para obtener la longitud del caracter
longitud_String = len(nombre_lenguaje_programacion)
print("Longitud del caracter", longitud_String)

print("Acceder al caracter en su posición:", nombre_lenguaje_programacion[0])
print("Acceder al caracter desde-hasta en su posición:",
      nombre_lenguaje_programacion[0:2])
print("Acceder al caracter desde una posición hasta el final:",
      nombre_lenguaje_programacion[3:])
print("Acceder al caracter desde inicio hasta una posición:",
      nombre_lenguaje_programacion[:2])
print("Acceder al caracter desde inicio " +
      "hasta el final de su posición:", nombre_lenguaje_programacion[:])

print(("---Formatear String---").upper())

nombre = "Yeltsin"
apellido = "Baltodano"

nombre_completo = nombre + " " + apellido
print("Nombre Completo:", nombre_completo)

# Nombre completo por el Operador de Formateo de String (f)
nombre_completo_otra_forma = f"{nombre} {apellido}"
print("Nombre completo por Operador:",nombre_completo_otra_forma)
# También se puede usar de diferentes manerar dentro de las llaves
uso_formateo_string =  f"{nombre[0]} {2 + 3}"
print("Uso del formateador de string",uso_formateo_string)


print(("---Métodos de String---").upper())

metodo_String = "  uso de algunos Métodos  "

# Mayúsculas
print(metodo_String.upper())
# Minúsculas
print(metodo_String.lower())
# La primera letra en mayúsculas y todo lo demás minúscula
print(metodo_String.capitalize())
# La primera letra de todas la palabras en mayúsculas
print(metodo_String.title())
# Eliminar los espacios del inicio y final del string
print(metodo_String.strip())
# Eliminar los espacios del inicio del string
print(metodo_String.lstrip())
# Eliminar los espacios del final del string
print(metodo_String.rstrip())
# usar varios métodos en un string
print(metodo_String.strip().capitalize())
# Buscar en el String y devuelve donde inicia su posición
print(metodo_String.find("us"))
# Reemplazar letras del string
print(metodo_String.replace("uso","use"))
#  Verifica si existe la/las letras/as en el string y devuelve un booleano
print("de" in metodo_String)
#  Verifica si no existe la/las letras/as en el string y devuelve un booleano
print("uso" not in metodo_String)

print(("---Secuencia de escape---").upper())
add_Comillas_En_String = "Python 'Básico'"
print("Comilla Simple:",add_Comillas_En_String)
add_Comillas_En_String = 'Python "Básico"'
print("Comillas Dobles:",add_Comillas_En_String)
add_Comillas_En_String = "Python \"Básico\""
print("Comillas Dobles Otro:",add_Comillas_En_String)
# salto de linea
salto_de_linea_En_String = "Python \n\"Básico\""
print("Salto de Linea:",salto_de_linea_En_String)
# Elimina una posición de lo que haya atrás
eliminar_En_String = "Python \b\"Básico\""
print("Eliminar lo que hay en una posición atrás:",eliminar_En_String)
