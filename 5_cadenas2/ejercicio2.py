#  Crear una función que reciba una cadena y un caracter. La función deberá
# devolver el índice en el que se encuentre la primera incidencia de dicho
# caracter, o-1 en caso de que no esté



def buscar_indice(cadena: str, caracter: str) -> int:
  
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i  
        

print(buscar_indice("murcielaguito", "a")) 


 
