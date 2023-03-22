import math # módulo para los números
"""Número"""

entero = 3 # int
decimal = 1.2 # float
imaginario = 2 +2j # complex = 2 + 2i (raíz cuadrada de -1)

print("---OPERACIONES CON NOTACIÓN---")

entero += 2
print("Suma:", entero)
entero -= 2
print("Resta:", entero)
entero *= 2
print("Multiplicación:", entero)
entero **= 2
print("A la potencia:", entero)
entero /= 5
print("División:", entero)
entero //= 2
print("División Entera:", entero)
entero %= 2
print("Módulo-Residuo:", entero)

print("---Algunas Funciones Nativas---")
print(round(1.4)) # redondea al número
print(round(1.5)) # redondea al número
print(abs(-7)) # devuelve el valor absoluto de cualquier número: 7
print(abs(7)) # devuelve el valor absoluto de cualquier número: 7

print("---Algunas Funciones del Módulo---")
print(math.ceil(1.1)) # devuelve el número superior entero más cercano: 2
print(math.floor(1.99)) # devuelve el número inferior entero más cercano: 1
print(math.isnan(7)) # acepta solo número reales y devuelve un boolean negandolo
print(math.pow(10,2)) # eleva a la potencia
print(math.sqrt(9)) # devuelve la raíz cuadrada
