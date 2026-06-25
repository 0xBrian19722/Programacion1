# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot


jugador = int(input("Ingrese la altura del jugar: "))

if jugador >= 160 and jugador < 180:
    print("El jugador es escolta")
elif jugador >= 180 and jugador < 200:
    print("El jugador es Alero")
else:  
    jugador >= 200
    print("El jugador es Ala-Pívot o Pívot")       