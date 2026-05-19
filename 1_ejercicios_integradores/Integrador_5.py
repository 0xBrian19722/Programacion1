'''
Ejercicio 2: Registro de alquiler de vehículos 
Una empresa registra alquileres de autos durante un período. No se sabe cuántos registros 
habrá. 
Por cada alquiler se ingresan: 
● Nombre del cliente 
● Tipo de vehículo (auto, camioneta, moto) 
● Cantidad de días de alquiler (entre 1 y 30) 
● Precio por día (mayor a 0) 
● Kilómetros recorridos (entre 0 y 5000) 
● Forma de pago (efectivo, tarjeta, transferencia) 
● Cliente frecuente (sí/no) 
Validar todos los datos. 
Consideraciones: 

● Si el cliente es frecuente, tiene un descuento del 15% sobre el total del alquiler. 
● Si el total de kilómetros acumulados supera los 20000 km, se aplica un recargo del 
10% sobre el total bruto general. 
● Las camionetas tienen un recargo del 20% sobre su costo individual. 
Se pide: 
a. Calcular el importe total bruto y el total final. 
b. El tipo de vehículo con mayor cantidad de alquileres. 
c. El nombre del cliente que más días alquiló en total. 
d. El promedio de kilómetros recorridos. 
e. Qué tipo de vehículo acumuló más kilómetros. 
f. Cuántos alquileres fueron pagados con tarjeta. 
g. El alquiler de mayor importe (indicar cliente y monto).
'''

def pedir_dato(mensaje:str):
    nombre = input(f"{mensaje}: ")
    return nombre

def pedir_validacion(mensaje, mensaje1, mensaje2, mensaje3):
    validacion = input(f"{mensaje}, ({mensaje1}, {mensaje2}, {mensaje3}): ")
    while validacion != mensaje1 and validacion != mensaje2 and validacion != mensaje3:
        validacion = input(f"Error, {mensaje} ({mensaje1}, {mensaje2}, {mensaje3}): ")
    return validacion

def pedir_validacion_cliente(mensaje, mensaje1, mensaje2):
    validacion = input(f"{mensaje}, ({mensaje1}, {mensaje2}): ")
    while validacion != mensaje1 and validacion != mensaje2:
        validacion = input(f"Error, {mensaje} ({mensaje1}, {mensaje2}): ")
    return validacion

def pedir_int(min, max, mensaje):
    dato = int(input(f"{mensaje}, entre ({min} y {max}): "))  
    while dato < min or dato > max:
        dato = int(input(f"Error!, {mensaje} entre {min} y {max}: "))  
    return dato

def pedir_precio(min, mensaje):
    dato = int(input(f"{mensaje}, mayor a {min}: "))  
    while dato <= min:
        dato = int(input(f"Error!, {mensaje} mayor {min}: "))  
    return dato

def pedir_corte(mensaje, afirmativo, negativo):
    global bandera
    corte = input(f"{mensaje} ({afirmativo}/{negativo}): ")
    while corte != afirmativo and corte != negativo:
        corte = input(f"Error, {mensaje} ({afirmativo}/{negativo}): ")
    if corte == negativo:
        print("Fin de la carga...")
        bandera = False
    else:
        bandera = True


bandera = True
contador_auto = 0
contador_camioneta = 0
contador_moto = 0
contador_tarjeta = 0
acumulador_km = 0
contador_vueltas = 0
acum_km_auto = 0
acum_km_moto = 0
acum_km_camioneta = 0
dias_max = 0
nombre_cliente_dias = ""
alquiler_mayor_importe = 0
nombre_cliente_mayor_importe = ""
total_bruto_general = 0
total_final_general = 0

while bandera: 
    contador_vueltas += 1
    nombre = pedir_dato("Ingrese el nombre: ")
    vehiculo = pedir_validacion("Ingrese el vehículo", "auto", "camioneta", "moto")
    dias = pedir_int(1, 30, "Ingrese los días")
    precio_por_dia = pedir_precio(0, "Ingrese el precio por día")
    kilometros_recorridos = pedir_int(0, 5000, "Ingrese los kilómetros recorridos")
    forma_de_pago = pedir_validacion("Ingrese la forma de pago", "efectivo", "tarjeta", "transferencia")
    cliente_frecuente = pedir_validacion_cliente("Es cliente frecuente?", "si", "no")

    acumulador_km += kilometros_recorridos

    if dias > dias_max:
        dias_max = dias
        nombre_cliente_dias = nombre

    if forma_de_pago == "tarjeta":
        contador_tarjeta += 1

    if vehiculo == "auto":
        contador_auto += 1
        acum_km_auto += kilometros_recorridos
    elif vehiculo == "camioneta":
        contador_camioneta += 1
        acum_km_camioneta += kilometros_recorridos
    else:
        contador_moto += 1    
        acum_km_moto += kilometros_recorridos
    
    total_bruto_alquiler = dias * precio_por_dia

    
    if vehiculo == "camioneta":
        total_bruto_alquiler = total_bruto_alquiler * 1.20

   
    if cliente_frecuente == "si":
        total_bruto_alquiler = total_bruto_alquiler * 0.85

    total_bruto_general += dias * precio_por_dia
    total_final_general += total_bruto_alquiler


    if total_bruto_alquiler > alquiler_mayor_importe:
        alquiler_mayor_importe = total_bruto_alquiler
        nombre_cliente_mayor_importe = nombre

    pedir_corte("Ingresar otro cliente?", "si", "no")


if acumulador_km > 20000:
    total_final_general = total_final_general * 1.10


if contador_auto >= contador_camioneta and contador_auto >= contador_moto:
    vehiculo_mas_usado = "auto"
elif contador_moto >= contador_auto and contador_moto >= contador_camioneta:
    vehiculo_mas_usado = "moto"
else:
    vehiculo_mas_usado = "camioneta"


promedio_km = acumulador_km / contador_vueltas


if acum_km_moto >= acum_km_auto and acum_km_moto >= acum_km_camioneta:
    vehiculo_mas_km = "moto"
elif acum_km_auto >= acum_km_moto and acum_km_auto >= acum_km_camioneta:
    vehiculo_mas_km = "auto"
else:
    vehiculo_mas_km = "camioneta"


print(f"A) Importe total bruto: {total_bruto_general}, total final: {total_final_general}")  
print(f"B) Vehículo más alquilado: {vehiculo_mas_usado}")
print(f"C) Cliente con más días: {nombre_cliente_dias} ({dias_max} días)")
print(f"D) Promedio de kilómetros recorridos: {promedio_km}")
print(f"E) Vehículo con más kilómetros acumulados: {vehiculo_mas_km}")
print(f"F) Alquileres pagados con tarjeta: {contador_tarjeta}")
print(f"G) Alquiler de mayor importe: {alquiler_mayor_importe} (Cliente: {nombre_cliente_mayor_importe})")





# b. El tipo de vehículo con mayor cantidad de alquileres. 
# c. El nombre del cliente que más días alquiló en total. 
# d. El promedio de kilómetros recorridos. 
# e. Qué tipo de vehículo acumuló más kilómetros. 
# f. Cuántos alquileres fueron pagados con tarjeta. 
# g. El alquiler de mayor importe (indicar cliente y monto).
# '''
    
