# Enunciado 3:
# Realizar un programa que solicite al usuario ingresar 5 números enteros (uno por uno).
# Por cada número ingresado, el programa debe:
# •	Determinar si es positivo, negativo o cero. 
# •	Contar cuántos números positivos, negativos y ceros se ingresaron. 
# Al finalizar, informar:
# •	La cantidad de números positivos. 
# •	La cantidad de números negativos. 
# •	La cantidad de ceros. 
# •	El promedio de los números positivos.

num_positivo = 0
num_negativo = 0
cero = 0
total = 0


for i in range(5):
    num = int(input("ingrese un numero: "))
    total = total + num
    if num > 0:
       num_positivo += 1
    elif num == 0:
       cero += 1
    elif num < 0:
        num_negativo += 1

promedio = total / 5        

print ("La cantidad de numeros positivos son: ", num_positivo)        
print ("La cantidad de numeros negativos son: ", num_negativo)        
print ("La cantidad de ceros son: ", cero) 
print ("El promedio de los datos ingresados es: ", promedio)



          
            


