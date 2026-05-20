# Crea una función que verifique si un número dado es par o impar. La función debe 
# imprimir un mensaje indicando si el número es par o impar.

def verificar(numero:int):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es inpar")    


numero = 5
verificar(numero)