# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

print("Ingrese un numero, puede cancelarlo ingresando el numero 0")

suma_contador = 0
acu_producto = 1
flag = True
numero = 0

while flag:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
       flag = False
    if numero > 0:
      suma_contador += numero
    elif numero <= -1:
     acu_producto *= numero
print(f"La suma de los numeros positivos es: {suma_contador}, y el producto de los numeros negativos es {acu_producto}")
