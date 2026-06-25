# Se proporciona un archivo JSON de juegos: leerlo y guardarlo en una 
# colección.  


import json


def leer_json():
    with open("practicadelmate/juegos.json","r") as archivo:
        datos = json.load(archivo)
        return(datos)


def eliminar_juego(datos):
    nombre = input("Ingrese el juego a eliminar: ")
    for i in range (len(datos)-1):
        if datos[i]["titulo"] == nombre:
            datos.pop(i)
            print(f"Se a eliminado {nombre} con exito")

def guardar_json(datos):
    with open("practicadelmate/juegos.json","w") as archivo:
        json.dump(datos, archivo, indent=4)            


lista_json = leer_json()


for i in range(len(lista_json)):
    print(lista_json[i])
    print("--------")


eliminar_juego(lista_json)
guardar_json(lista_json)

for i in range (len(lista_json)):
    print(lista_json[i])
    print("-----------")