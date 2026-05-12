# Enunciado/s:
# Tabla de Posiciones de Torneo de Ping-Pong
# Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
# Los datos que se cargarán son:
# Nombre del jugador
# Edad (validar)
# Cantidad de puntos (validar-número entero positivo, hasta 60).
# Número de partidos ganados (validar-número entero positivo, hasta 35).
# Tipo de saque ("plano", "liftado", "cortado")
# Categoría ("elite", "experto", "avanzado")
# Se necesita saber
# TemaA:
# 1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
# inclusive.
# 2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
# 3-Porcentaje de jugadores de categoría "experto".
# 4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
# 5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”


edad = 0
nombre = ""
cantidad_puntos = 0
partidos = 0
tipo_de_saque = ""
categoria = ""
punto_uno = 0
menor_edad = 0
bandera_menor = True
categoria_menor = ""
nombre_menor = ""
acumulador_de_vueltas = 0
acu_categoria_experto = 0
promedio_edad = 0
promedio_avanzado = 0
saque_liftado = 0
saque_cortado = 0
saque_plano = 0
saque_mas_usado = ""

bandera = True

print("Tabla de posiciones del torneo de Ping-Pong")
while bandera:
    nombre = input("Ingrese el nombre del jugador: ")

    edad = int(input("Ingrese la edad: "))
    while edad < 1:
        edad = int(input("Error, Ingrese una edad valida mayor a 0: "))

    cantidad_puntos = int(input("Ingrese la cantidad de puntos 'hasta 60': "))
    while (cantidad_puntos < 0) or (cantidad_puntos > 60):
        cantidad_puntos = int(input("Error: Ingrese una cantidad de puntos mayor a '0' hasta '60': "))

    partidos = int(input("Ingrese la cantidad de partidos 'hasta 35': "))
    while (partidos < 0) or (partidos > 35):
        partidos = int(input("Error: Ingrese una cantidad de partidos mayor a '0' hasta '35': "))

    tipo_de_saque = input("Qué tipo de saque es: 'plano', 'liftado', 'cortado': ")
    categoria = input("Ingrese la categoría: 'elite', 'experto', 'avanzado': ")

   
    if categoria == "elite" and tipo_de_saque == "plano" and (edad >= 19 and edad <= 25):
        punto_uno += 1

    
    if cantidad_puntos > 50:
        if bandera_menor:
            menor_edad = edad
            nombre_menor = nombre
            categoria_menor = categoria                     # punto dos
            bandera_menor = False
        elif edad < menor_edad:
            menor_edad = edad
            nombre_menor = nombre
            categoria_menor = categoria

    
    if categoria == "experto":
        acu_categoria_experto += 1                          #punto tres

    
    if categoria == "avanzado":
        promedio_avanzado += 1                             #punto cuatro
        promedio_edad += edad

    
    if categoria == "elite":
        if tipo_de_saque == "plano":
            saque_plano += 1
        elif tipo_de_saque == "liftado":
            saque_liftado += 1                            #punto cinco
        elif tipo_de_saque == "cortado":
            saque_cortado += 1

    acumulador_de_vueltas += 1

    corte = int(input("Realizar otra carga de datos? 1 = si, 2 = no: "))
    if corte == 2:
        print("Fin de la carga de datos.")
        bandera = False


porcentaje = (acu_categoria_experto * 100) / acumulador_de_vueltas
if promedio_avanzado > 0:
    promedio_de_edad_avanzado = promedio_edad / promedio_avanzado
else:
    promedio_de_edad_avanzado = 0

if saque_plano > saque_liftado and saque_plano > saque_cortado:
    saque_mas_usado = "plano"
elif saque_liftado > saque_cortado:
    saque_mas_usado = "liftado"
else:
    saque_mas_usado = "cortado"


print (f"1_ La cantidad de jugadores es {punto_uno}")
print (f"2_ El nombre del jugador es {nombre_menor} y su edad {menor_edad}")
print(f"3_ El porcentaje de la categoria experto es {porcentaje}")
print(f"4_ El promedio de edad es {promedio_de_edad_avanzado}")
print(f"5_ El tipo de saque mas usado es '{saque_mas_usado}'")










                                   



                   
        



    

                   


