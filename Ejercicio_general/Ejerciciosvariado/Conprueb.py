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
# Se pide: 
# a. Calcular el costo total bruto de producción. Luego, calcular el costo total final con 
# descuentos e impuestos (informar qué descuento y/o qué recargo se le aplica al precio). 
# b. Cuál fue el costo por metro del lote de algodón más corto en cantidad producida 
# (metros). 
# c. ¿Qué porcentaje de los lotes fue de mezcla?. 
# d. Se produjeron más lotes de primera o de genérica? 
# e. Informar cuántos lotes son de calidad primera.

seguir = "si"
costo_total = 0
cantidad_metros = 0 

while seguir == "si":
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
    seguir = input("Desea ingresar otro lote? si/no: ")

if calidad == "primera":
    descuento = costo_total * 0.10  
else:    descuento = 0      
if costo_por_metro > 50:
    impuesto = costo_total * 0.10  
else:    impuesto = 0       
if cantidad_metros > 30000:
    recargo = costo_total * 0.10  
else:    recargo = 0    
costo_total_bruto = cantidad_metros * costo_por_metro
costo_total_final = costo_total_bruto - descuento + impuesto + recargo   

print("El costo total bruto de producción es: ", costo_total_bruto)
print("El costo total final con descuentos e impuestos es: ", costo_total_final)    
print("El descuento aplicado es: ", descuento)
print("El impuesto aplicado es: ", impuesto)    
print("El recargo aplicado es: ", recargo)
print("El costo por metro del lote de algodón más corto en cantidad producida es: ", costo_por_metro)
print("El porcentaje de los lotes que fue de mezcla es: ", (cantidad_metros / costo_total_bruto) * 100)
print("Se produjeron más lotes de primera o de genérica? ", tipo_calidad)
print("La cantidad de lotes de calidad primera es: ", tipo_calidad)     




# 1 git it-  2 crear repositorio de github   (nota directorio)

