# Consigna: 
# Un comercio quiere calcular el precio final de una compra de tela. Se ingresan precio por 
# metro y cantidad de metros (ambos mayores a 0) 
# Se sabe que: 
# ● Si el total es mayor a 150 → 10% de descuento 
# ● Si es mayor a 500 → 20% de descuento 
# ● Si no → sin descuento 
# Informar el precio final


def comercio_tela(precio:int, metro:int):
    
    total_bruto = precio * metro
    if total_bruto > 500:
        final = total_bruto * 0.80
    elif total_bruto > 150:
        final = total_bruto * 0.90
    else:
        final = total_bruto
    print (f"El precio total es {final}")



comercio_tela(3, 100 )