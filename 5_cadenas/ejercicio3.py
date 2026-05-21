# Desarrollar una función “char_at” que recibe una cadena y un número.  
# Se debe retornar el caracter en la posición indicada por el número si ésta es válida.  
# **IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el 
# <número de caracteres> - 1.


def char_at(cadena:str,indice:int):
    if indice < 0 or indice >= len(cadena):
        print ("Índice no válido")
    else:
        return cadena[indice]


print(char_at("hola", 2))   
