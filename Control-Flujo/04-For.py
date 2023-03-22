"""FOR"""

'''
Sirve para poder iterar, buscar y más dentro de una lista y/o string
El ELSE al final del For se debe de utilizar con un Break
porque al termina de recorrer la lista lo ejecutará igualmente y 
con el Break termina la secuencia y no lo ejecuta
'''

buscar = 2

# el Range es un iterable
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado")
        break
else:
    print("No encontrado")
