def buscar_epoca(lista:list)->list:
    '''
    brief: Recorre la lista de personajes y construye una lista con todas las
    epocas distintas encontradas.
    '''
    bandera = False
    lista_epoca = []
    for i in range(len(lista)):
        bandera = False  
        for j in range(len(lista_epoca)):
            if lista_epoca[j] == lista[i]["epoca"]:
                bandera = True
        if bandera == False:
            lista_epoca.append(lista[i]["epoca"])
    return (lista_epoca)


def buscar_clave(lista:list,clave:str,ingreso: str)->bool:
    '''
    brief: Recorre una lista de diccionarios y verifica si existe algun elemento
    que coincida con el valor en la clave indicada con el dato ingresado.
    '''
    bandera = False
    for i in range(len(lista)):
        if lista[i][clave] == ingreso:
            bandera = True
    return bandera




def buscar_max_min(lista: list, clave: str, tipo: str) -> int:
    '''
    brief: Busca dentro de una lista de diccionarios el indice del personaje
    que tenga la mayor o menor cantidad de elementos en el valor de la
    clave indicada, segun el tipo solicitado ("max" o "min").
    '''

    resultado = len(lista[0][clave])
    indice = 0

    for i in range(len(lista)):
        if tipo == "max":
            if len(lista[i][clave]) > resultado:
                resultado = len(lista[i][clave])
                indice = i
        elif tipo == "min":
            if len(lista[i][clave]) < resultado:
                resultado = len(lista[i][clave])
                indice = i

    return indice