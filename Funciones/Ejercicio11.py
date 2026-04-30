# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
# muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
# La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range (2, numero):
        if numero % i == 0:
         return False
    return True


def mostrar_primos(hasta):
   contador = 0
   for num in range(2, hasta +1):
      if es_primo(num):
         print(num)
         contador = contador + 1
   return contador 

def menu():
   n = int(input("Ingrese un numero: "))   
   cantidad = mostrar_primos(n)
   print(f"Cantidad de primos encontrados {cantidad}") 

menu()   


    

   