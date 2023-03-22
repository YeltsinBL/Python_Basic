"""IF-ELIF-ElSE"""

edad = 24

if edad > 60:
    print("Accedió al adulto mayor")
elif edad >17:
    print ("Ya es mayor de edad")
else: print("Aún es menor de edad")


"""Operador Termario"""

mensaje = "Es mayor de edad" if edad > 17 else "Es menor de edad"
print(mensaje)