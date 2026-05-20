# Especializar las funciones del punto 12 para hacerla reutilizable. Agregar 
# validaciones.


def ingresar_cadena():
    bandera = True
    while bandera:
        texto = input("Ingrese una cadena: ").strip()
        if texto != "":
            bandera = False   
        else:
            print("Error, la cadena no puede estar vacia.")
    return texto   



hola = ingresar_cadena()