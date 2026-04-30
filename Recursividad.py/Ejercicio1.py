def suma_acumulada(n:int):
    if n <= 0:              # caso base
        return 0
    else:                   # caso recursivo
        return n + suma_acumulada(n-1)

print(suma_acumulada(4))  