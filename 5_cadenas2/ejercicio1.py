# Crear una función que reciba como parámetro una cadena y determine la
# cantidad de vocales que hay de cada una (individualmente). La función
# retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
# la cantidad.


def contar_vocales(cadena: str) -> list:
    
    resultado = [["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0]]

    for caracter in cadena:
        if caracter == "a" or caracter == "A":
            resultado[0][1] += 1
        elif caracter == "e" or caracter == "E":
            resultado[1][1] += 1
        elif caracter == "i" or caracter == "I":
            resultado[2][1] += 1
        elif caracter == "o" or caracter == "O":
            resultado[3][1] += 1
        elif caracter == "u" or caracter == "U":
            resultado[4][1] += 1

    return resultado

palabra = "murcielaguito"
print(contar_vocales(palabra))