#  Crear una funcion que devuelva una lista con el diccionario (lista de 
# diccionario)

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
    {
        "numero": 11,
        "nombre": "Angel",
        "apellido": "Correa",
        "edad": 31,
        "calificaciones": [8, 7, 8],
        "equipo": {"club": "Atletico Madrid", "pais": "España"},
        "grupos": [
            {"nombre": "Suplentes", "descripcion": "Jugadores de rotación"}
        ],
        "posicion": "Delantero"
    },
    
]


def mostrar(lista:dict):
    for mostrar in lista:
        print(mostrar)
        print("---------")
    


