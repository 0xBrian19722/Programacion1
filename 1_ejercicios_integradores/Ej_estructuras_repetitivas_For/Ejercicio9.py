contador = 0

num = int(input("Ingrese un numero: "))
for i in range(1,num):
    if i % 2 == 0:
        contador += 1

print (f"La cantidad de divisores es: {contador}")





