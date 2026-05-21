# Ejercicio 1: Desarrollar una función que reciba una letra y una cadena. 
# Debe retornar las veces que la letra está incluida en el texto.

def recibir_cadena(letra: str, cadena: str) -> int:
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == letra:   
            contador += 1
    return contador  


print(recibir_cadena("a", "banana"))  # 3
