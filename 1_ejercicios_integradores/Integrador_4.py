# Ejercicio 1: Registro de internaciones en un hospital 
# Un hospital registra una cantidad indeterminada de internaciones en un día. 
# Por cada paciente se ingresan los siguientes datos: 

# ● Nombre del paciente 
# ● Edad (entre 0 y 100) 
# ● Tipo de atención (urgencia, control, cirugía) 
# ● Cantidad de días internado (entre 1 y 60) 
# ● Costo por día (mayor a 0) 
# ● Sexo (F, M, NB) 
# ● Tiene obra social (sí/no) 
# ● Forma de pago (efectivo, tarjeta, transferencia) 

# Todos los datos deben ser validados. 
# Consideraciones: 

# ● Si el paciente tiene obra social, se aplica un descuento del 20% sobre el costo de su 
# internación. 
# ● Si la cantidad total de días acumulados supera los 500, se aplica un descuento 
# general del 10% sobre el total bruto. 
# Se pide: 
# a. Total bruto recaudado por internaciones. Luego, total final con descuentos aplicados. 
# b. Cantidad de pacientes por tipo de atención. 
# c. El tipo de atención con mayor cantidad de días acumulados. 
# d. El nombre del paciente con mayor costo total de internación. 
# e. El promedio de costo por día de todos los pacientes. 
# f. Qué forma de pago fue la más utilizada. 
# g. Cuántos pacientes tienen más de 10 días de internación.

bandera = True
edad = 0
nombre = ""
acumulador_dias = 0
contador_urgencia = 0
contador_control = 0
contador_cirugia = 0
acum_dias_control = 0
acum_dias_cirugia = 0
acum_dias_urgencia = 0
tipo_mayor_atencion = ""
nombre_mayor_costo = ""
total_bruto_maximo = 0
promedio_por_dia = 0
contador_vueltas = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0
tipo_mayor_pago = 0
contador_pacientes_diez_dias = 0
total_acumulado = 0
cantidad_dias_internado = 0

