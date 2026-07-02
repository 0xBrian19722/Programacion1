# Un comercio quiere calcular el precio final de una compra de tela. Se ingresan precio por 
# metro y cantidad de metros (ambos mayores a 0) 
# Se sabe que: 
# ● Si el total es mayor a 150 → 10% de descuento 
# ● Si es mayor a 500 → 20% de descuento 
# ● Si no → sin descuento 
# Informar el precio final

def mostrar_precio(metros:int,precio:int)-> int:
    total = metros * precio
    descuento = 0
    if total > 150:
        descuento = total * 0.90
    elif total > 500:
        descuento = total * 0.80
    else:
        descuento = total
    return (f"El total es {descuento} $")   


metro = int(input("Ingrese los metros de la tela: "))
precio = int(input("Ingrese el precio: "))

print(mostrar_precio(metro,precio))


