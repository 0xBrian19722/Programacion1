# Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida 
# posición y número a guardar al usuario, lo guarde en una lista en la posición 
# solicitada aleatoriamente y la retorne.  El programa principal debe invocar a la 
# función y mostrar por pantalla el retorno.

def pedir_lista():
    lista = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        posicion = int(input("Ingrese la posicion: "))
        numero = int(input("Ingrese el numero: "))
        lista[posicion] = numero
    return lista


lista = pedir_lista()
print (lista)

