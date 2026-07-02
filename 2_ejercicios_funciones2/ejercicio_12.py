# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def ingresar_cadena() -> str:
    cadena = input("Ingrese una cadena de texto: ")
    return cadena

texto = ingresar_cadena()
print("La cadena ingresada es: ", texto)