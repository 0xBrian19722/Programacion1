# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def primo():
    numero = int(input("Ingrese un numero: "))
    if numero <= 1:
        return "false"
    for i in range(2, numero):
        if numero % i == 0:
            return "false"
    return "true"

input(primo())

