# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

numero = int(input("Ingrese un numero: "))
num_max = numero
num_min = numero
contador = 1


while contador < 10:
 numero = int(input("Ingrese un numero: "))
 if numero < num_max:
  num_max = numero
 if numero > num_min:
  num_min = numero
 contador += 1
print(f"El máximo es {num_max} y el mínimo es {num_min}")  



   
 

    




   








