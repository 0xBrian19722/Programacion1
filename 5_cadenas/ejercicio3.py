# Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.  
# Se debe retornar el caracter en la posición indicada por el número si ésta es válida.  
# **IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el 
# <número de caracteres> - 1.

def char_at():
    cadena = input("Ingrese una palabra: ")
    num = int(input("Ingrese un numero: "))
    if num > len(cadena):
        print("Fuera de rango")
    else:
        return cadena[num]  
        

print(char_at())