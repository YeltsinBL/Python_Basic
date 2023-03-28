inicio = 8

def sumar():
    """acceder al una variable global"""
    global inicio # para acceder a la variable se debe de usar la palabra reservada global seguido del nombre de la variable
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
