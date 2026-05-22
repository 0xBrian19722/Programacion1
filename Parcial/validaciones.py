def es_numero(cadena: str) -> bool:
    ''' brief: Valida si una cadena representa un numero entero o decimal.
        cadena: Cadena de dato string a validar.
        retorno: Devuelve true si la cadena es numerica, false si no lo es.
    '''
    if cadena == "":
        return False
    punto = 0
    for i in range(len(cadena)):   
        caracter = cadena[i]
        if caracter == ".":
            punto += 1
            if punto > 1:   
                return False
        elif caracter < "0" or caracter > "9":
            return False
    return True         