while bandera:
    contador_vueltas += 1
    nombre = input("Ingrese el nombre: ")

    edad = int(input("Ingrese su edad: "))
    while edad > 100 or edad < 0:
        edad = int(input("Error, ingrese una edad valida: "))


    cantidad_dias_internado = int(input("Ingrese la canitdad de dias internado (entre 0 y 60 dias): "))    
    while cantidad_dias_internado < 1 or cantidad_dias_internado > 60:
        cantidad_dias_internado = int(input("Error, Ingrese los dias dentro del rango (0 - 60) dias: "))
    acumulador_dias += cantidad_dias_internado
    if cantidad_dias_internado > 10:
            contador_pacientes_diez_dias += 1
        
    tipo_de_urgencia = input("Ingrese el tipo de urgencia (urgencia, control, cirugía):  ")    
    while tipo_de_urgencia != "urgencia" and tipo_de_urgencia != "control" and tipo_de_urgencia != "cirugia":
        tipo_de_urgencia = input("Error, ingrese nuevamente el tipo de urgencia: ")
    if tipo_de_urgencia == "urgencia":
            contador_urgencia += 1
            acum_dias_urgencia += cantidad_dias_internado
    elif tipo_de_urgencia == "control":
            contador_control += 1
            acum_dias_control += cantidad_dias_internado
    elif tipo_de_urgencia == "cirugia":
            contador_cirugia += 1 
            acum_dias_cirugia += cantidad_dias_internado       

    costo_por_dia = int(input("Ingrese el costo por dia: "))  
    while costo_por_dia < 0:
        costo_por_dia = int(input("Error, Ingrese un costo mayor a 0: "))  

    sexo = input("Ingrese el sexo (F, M, NB): ")    
    while sexo != "f" and sexo != "m" and sexo != "nb":
        sexo = input("Error, Ingrese una opcion valida: ")
    
    obra_social = input("Tiene obra social (si/no): ")  
    while obra_social != "si" and obra_social != "no":
        obra_social = input("Error, Ingrese una opcion valida: ")  

    forma_de_pago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")
    while forma_de_pago != "efectivo" and forma_de_pago != "tarjeta" and forma_de_pago != "transferencia":
        forma_de_pago = input("Error, Ingrese una forma de pago valida (efectivo, tarjeta, transferencia):  ")
    if  forma_de_pago == "efectivo":
     contador_efectivo += 1
    elif forma_de_pago == "tarjeta":
     contador_tarjeta += 1
    elif forma_de_pago == "transferencia":
     contador_transferencia += 1 
            
          
           


    corte = input("Ingresar otro paciente (si/no): ") 
    while corte != "si" and corte != "no":
        corte = input("Error, Ingrese una opcion valida: ")
    if corte == "no":
        bandera = False
        print("Carga de datos finalizada.")
    else:
        bandera = True

    total_bruto = cantidad_dias_internado * costo_por_dia 
    total_acumulado += total_bruto   
    promedio_por_dia = total_acumulado / contador_vueltas
    if total_bruto > total_bruto_maximo:
        total_bruto_maximo = total_bruto
        nombre_mayor_costo = nombre
         
    # ● Si el paciente tiene obra social, se aplica un descuento del 20% sobre el costo de su 
    # internación. 
    if obra_social == "si":
     total_con_obrasocial = total_bruto * 0.80 

    # Si la cantidad total de días acumulados supera los 500, se aplica un descuento 
    # general del 10% sobre el total bruto. 
    if acumulador_dias > 500:
        total_general_con_descuento = total_acumulado * 0.90
    else:
        total_general_con_descuento = total_acumulado

    # c. El tipo de atención con mayor cantidad de días acumulados
    if acum_dias_urgencia >= acum_dias_cirugia and acum_dias_urgencia >= acum_dias_control:
        tipo_mayor_atencion = "urgencia"
    elif acum_dias_control >= acum_dias_cirugia and acum_dias_control >= acum_dias_urgencia:
        tipo_mayor_atencion = "control"
    elif acum_dias_cirugia >= acum_dias_control and acum_dias_cirugia >= acum_dias_urgencia:
        tipo_mayor_atencion = "cirugia"


    if contador_efectivo >= contador_tarjeta and contador_efectivo >= contador_transferencia:
        tipo_mayor_pago = "efectivo"
    elif contador_tarjeta >= contador_efectivo and contador_tarjeta >= contador_transferencia:
        tipo_mayor_pago = "tarjeta"
    elif contador_transferencia >= contador_tarjeta and contador_transferencia >= contador_efectivo:
        tipo_mayor_pago = "transferencia"


    

print(f"1_ El total reacudado por internacion es {total_acumulado} y el total con descuentos aplicados es {total_general_con_descuento}")
print(f"2_ La cantidad de pacientes en urgencias es {contador_urgencia} pacientes, en control {contador_control} pacientes, y en cirugia {contador_cirugia} pacientes")
print(F"3_ El tipo de atencion con mayor cantidad de dias acumulados es {tipo_mayor_atencion} ")
print(f"El nombre del paciente con mayor costo es {nombre_mayor_costo}")
print(f"El promedio de costo por dia de todos los pacientes es {promedio_por_dia}")
print(f"La forma de pago mas utilizada es {tipo_mayor_pago}")
print(f"La cantidad de pacientes con mas de diez dias de internacion es {contador_pacientes_diez_dias}")






# a. Total bruto recaudado por internaciones. Luego, total final con descuentos aplicados. 
# b. Cantidad de pacientes por tipo de atención. 
# c. El tipo de atención con mayor cantidad de días acumulados. 
# d. El nombre del paciente con mayor costo total de internación. 
# e. El promedio de costo por día de todos los pacientes. 
# f. Qué forma de pago fue la más utilizada. 
# g. Cuántos pacientes tienen más de 10 días de internación.
    





       









    
   