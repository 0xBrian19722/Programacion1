# Consigna 1 

# Nos ingresan una cantidad indeterminada de estadías de  vacaciones, validando los datos 
# ingresados: 
# nombre del titular , 
# lugar ( “Puerto Madryn”, “Villa Gessel” o “Córdoba”), 
# temporada(“alta”, “baja”), 
# cantidad de días que durará el viaje. 
# importe del viaje 
# altura del pasajero 
# peso del pasajero 
# sexo pasajero (F o M o NB) 
# Viaja con equipaje de mano? 
# paga con mercado , tarjeta o efectivo 

# 1)  

# a- cantidad de personas que viajan en cada temporada 
# b- el peso acumulado de todos los que viajan a villa gesell 
# c-
# d- la suma de todos los importes



continuar = "si"
pasajeros = 0
temporada_alta = 0
temporada_baja = 0
peso_acumulado_villa_gessel = 0
importe_total = 0

while continuar == "si":
    nombre = input("Ingrese el nombre del titular: ")
    pasajeros += 1

    lugar = input("Que lugar es el viaje? Puerto Madryn, Villa Gessel o Córdoba: ")
    while lugar != "Puerto Madryn" and lugar != "Villa Gessel" and lugar != "Córdoba":
        lugar = input("Error, ingrese un lugar valido: Puerto Madryn, Villa Gessel o Córdoba: ")

    peso_pasajero = float(input("Cual es el peso del pasajero?: "))
    if lugar == "Villa Gessel":
        peso_acumulado_villa_gessel += peso_pasajero

    temporada = input("Temporada alta o baja?: ")
    while temporada != "alta" and temporada != "baja":
        temporada = input("Error, ingrese una temporada valida: alta o baja: ")
    if temporada == "alta":
        temporada_alta += 1
    else:
        temporada_baja += 1

    dias = int(input("Cuantos dias dura el viaje?: "))
    importe_del_viaje = float(input("Cual es el importe del viaje?: "))
    importe_total += importe_del_viaje

    altura_pasajero = float(input("Cual es la altura del pasajero?: "))
    sexo_pasajero = input("Que sexo es?: f: Femenino m: Masculino nb: No Binario: ")
    while sexo_pasajero != "f" and sexo_pasajero != "m" and sexo_pasajero != "nb":
        sexo_pasajero = input("Error, ingrese un sexo valido: f: Femenino m: Masculino nb: No Binario: ")

    equipaje_de_mano = input("Viaja con equipaje de mano? si o no: ")
    while equipaje_de_mano != "si" and equipaje_de_mano != "no":
        equipaje_de_mano = input("Error, ingrese una respuesta valida: si o no: ")

    metodo_de_pago = input("Paga con tarjeta o efectivo: ")
    while metodo_de_pago != "tarjeta" and metodo_de_pago != "efectivo":
        metodo_de_pago = input("Error, ingrese un metodo de pago valido: tarjeta o efectivo: ")

    continuar = input("Desea ingresar otro pasajero? si o no: ")
    while continuar != "si" and continuar != "no":
        continuar = input("Error, ingrese una respuesta valida: si o no: ")

print("La cantidad de personas que viajan en temporada alta es:", temporada_alta)
print("La cantidad de personas que viajan en temporada baja es:", temporada_baja)
print("El peso acumulado de los pasajeros que viajan a Villa Gessel es:", peso_acumulado_villa_gessel)
print("La suma de todos los importes es:", importe_total)







 


 


 






#  temporada = input("Temporada alta o baja?: ")
#  dias = input("Cuanto dias dura el viaje?: ")
#  importe_del_viaje = input("Cual es el importe del viaje?: ")
#  altura_pasajero = input("Cual es la altura del pasajero?: ")
#  peso = input("Cual es el peso del pasajero: ")
#  sexo_pasajero = input("Que sexo es?: f: Femenino m: Masculino  nb: No Binario)")
#  equipaje_de_mano = ("viaja con equipaje de mano?: si o no")
#  metodo_de_pago =("Paga con tarjeta o efectivo: ")












