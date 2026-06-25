from validaciones import validar_numero

def agregar_heroe(lista:list) -> None:
    '''brief: Solicita datos de un nuevo heroe, valida cada campo y 
       lo agrega a la lista si es correcto.
       lista: Lista de listas donde se almacenan los héroes.
       retorno: No retorna nada.
    '''
    nombre = input("Nombre: ")
    identidad = input("Identidad: ")

    bandera = True
    while bandera:
        empresa = input("Empresa (DC Comics / Marvel Comics): ")
        if empresa == "DC Comics" or empresa == "Marvel Comics":
            bandera = False
        else:
            print("Error: la empresa debe ser 'DC Comics' o 'Marvel Comics'.")
            
    bandera = True
    while bandera:
        altura_str = input("Altura: ")
        if validar_numero(altura_str):
            altura = float(altura_str)
            bandera = False
        else:
            print("Error: la altura debe ser un numero valido.")

    bandera = True
    while bandera:
        peso_str = input("Peso: ")
        if validar_numero(peso_str):
            peso = float(peso_str)
            bandera = False
        else:
            print("Error: el peso debe ser un numero valido.")

    bandera = True
    while bandera:
        fuerza_str = input("Fuerza: ")
        if validar_numero(fuerza_str):
            fuerza = int(fuerza_str)
            bandera = False
        else:
            print("Error: la fuerza debe ser un numero valido.")

    genero = input("Genero (M/F/NB): ")
    ojos = input("Color de ojos: ")
    pelo = input("Color de pelo: ")
    inteligencia = input("Inteligencia (low/average/good/high/genius): ")

    if nombre != "" and identidad != "" \
       and altura > 0 and peso > 0 and fuerza > 0 \
       and (genero == "M" or genero == "F" or genero == "NB") \
       and (inteligencia == "low" or inteligencia == "average" or inteligencia == "good" \
            or inteligencia == "high" or inteligencia == "genius"):
        lista.append([nombre, identidad, empresa, altura, peso, genero,
                      ojos, pelo, fuerza, inteligencia])
        print("Héroe agregado con éxito.\n")
    else:
        print("Datos invalidos, no se agrego el heroe.\n")
    
def eliminar_heroe(lista:list) -> None:
    '''brief: Elimina un heroe de la lista segun su nombre.
       lista: Lista de heroes.
       retorno: No retorna nada.
    '''
    nombre = input("Ingrese el nombre a eliminar: ")
    for i in range(len(lista)):
        if lista[i][0] == nombre:
            lista.pop(i)
            print("Héroe eliminado.\n")
            break
    else:   
        print("No se encontró el héroe.\n")

def mostrar_heroes(lista: list) -> None:
    '''brief: Muestra los datos principales de cada heroe en formato estructurado.
       lista: Lista de listas que contiene los heroes y sus atributos.
       retorno: No retorna nada.
    '''
    for i in range(len(lista)):
        print("Nombre:", lista[i][0], "\n",
              "Identidad:", lista[i][1], "\n",
              "Empresa:", lista[i][2], "\n",
              "---------------------------")

def ordenar_por_nombre(lista:list)->None:
    '''brief: Ordena la lista de heroes por nombre en orden alfabetico.
       lista: Lista de heroes.
       retorno: No retorna nada.
    '''
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
             if lista[j] > lista[j+1]:
              aux = lista[j]
              lista[j] = lista[j+1]
              lista[j+1] = aux
    print("Lista ordenada por nombre.\n")



