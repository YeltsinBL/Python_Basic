numeros = [1, 2, 9, 6, 8, 3, 7, 5]

# Utilizando Sort
# Ordena de forma ascendente
numeros.sort()
# Ordena de forma descendente
numeros.sort(reverse=True)
print(numeros)
letras = ["a", "c","e","b","d"]
letras.sort()
letras.sort(reverse=True)
print(letras)

# Utilizando Sorted
numeros2 = sorted(numeros)
numeros2 = sorted(numeros, reverse=True)
print(numeros2)

# Ordenar Lista de Lista por el valor
usuario = [["Python", 4], ["Ejercicio", 1], ["Ordenar", 5]]
usuario.sort()
print(usuario)
# Ordenar de forma ascendente la Lista de Lista por el número
def ordenar(elemento):
    """recibe un iterable para devolver los elementos de la posición 1"""
    return elemento[1]
usuario.sort(key=ordenar)
print(usuario)
# Ordenar de forma descendente la Lista de Lista por el número usando Lambda
usuario.sort(key=lambda elemento: elemento[1], reverse= True)
print(usuario)
