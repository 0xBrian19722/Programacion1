import json

def leer_json(lista:list,ruta:str,apertura:str)->None:
    '''
    brief: Abre un archivo json desde la ruta indicada por 
    parametro, carga su contenido y agrega cada elemento a 
    la lista recibida.
    '''
    with open(ruta,apertura) as archivo:
        datos = json.load(archivo)
        for i in range(len(datos)):
            lista.append(datos[i])
        
    
def guardar_json(lista:list,ruta:str,apertura:str)->None:
    '''
    brief: Guarda en un archivo json el contenido de la lista recibida, 
    usando la ruta y el modo de apertura pasados por parametro.
    '''
    with open(ruta, apertura) as archivo:
        json.dump(lista, archivo, indent=4)
    print("\nDatos guardados correctamente...\n")
   
