def buscar_indice(cadena: str, caracter: str) -> int:
  
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i  
        

print(buscar_indice("murcielaguito", "a")) 


 
