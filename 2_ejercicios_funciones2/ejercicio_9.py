# Crear una función que imprima la tabla de multiplicar de un número recibido como 
# parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir 
# el rango de multiplicación. Por defecto es del 1 al 10. 

def calcular_tabla(num:int, inicio:int=1, fin:int=10) -> int:
    for i in range(inicio, fin+1):   
        print(f"{num} x {i} = {num * i}")


calcular_tabla(2, 1, 6)      


