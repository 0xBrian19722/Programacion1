# Realizar una función recursiva que calcule la potencia de un número:


def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:              
        return 1
    else:                           
        return base * calcular_potencia(base, exponente - 1)
    

print(calcular_potencia(3,3))    