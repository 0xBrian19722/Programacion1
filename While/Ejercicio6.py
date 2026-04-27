# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
#  Mostrar la suma y el promedio por pantalla.

contador = 0
acu_numero = 0

while contador < 5:
    numero = int(input("Ingrese un numero: "))
    acu_numero += numero
    contador += 1

total = acu_numero / 5

print (f"La suma de los numeros ingresados es: {acu_numero}, y el promddio es: {total}")

