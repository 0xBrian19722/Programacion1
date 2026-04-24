n = int(input("Ingrese un número: "))
contador = 0

for num in range(2, n + 1):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)
        contador = contador + 1

print("Cantidad de primos encontrados:", contador)



