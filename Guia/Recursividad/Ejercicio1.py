def suma_acumulada(n:int):
    if n <= 0:              
        return 0
    else:                   
        return n + suma_acumulada(n-1)

print(suma_acumulada(4))  