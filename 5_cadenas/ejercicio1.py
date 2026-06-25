# Ejercicio 1: Desarrollar una función que reciba una letra y una cadena. 
# Debe retornar las veces que la letra está incluida en el texto.

def recibir():
    letra = input("Escriba una letra: ")
    cadena = input("Escriba una palabra: ")
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == letra:
            contador += 1
    return {f"Las veces que la '{letra}' se encuentra en '{cadena}' es {contador}"} 



print(recibir())
