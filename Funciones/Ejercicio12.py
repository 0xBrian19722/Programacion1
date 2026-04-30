# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
# Por defecto es del 1 al 10.

def no_es_domingo(num1:int):
     acumulador = 0
     for i in range(1, num1 + 1):
      acumulador += i
      print (acumulador)

no_es_domingo(8)
       
# for i in range(1, 10):
#     print(i)


     