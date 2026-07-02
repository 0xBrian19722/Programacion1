jugadores = [
    ["Ana", 85],
    ["Luis", 92],
    ["Carla", 78],
    ["Pedro", 95],
    ["Sofía", 88]
]


def buscar_jugador(lista:list)-> str:
    jugador_max = lista[0][0]
    puntaje_max = lista[0][1]
    jugador_min = lista[0][0]
    puntaje_min = lista[0][1]
    for i in range(len(lista)):
        if lista[i][1] > puntaje_max:
            puntaje_max = lista[i][1]
            jugador_max = lista[i][0]
        if lista[i][1] < puntaje_min:
            puntaje_min = lista[i][1]
            jugador_min = lista[i][0]
    return (f"El jugador con el mas puntaje es: {jugador_max} y con el menor es: {jugador_min}") 


print(buscar_jugador(jugadores))



