# Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en 
# un rango determinado pasado por parámetro “desde”-“hasta”.

def pedir_numero(numero, num:int, num2:int):
    print(f"El numero ingresado es {numero}")
    if numero > num and numero <num2:
        print("Esta dentro del rango")
    else:
        print("Fuera del rango")    

pedir_numero(11, 0, 10)
  




