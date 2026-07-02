# Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2 
# los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la 
# variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar), realice 
# la operación de dichos valores a través de una función. Mostrar el resultado por 
# pantalla. 


def pedir_numero():
    num = int(input("Ingrese un numero: "))
    return num

def validar(num: int) -> int:
    bandera = True
    while bandera:
        if num < 10 or num > 100:
            num = int(input("Error, Ingrese un numero dentro del rango (10 y 100): "))
        else:
            bandera = False
    return num

def sumar_restar(numero1:int,numero2:int):
    bandera = True
    while bandera:
        operacion = input("Ingrese una opcion: 's' para sumar o 'r' para restar: ")
        while operacion != "s" and operacion != "r":
            operacion = input("Error, ingrese una operacion valida: ")
        if operacion == "s":
            resultado = numero1 + numero2
        elif operacion == "r":
            resultado = numero1 - numero2
        return resultado    
                          



numero1 = pedir_numero()
numero1 = validar(numero1)
numero2 = pedir_numero()
numero2 = validar(numero2)

print("El resultado es: ", sumar_restar(numero1,numero2))