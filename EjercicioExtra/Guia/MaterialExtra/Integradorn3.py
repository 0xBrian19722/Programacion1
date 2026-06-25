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


bandera = True
corte = ""
edad = 0
tipo_de_saque = ""
cantidad_de_jugadores = 0
menor_edad = 0
nombre_menor = ""
categoria_menor = ""
contador = 0
contador_experto = 0
porcentaje = 0
promedio_de_edad = 0
acumulador_edad = 0
plano = 0
liftado = 0
cortado = 0
saque_mas_usado = 0
contador_experto = 0
contador_categoria = 0
contador_edad_categoria = 0
contador_edad = 0
promedio_edad = 0

print("TABLA DE POSICIONES DE TORNEO DE Ping - Pong")

bandera = True

cantidad_de_jugadores = 0
menor_edad = 0
nombre_menor = ""
categoria_menor = ""
contador = 0
total_jugadores = 0
contador_experto = 0
acumulador_edad = 0
contador_edad_categoria = 0
plano = 0
liftado = 0
cortado = 0
saque_mas_usado = ""

while bandera:
    nombre = input("Ingrese nombre del jugador: ") 

    while True:
        try:    
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError: 
            print("ERROR, Ingrese la edad nuevamente: ")

    puntuacion = input("Ingrese la puntuacion: ") 
    while not puntuacion.isdigit() or int(puntuacion) > 60 or int(puntuacion) < 0:
        puntuacion = input("Error, Ingrese devuelta una puntuacion valida, mayor a 0 y menor a 60: ")
    puntuacion = int(puntuacion)

    partidos_ganados = input("Ingrese la cantidad de partidos ganados: ")
    while not partidos_ganados.isdigit() or int(partidos_ganados) > 35 or int(partidos_ganados) < 0:
        partidos_ganados = input("Error, ingrese una cantidad de partidos validas mayor a 0 y hasta 35 partidos: ")
    partidos_ganados = int(partidos_ganados)

    tipo_de_saque = input("Ingrese el tipo de saque: liftado, plano o cortado ")
    while tipo_de_saque != "plano" and tipo_de_saque != "liftado" and tipo_de_saque != "cortado":
        tipo_de_saque = input("Error, Ingrese un tipo de saque valido: ")

    categoria = input("Ingrese la categoria: (elite, experto, avanzado)")  
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("Error, Ingrese una categoria valida: ")

    total_jugadores = total_jugadores + 1
    if categoria == "experto":
        contador_experto = contador_experto + 1
    if categoria == "avanzado":
        acumulador_edad = acumulador_edad + edad
        contador_edad_categoria = contador_edad_categoria + 1

    if categoria == "elite" and tipo_de_saque == "plano" and (edad >= 19 and edad <= 25):
        cantidad_de_jugadores = cantidad_de_jugadores + 1

    if puntuacion > 50:
        if contador == 0:   
            menor_edad = edad
            nombre_menor = nombre
            categoria_menor = categoria
        elif edad < menor_edad:   
            menor_edad = edad
            nombre_menor = nombre
            categoria_menor = categoria
        contador = contador + 1

    if categoria == "elite":
        if tipo_de_saque == "plano":
            plano = plano + 1
        elif tipo_de_saque == "liftado":
            liftado = liftado + 1
        elif tipo_de_saque == "cortado":
            cortado = cortado + 1

    corte = input("Desea continuar con la lista ingrese: (si) o para terminar (no): ") 
    if corte == "no":
        bandera = False

if total_jugadores != 0:
    porcentaje = (contador_experto / total_jugadores) * 100
else:
    porcentaje = 0

if contador_edad_categoria != 0:
    promedio_de_edad = acumulador_edad / contador_edad_categoria
else:
    promedio_de_edad = 0

if plano >= liftado and plano >= cortado:
    saque_mas_usado = "plano"
elif liftado >= plano and liftado >= cortado:
    saque_mas_usado = "liftado"
else:
    saque_mas_usado = "cortado"

print(f"Cantidad de jugadores de la categoría elite con tipo de saque plano, cuya edad esté entre 19 y 25 años es: {cantidad_de_jugadores}.")
print(f"El nombre y la categoria del jugador con menos edad es {nombre_menor} con {menor_edad} años.")
print(f"El porcentaje de jugador de categoria experto es {porcentaje}.")
print(f"El promedio de edad de la categoria (avanzado) es: {promedio_de_edad}")
print(f"El tipo de saque mas usado de la categoria de elite es: {saque_mas_usado}")


     
    
