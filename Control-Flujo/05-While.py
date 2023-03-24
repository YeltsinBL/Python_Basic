"""While"""

'''
También es un Loop al igual que el For 
pero se ejecuta siempre y cuando se cumpla la condición.
Al igual que en el For, el break corta la ejecución 
y no se utiliza el ELSE al final
'''

numero = 1
while numero < 10:
    print(numero)
    numero *= 2
    if numero == 4:
        break

"""While Infinitos"""

while True:
    comando = input("$ ")
    if comando.lower() == "salir":
        break
