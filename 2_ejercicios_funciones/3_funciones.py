# Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La 
# función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el 
# programa principal realizando la invocación o llamada. 

def buscar_par():
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        print("True")
    else:
        print("False")

buscar_par()
