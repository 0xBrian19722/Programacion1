
import json
with open("archivos/data_stark.json", "r") as archivo:
    datos = json.load(archivo)


    # for heroes in datos["heroes"]:
    #     print(heroes)
    #     print("------")


def leer_json(ruta,clave):
    with open(ruta,"r") as archivo:
        datos = json.load(archivo)
        return datos[clave]
    

    



print(leer_json("archivos/data_stark.json","heroes"))