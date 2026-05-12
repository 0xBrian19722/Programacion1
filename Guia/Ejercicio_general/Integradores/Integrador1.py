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
    tipo_producto = input("Ingrese el tipo de producto (alimento/limpieza/perfumeria): ")
    while tipo_producto not in ["alimento", "limpieza", "perfumeria"]:
        tipo_producto = input("ERROR: Ingrese nuevamente el producto válido: ")

    cantidad_de_unidades = int(input("Ingrese la cantidad de unidades (1-20): "))
    while cantidad_de_unidades < 1 or cantidad_de_unidades > 20:
        cantidad_de_unidades = int(input("ERROR: Ingrese nuevamente dentro del rango: "))
    acu_unidades += cantidad_de_unidades

    precio_unitario = int(input("Ingrese el precio unitario (>0): "))
    while precio_unitario <= 0:
        precio_unitario = int(input("ERROR: Ingrese un precio válido: "))

    forma_de_pago = input("Ingrese la forma de pago (efectivo/tarjeta/transferencia): ")
    while forma_de_pago not in ["efectivo", "tarjeta", "transferencia"]:
        forma_de_pago = input("ERROR: Ingrese una forma de pago válida: ")

    
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




   
   





      


    