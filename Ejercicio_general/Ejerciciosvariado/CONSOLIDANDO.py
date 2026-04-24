# Consigna 2 
# Una fábrica textil registra la producción de lotes de tela en un día de trabajo. No hay un total 
# de registros mínimo ni se sabe cuántos habrá en total. 

# Por cada lote se ingresan: 
# ● Tipo de tela (algodón, poliéster, mezcla) 
# ● Cantidad producida en metros (entre 100 y 5000) 
# ● Costo por metro (mayor a 0) 
# ● Calidad (primera, generica) 


# Todos los datos deben ser validados. 

# Consideraciones: 
# ● Los productos de calidad premium tienen un descuento del 10% sobre su precio 
# bruto 
# ● Si el costo por metro promedio de los lotes es mayor a 50, se aplica un impuesto 
# adicional del 10% sobre el total bruto. 
# ● Si la producción total supera los 30000 metros, se aplica un recargo del 10% en 
# concepto de impuestos.
# 
#  
# Se pide: 
# a. Calcular el costo total bruto de producción. Luego, calcular el costo total final con 
# descuentos e impuestos (informar qué descuento y/o qué recargo se le aplica al precio). 
# b. Cuál fue el costo por metro del lote de algodón más corto en cantidad producida 
# (metros). 
# c. ¿Qué porcentaje de los lotes fue de mezcla?. 
# d. Se produjeron más lotes de primera o de genérica? 
# e. Informar cuántos lotes son de calidad primera.

otro_lote = "o"

algodon = "a"
poliester = "b"
mezcla = "c"
sum_tipoT = 0

while otro_lote == "o":

 tela = input("Ingresar tipo de tela: a: algodon, b: poliester, c: mezcla: ")
 match tela:
    case "a":
        tipo_tela = "algodón"
    case "b":
        tipo_tela = "poliéster"
    case "c":
        tipo_tela = "mezcla"
 
 
 cantidad_metros = float(input("Ingrese la cantidad de metros producida (100 - 5000): "))
 costo_por_metro = float(input("Ingrese el costo por metro: "))
 calidad = input("p = primera o g = generica: ")
match calidad:
    case "p":
        tipo_calidad = "primera"
    case "g":
        tipo_calidad = "genérica"


otro_lote = input("Desea ingresar otro lote? (s = si o n = no): ")