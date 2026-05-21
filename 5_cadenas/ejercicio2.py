# Desarrollar una función que reciba una cadena y dos índices.  
# Se debe retornar la cadena que va entre las posiciones indicadas por los índices.  
# Si las posiciones no son válidas se debe informar. 

def recibir_cadena(cadena:str, inicio:int, fin:int):

    if inicio < 0 or fin > len(cadena) or inicio >= fin:
        print("Índices no válidos")
    else:
        return cadena[inicio:fin]



print(recibir_cadena("programacion", 0, 7))   
