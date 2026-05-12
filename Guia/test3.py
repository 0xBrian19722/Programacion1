# def determinar_palindromo(palabra) ->bool:
#     if palabra == palabra:
#         print(True)
#     else:
#         print(False)    
    


# palabra = input("Ingrese una palabra: ")
# determinar_palindromo(palabra)



def determinar_palindromo(palabra: str) -> bool:
    palabra = palabra.lower().replace(" ", "")
    
    # Recorremos la palabra desde ambos extremos
    for i in range(len(palabra)):
        # Comparamos el carácter en posición i con el simétrico desde el final
        if palabra[i] != palabra[len(palabra) - 1 - i]:
            return False
    return True

# Ejemplo de uso
palabra = input("Ingrese una palabra: ")
print(determinar_palindromo(palabra))