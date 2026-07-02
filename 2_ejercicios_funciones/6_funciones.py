# Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor 
# solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a 
# dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado 
# por pantalla.  Atención: pueden reutilizarse funciones ya creadas.

def pedir_numero():
    num = int(input("Ingrese un numero: "))
    return num
def realizar_descuento(numero:int):
    descuento = numero * 0.95
    return descuento


bandera = True

numero1 = pedir_numero()
while bandera:
    if numero1 < 10 or numero1 > 100:
        numero1 = int(input("Error, Ingrese un numero dentro del rango (10 y 100): "))
    else:
        numero1 = realizar_descuento(numero1) 
        print(f"El numero ingresado con el descuento es: {numero1}")
        bandera = False   







