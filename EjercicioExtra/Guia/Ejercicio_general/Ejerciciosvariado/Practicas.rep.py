# Pide números hasta que el usuario escriba “fin”.

# Guarda en una lista y luego muestra:

# El mayor

# El menor

# El promedio

flag = 0
mayor = 0
menor = 0
suma = 0

for i in range(3):
    n = int(input("Ingrese un número: "))
    suma = suma + n

    if flag == 0:   # primera vez
        mayor = n
        menor = n
        flag = 1
    else:           # siguientes veces
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n

promedio = suma / 3

print("El mayor es:", mayor)
print("El menor es:", menor)
print("El promedio es:", promedio)