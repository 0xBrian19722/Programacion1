# Enunciado 2:
# Realizar un programa que pida al usuario un número entero positivo.
#  Luego, utilizando un for, mostrar:
# •	Todos los números desde 1 hasta ese número. 
# •	La suma de todos esos números. 
# •	El promedio de los números mostrados


num = int(input("ingrese un numero entero positivo: "))
total = 0
contador = 0

print ("Todos los numeros son: ")
for i in range (num, 0, -1):
 total += i
 contador += 1
 print(i)

promedio = total / contador


print ("La suma de todos los numeros en el rango", num, "y el 1 es: ", total )
print ("El promedio es: ", promedio)






