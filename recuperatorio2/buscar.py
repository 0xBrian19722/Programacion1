def buscar_epoca(lista:list)->list:
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
    """
    Busca un personaje por cualquier campo y retorna si existe.
    Parámetros:
        lista (list): Lista de diccionarios de personajes.
        campo (str): Campo por el cual buscar ("nombre", "epoca", etc).
        valor (str): Valor a buscar.
    Retorna:
        bool: True si existe, False si no.
    """
    bandera = False
    for i in range(len(lista)):
        if lista[i][clave] == ingreso:
            bandera = True
    return bandera


def buscar_max_min(lista: list, clave: str, tipo: str) -> int:
    """
    Busca el personaje con mayor o menor cantidad de elementos en un campo lista.

    Parámetros:
        lista (list): Lista de diccionarios de personajes.
        clave (str): Campo a analizar ("logros" o "eventos").
        tipo (str): "max" para buscar el mayor, "min" para buscar el menor.

    Retorna:
        int: Índice del personaje encontrado.
    """
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