my_string_variable = "Variable string"
my_int_variable = 5
my_float_variable = 5.0
my_bool_variable = True

# convertir variables
my_int_to_string_variable = str(my_int_variable)

# variables en una sola linea
name, surname, alias, age = "Guillermo", "Balto", "Chemo", 24

# imprimir variables
print(my_int_to_string_variable)
print(my_int_variable, my_string_variable, my_bool_variable)
print("Esta variable es:", my_bool_variable)
print("Cuenta la variable:", len(my_string_variable))

"""
se puede cambiar el tipo de la variable porque es de tipado débil
tener cuidado
"""

my_string_variable = 24
my_float_variable = "Cambio"

print(my_string_variable)
print(my_float_variable)
