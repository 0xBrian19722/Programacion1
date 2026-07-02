def validar_numero(cadena: str) -> bool:
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


def validar_prueba_str(mensaje:str)->str:
    nombre = input(f"{mensaje}")
    validar = 0

    while validar == 0:
        validar = 1
        if len(nombre) == 0:
            validar = 0
        else:
            for i in range(len(nombre)):
                if nombre[i] == ".":
                    validar = 0
        if validar == 0:
            nombre = input(f"Error, {mensaje}: ")
    return nombre


def valid():
    nombre = input("Ingrese: ")
    while len(nombre) == 0:
            nombre = input("Error: ")
    return nombre     