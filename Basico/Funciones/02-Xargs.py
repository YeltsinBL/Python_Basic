"""Función con \"X\" parámetros-argumentos """

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
