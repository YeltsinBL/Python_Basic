"""Operadores Lógicos"""

# Los operadores lógicos son: and, or y not
"""
And: todos en la evaluación son verdaderos.
Or: solo uno de la evaluación debe de ser verdadero.
Not: niega el valor de la variable que le sigue, 
    si es True lo cambia a Falso o viceversa 
    pero solo en la evaluación
"""

persona, animal, cosa = True, False, False

if not cosa and (persona and animal):
    print("Ingresó al IF")
else : print("No toda la evaluación es True")
