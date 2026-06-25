# Enunciado 1:
# Realizar un programa que solicite al usuario ingresar 10 números enteros.
#  Luego, el programa debe:
# •	Mostrar la suma total de los números ingresados. 
# •	Informar cuántos números son pares. 
# •	Indicar cuál fue el número mayor.

suma = 0
npar = 0
flag = False


for i in range(10):
     numero = int((input("Ingrese 10 numeros: ")))
     suma = suma + numero

     if numero % 2 == 0:
          npar += 1
     if flag == False:
          nmax = numero     
     elif numero > nmax:
          nmax = numero     






print("La suma total es: ", suma)
print("La cantidad de numeros pares es: ", npar)
print("El mayor numero ingresado es: ", nmax)







    
    



