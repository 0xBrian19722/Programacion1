#La división de alimentos está trabajando en un pequeño software para cargar las 
#compras de ingredientes para la cocina de Industrias Wayne. Realizar el algoritmo 
#que permita ingresar los datos de una compra de ingredientes para preparar comida 
#al por mayor. En total, sabemos que se realizarán 10 compras de ingredientes.
#Se registra por cada compra:

#1. PESO: (entre 10 y 100 kilos)
#2. PRECIO POR KILO: (mayor a 0 [cero]).
#3. TIPO VARIEDAD: (vegetal, animal, mezcla).

#Además, tener en cuenta que si compro más de 100 kilos en total tengo un 15% de 
# descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25% de descuento sobre el precio bruto.

#Se desea saber:
#A. El importe total a pagar, BRUTO sin descuento.
#B. El importe total a pagar con descuento (Solo si corresponde).
#C. Informar el tipo de alimento más caro.
#D. El promedio de precio por kilo en total.
#E. Porcentaje de variedad animal sobre el total

compra = 0
kilos = 0
total_kilos = 0
precio_total = 0
precio_con_descuento = 0
variedad_animal = 0
alimento_mas_caro = 0
sum_precio_kilo = 0
precio_mas_caro = 0

while compra < 10:

    kilos = float(input("Ingrese el peso del producto: "))
    precio_por_kilo = float(input("Ingrese el precio por kg: "))
    tipo_variedad = str(input("Ingrese si es tipo animal, vegetal o mezcla: "))

    total_kilos += kilos
    precio_total += kilos * precio_por_kilo
    sum_precio_kilo += precio_por_kilo

    if tipo_variedad == "animal":
        variedad_animal += 1

    if precio_por_kilo > precio_mas_caro:
        precio_mas_caro = precio_por_kilo
        alimento_mas_caro = tipo_variedad 

    compra += 1






if total_kilos > 100 and total_kilos <= 300:
    precio_con_descuento = precio_total * 0.85
elif total_kilos > 300:
    precio_con_descuento = precio_total * 0.75
else:
    precio_con_descuento = precio_total


promedio_precio_kilo = sum_precio_kilo / 10
porcentaje_animal = (variedad_animal / 10) * 100

# Resultados
print("A. Precio total:", precio_total)
print("B. Precio con el descuento:", precio_con_descuento)
print("C. Tipo de alimento más caro:", alimento_mas_caro)
print("D. Promedio de precio por kilo:", promedio_precio_kilo)
print("E. Porcentaje de variedad animal:", porcentaje_animal, "%")




   


















