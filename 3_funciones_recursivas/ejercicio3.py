# Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_digitos(numero: int)->int:
    if numero < 10:                 
        return numero
    else:                            
        return numero % 10 + sumar_digitos(numero // 10)
    
print(sumar_digitos(20))
    
