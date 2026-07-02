#  Crear una función que reciba como parámetro una cadena y suprima los
# caracteres repetidos.
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”


def suprimir_repetidos(cadena: str):
    nueva_cadena = ""
    for i in range(len(cadena)):
        caracter = cadena[i]
        repetido = False

        for j in range(len(nueva_cadena)):
            if nueva_cadena[j] == caracter:
                repetido = True
        if repetido == False:
            nueva_cadena = nueva_cadena + caracter
    return nueva_cadena

print(suprimir_repetidos("Hooola"))      
    

        

        

