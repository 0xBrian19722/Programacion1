def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
     return "ERROR: No se puede dividir por cero"
    return a / b

def menu():
   print ("Seleccione una operación:")
   print ("1. Suma")
   print ("2. Resta")
   print ("3. Multiplicar")
   print ("4. Dividir")
   print ("5. Salir")

def cuenta_regresiva(n):
    if n <= 0:
        print ("Despegue!")
    else:
        print(n)
        cuenta_regresiva (n -1)








   