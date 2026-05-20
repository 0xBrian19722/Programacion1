# Define una función que encuentre el máximo de tres números. La función debe 
# aceptar tres argumentos y devolver el número más grande. 

def buscar_maximo(n1:int,n2:int,n3:int) -> int:
    numero_max = 0
    if numero_max < n1:
        numero_max = n1
        if numero_max < n2:
            numero_max = n2
            if numero_max < n3:
                numero_max = n3
    return numero_max            

print(buscar_maximo(5, 7, 12))

