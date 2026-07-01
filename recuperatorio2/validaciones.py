def validar_numero(cadena: str)->bool:
    ''' brief: Valida si una cadena representa un numero entero o decimal.
        cadena: Cadena de dato string a validar.
        retorno: Devuelve true si la cadena es numerica, false si no lo es.
    '''
    valido = True
    punto = 0
    if cadena == "":
        valido = False
    else:
        inicio = 0
        if cadena[0] == "-":
            if len(cadena) == 1:
                valido = False
            else:
                inicio = 1
        for i in range(inicio, len(cadena)):
            caracter = cadena[i]
            if caracter == ".":
                punto += 1
                if punto > 1:
                    valido = False
            elif caracter < "0" or caracter > "9":
                valido = False
    return valido

def validar_opcion(mensaje:str,min:int,max:int)->int:
    """
    Valida que el usuario ingrese un número dentro del rango indicado.
    Parámetros: mensaje (str) - texto a mostrar, min (int) - valor mínimo, max (int) - valor máximo
    Retorno: opcion (int) - número válido ingresado por el usuario
    """
    opcion_valida = False
    opcion = 0

    while opcion_valida == False:
        opcion = input(mensaje)
        if validar_numero(opcion) == False:
            print(f"OPCION INVALIDA...")
        else:
            opcion = int(opcion)
            if opcion < min or opcion > max:
                print(f"OPCION INVALIDA...")
            else:
                opcion_valida = True

    return opcion