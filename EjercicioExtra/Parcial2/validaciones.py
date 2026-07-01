def validar_numero(cadena: str) -> bool:
    ''' brief: Valida si una cadena representa un numero entero o decimal.
        cadena: Cadena de dato string a validar.
        retorno: Devuelve true si la cadena es numerica, false si no lo es.
    '''
    valido = True
    punto = 0
    if cadena == "":
        valido = False
    else:
        for i in range(len(cadena)):
            caracter = cadena[i]
            if caracter == ".":
                punto += 1
                if punto > 1:
                    valido = False
            elif caracter < "0" or caracter > "9":
                valido = False

    return valido

def validar_opcion(mensaje: str, minimo: int, maximo: int) -> int:
    """
    Valida que el usuario ingrese un número dentro del rango indicado.
    Parámetros: mensaje (str) - texto a mostrar, minimo (int) - valor mínimo, maximo (int) - valor máximo
    Retorno: opcion (int) - número válido ingresado por el usuario
    """
    opcion_valida = False
    opcion = 0

    while opcion_valida == False:
        opcion = input(mensaje)
        if validar_numero(opcion) == False:
            print("Opcion invalida.")
        else:
            opcion = int(opcion)
            if opcion < minimo or opcion > maximo:
                print("Opcion invalida.")
            else:
                opcion_valida = True

    return opcion