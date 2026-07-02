#Aplicar descuento si el total supera 100

total= 0

a = int(input("ingrese el precio del 1er producto: "))
b = int(input("Ingrese el precio del 2do producto: "))

total = a + b

if total >= 100:
    total = total * 0.75
    print("Se aplica el descuenta")
else: 
    print("No hay descuenta ameo")

print ("El precio total  es: ", total)














    
   

