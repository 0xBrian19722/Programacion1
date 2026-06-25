
# lista_usuarios = [
    
#     {
#         "id" : 2,
#         "nombre" : "mariano",
#         "apellido" : "gomez",
#         "nacionalidad" : "argentina",
#         "dni" : 2323232323,
#     },
#     {
#         "id" : 3,
#         "nombre" : "fabio",
#         "apellido" : "josefo",
#         "nacionalidad" : "roma",
#         "dni" : 1,
#     },
#     {
#         "id" : 4,
#         "nombre" : "mariano",
#         "apellido" : "fernandez",
#         "nacionalidad" : "argentina",
#         "dni" : 343556,
#     },
# ]

jugadores = [
    {
        "numero": 10,
        "nombre": "Lionel",
        "apellido": "Messi",
        "edad": 39,
        "calificaciones": [10, 9, 10], # de los ultimos partidos, como jugo
        "equipo": {"club": "Inter Miami", "pais": "Estados Unidos"},
        "grupos": [
            {"nombre": "Titulares", "descripcion": "Jugadores habituales del once inicial"},
            {"nombre": "Capitanes", "descripcion": "Referentes del equipo"}
        ],
        "posicion": "Delantero"
    },
    {
        "numero": 22,
        "nombre": "Lautaro",
        "apellido": "Martinez",
        "edad": 29,
        "calificaciones": [9, 8, 10],
        "equipo": {"club": "Inter", "pais": "Italia"},
        "grupos": [
            {"nombre": "Titulares", "descripcion": "Jugadores habituales del once inicial"}
        ],
        "posicion": "Delantero"
    },
]

def mostrar_jugadores(lista:list):
    for diccioanrio in lista:
        print(diccioanrio)
        print("------")
    return diccioanrio

mostrar_jugadores(jugadores)    
        




