import json

def leer_json(lista:list,ruta:str,apertura:str):
    with open(ruta,apertura) as archivo:
        datos = json.load(archivo)
        for i in range(len(datos)):
            lista.append(datos[i])
        return(datos)
    
def guardar_json(lista:list,ruta:str,apertura:str)->None:
    '''
    Guarda la lista de personajes en el archivo JSON.
    Parametros: lista (list) - lista de diccionarios con los personajes
                ruta (str) - ruta del archivo JSON
    Retorno: None
    '''
    with open(ruta, apertura) as archivo:
        json.dump(lista, archivo, indent=4)
    print("\nDatos guardados correctamente...\n")
