# Crear una función que reciba como parámetro una cadena y determine si la
# misma es o no un palíndromo. Deberá retornar un valor booleano indicando
# lo sucedido

def buscar_palindromo(cadena: str) -> bool:
    
    palindromo = True
    
    for i in range(len(cadena)):
        if cadena[i] != cadena[len(cadena) - 1 - i]:
            palindromo = False   
    return palindromo


print(buscar_palindromo("neuquen"))   
   
