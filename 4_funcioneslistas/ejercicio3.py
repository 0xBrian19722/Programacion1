#  Desarrollar una función que pida 10 números dentro de un rango 
# especificado, validar los números solicitados dentro de ese rango, guardar en una 
# lista y retornarla.  El programa principal debe invocar a la función y mostrar por 
# pantalla el retorno.


def crear_lista():
    lista = []
    minimo = 0
    maximo = 30

    for i in range(10):
        bandera = True
        while bandera:  
            numero = int(input(f"Ingrese el numero {i+1} (entre {minimo} y {maximo}): "))
            if minimo <= numero and numero <= maximo:
                lista.append(numero)
                bandera = False  
            else:
                print("Error, numero fuera de rango, intente de nuevo.")
    return lista


print("Lista final: ", crear_lista())