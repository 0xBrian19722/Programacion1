# Crear una función que le solicite al usuario el ingreso de un número flotante y lo 
# retorne. 

def ingresar_numero():
    numero = float(input("Ingrese un numero 'float': "))
    return numero

numero = ingresar_numero()

print(f"El numero ingresado es: {numero}")