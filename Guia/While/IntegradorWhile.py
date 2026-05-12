# Realizar un programa que permita que el usuario ingrese todos los números que desee. 
# Una vez finalizada la carga determinar:

# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.


corte = ""
acu_negativos = 0
acu_positivos = 0
contador_negativos = 0
contador_positivos = 0
max_positivo = 0
contador = 0
porcentaje = 0

while corte != "fin":
    ingreso = input("Ingrese un número o la palabra 'fin' para terminar: ")
    if ingreso != "fin":
        numero = int(ingreso)
        contador += 1

        if numero < 0:
            acu_negativos += numero
            contador_negativos += 1
        elif numero > 0:
            acu_positivos += numero
            contador_positivos += 1
            if numero > max_positivo:
                max_positivo = numero
    else:
        corte = "fin"


if contador_positivos > 0: 
    promedio = acu_positivos / contador_positivos
else:
    promedio = 0

if contador > 0:
    porcentaje = (contador_negativos / contador) * 100
else:
    porcentaje = 0
print (f"La suma de los numeros negativos es: {acu_negativos}")    
print (f"La suma acumulada de los numeros positivos es: {acu_positivos}")
print (f"La cantidad de los numeros negativos es: {contador_negativos}")
print (f"El promedio de los numeros positvos es: {promedio}")
print(f"El numero positivo mas grande es: {max_positivo}")
print (f"El porcentaje de los numeros negativos es: {porcentaje} %")
       



















