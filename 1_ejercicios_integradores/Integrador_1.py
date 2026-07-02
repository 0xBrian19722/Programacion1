# Cadena de supermercados  
# Consigna  
# Una cadena de supermercados desea desarrollar un sistema para registrar la venta diaria 
# de productos en distintas sucursales. Se sabe que se realizarán 25 ventas.  
# Por cada venta se deben ingresar los siguientes datos:  

# ● Tipo de producto (alimento, limpieza, perfumería)   
# ● Cantidad de unidades vendidas (entre 1 y 20)   
# ● Precio unitario (mayor a 0)   
# ● Forma de pago (efectivo, tarjeta, transferencia)   
# Se debe validar cada dato ingresado.  

# Consideraciones:  

# ● Si la cantidad total de unidades vendidas supera las 200, se aplica un descuento 
# del 10% sobre el total bruto.   
# ● Si supera las 400 unidades, el descuento será del 20%.   
# ● Las ventas pagadas en efectivo tienen un 5% de descuento adicional sobre el 
# subtotal de esa venta.  

# Se pide:  
# 1- Calcular el importe total bruto sin descuentos.  
# 2- Calcular el importe total final con todos los descuentos aplicados.  
# 3- Informar la venta más cara hecha con tarjeta.  
# 4- Calcular el promedio de precio unitario de todas las ventas.  
# 5- Informar cuál fue la forma de pago más utilizada.

def validar_opciones(msj:str,msj1:str,msj2:str)-> str:
    ingreso = input(f"Ingrese: {msj}, {msj1}, {msj2}: ")
    while ingreso != msj and ingreso != msj1 and ingreso != msj2:
        ingreso = input(f"Error, ingrese {msj}, {msj1}, {msj2}: ")
    return ingreso

def validar_cantidad(msj:str,num:int,num1:int) -> int:
    ingreso = int(input(f"{msj} ({num}-{num1}): "))
    while ingreso < num or ingreso > num1:
        ingreso = int(input(f"ERROR: {msj}, ({num}-{num1}): "))
    return ingreso

def validar_unitario(msj:str,num:int):
    ingreso = int(input(f"{msj}, (<= {num}): "))
    while ingreso <= num:
        ingreso = int(input(f"ERROR: {msj}, (<= {num}): "))
    return ingreso

ventas = 0
acu_unidades = 0
total_bruto = 0
total_con_descuentos = 0
cont_efectivo = 0
cont_tarjeta = 0
cont_transferencia = 0
venta_mas_cara_tarjeta = 0
suma_precios_unitarios = 0

while ventas < 25:
    tipo_producto = validar_opciones("alimento","limpieza","verduleria")

    cantidad_de_unidades = validar_cantidad("Ingrese la canitdad: ",1,20)
    acu_unidades += cantidad_de_unidades

    precio_unitario = validar_unitario("Ingrese el precio unitario",0)

    forma_de_pago = validar_opciones("efectivo","tarjeta","transferencia")
    

    
 
    
    subtotal = cantidad_de_unidades * precio_unitario          #TOTAL POR VUELTA
    total_bruto += subtotal

    
    if forma_de_pago == "efectivo":
        subtotal *= 0.95
        cont_efectivo += 1
    elif forma_de_pago == "tarjeta":
        cont_tarjeta += 1
        if subtotal > venta_mas_cara_tarjeta:
            venta_mas_cara_tarjeta = subtotal
    else:
        cont_transferencia += 1

    total_con_descuentos += subtotal
    suma_precios_unitarios += precio_unitario
    ventas += 1


if acu_unidades > 400:
    total_neto = total_con_descuentos * 0.80
elif acu_unidades > 200:
    total_neto = total_con_descuentos * 0.90
else:
    total_neto = total_con_descuentos

promedio = suma_precios_unitarios / ventas

if cont_efectivo >= cont_tarjeta and cont_efectivo >= cont_transferencia:
    pago_mas_utilizado = "efectivo"
elif cont_tarjeta >= cont_efectivo and cont_tarjeta >= cont_transferencia:
    pago_mas_utilizado = "tarjeta"
else:
    pago_mas_utilizado = "transferencia"

print("Total bruto sin descuentos:", total_bruto)
print("Total final con descuentos:", total_neto)
print("Venta más cara con tarjeta:", venta_mas_cara_tarjeta)
print("Promedio de precios unitarios:", promedio)
print("Forma de pago más utilizada:", pago_mas_utilizado)

   
        







def valid():
    nombre = input("Ingrese: ")
    while len(nombre) == 0:
            nombre = input("Error: ")
    return nombre        
    
        
            

