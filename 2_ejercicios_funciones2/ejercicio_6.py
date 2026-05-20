# Diseña una función que calcule la potencia de un número. La función debe recibir la 
# base y el exponente como argumentos y devolver el resultado. 

def calcular_pontecia(numero:int,base:int):
    potencia = (numero ** base)
    return (f"La potencia es: {potencia}")

print(calcular_pontecia(2, 2))