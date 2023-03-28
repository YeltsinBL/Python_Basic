"""Función con \"X\" parámetros-argumentos 
    pero pasandole un nombre de cada parámetro"""

def get_product(**datos):
    """Cuando hay dos asteriscos en el parámetro, significa que 
        se utilizará el 'KW' (keyWord-palabra clave) del parámetro
    """
    print(datos) # este parámetro será un diccionario de datos: {nombre:valor}
    print(datos["id"], datos["nombre"]) # acceder a los datos del diccionario


 # para utilizar esta función, se debe de dar un nombre al parámetro
 # sino no funcionará
get_product(id=21, nombre="Python", desc="Función usando KWargs.")
