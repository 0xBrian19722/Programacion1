# Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.  
# Se debe retornar la cadena que va entre las posiciones indicadas por los índices.  
# Si las posiciones no son válidas se debe informar.

def recibir(cadena:str,indice1:int,indice2:int)->str:
    if indice1 < 0 or indice2 > len(cadena):
        print("Fuera de rango")
    else:
       return (cadena[indice1:indice2])


print(recibir("programacion",2,6))                



