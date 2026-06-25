import json
from validaciones import *
from copy import deepcopy



def mostrar_menu()-> None:
    bandera = True
    lista_datos = []

    while bandera:
        print('''
            1)_ Importar datos de Json
            2)_ Listar razas
            3)_ Modificar personaje
            4)_ Eliminar personaje
            5)_ Ordenar la lista de personajes
            6)_ Personaje con mas cantidad de tecnicas  
            7)_ Listar los datos del personaje que más menos cantidad   
            de transformaciones tenga  
            8)_ Salir del programa
            ''')
        opcion = input("Elija una opcion del menu: ")

        if opcion == "1":
            lista_datos = importar_json()
            print("\nDATOS GUARDADOS\n")
        elif opcion == "2":
            if lista_datos:
                listar_razas(lista_datos)   
            else:
                print("Error, primero debe importar los datos (opcion 1)")    
        elif opcion == "3":
            if lista_datos:
                modificar_personaje(lista_datos)  
            else:
                 print("Error, primero debe importar los datos (opcion 1)")   
        elif opcion == "4":
            if lista_datos:
                eliminar_personaje(lista_datos)
            else:
                print("Error, primero debe importar los datos (opcion 1)")    
        elif opcion == "5":
            if lista_datos:
                ordenar_personajes(lista_datos)
            else:
                print("Error, primero debe importar los datos (opcion 1)")
        elif opcion == "6":
            if lista_datos:
                buscar_max_min(lista_datos, "tecnicas", True, "\nEl personaje con mas tecnicas es:")
            else:
                print("Error, primero debe importar los datos (opcion 1)")
        elif opcion == "7":
            if lista_datos:
             buscar_max_min(lista_datos, "transformaciones", False, "\nEl personaje con menos transformaciones es:")
            else:
                 print("Error, primero debe importar los datos (opcion 1)")   
        elif opcion == "8":
            if lista_datos:
                guardar_json(lista_datos)
                print("Saliendo del programa...")
            else:
                print("No hay datos para guardar.")
            bandera = False
        else:
            print("Opcion invalida, ingrese un numero del 1 al 8.")   
                

def mostrar_lista(lista: list)-> None:
    '''
    brief: Muestra los nombres de todos los personajes de la lista.
    '''
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]['nombre']}")
    
    

def mostrar_personaje(personaje: dict)-> None:
    '''
    brief: Muestra todos los datos de un personaje recorriendo 
    las claves del diccionario.
    '''
    
    claves = []
    for clave in personaje:
        claves.append(clave)
    for i in range(len(claves)):
        print(f"{claves[i]}: {personaje[claves[i]]}")


def importar_json()-> list:
    '''
    brief: Importa los datos del archivo JSON y los 
    retorna como lista de diccionarios.
    '''
    with open("Parcial2/dragon_ball.json","r") as archivo:
        datos = json.load(archivo)
    return datos
  

def listar_razas(lista:list)-> None:
    '''
    brief: Recorre la lista de personajes, agrupa las razas
    '''
    razas = []
    
    for personaje in lista:
        encontrada = False
        for raza in razas:
            if raza == personaje['raza']:
                encontrada = True
        if encontrada == False:
            razas.append(personaje['raza'])
    
    print("\nRazas de los personajes: ")
    for i in range(len(razas)):
        print(f"  {i + 1}_ {razas[i]}")
    print("------------\n")

    elejir_raza(lista, razas)

def elejir_raza(lista: list, razas: list)->None:
    '''
    brief: Permite al usuario elegir una raza y muestra 
    los personajes que pertenecen a ella.
    '''
    
    opcion_valida = False
    while opcion_valida == False:
        opcion = input("Elija una raza para ver sus personajes: ")
        if validar_numero(opcion) == False:
            print("\nError, ingrese un numero valido.\n")
        elif int(opcion) < 1 or int(opcion) > len(razas):
            print("\nOpcion invalida, intente de nuevo.\n")
        else:
            opcion_valida = True

    raza_elegida = razas[int(opcion) - 1]
    print(f"\n=== Personajes de la raza {raza_elegida} ===")
    for i in range(len(lista)):
        if lista[i]['raza'] == raza_elegida:
            mostrar_personaje(lista[i])
            print("------------")


def modificar_personaje(lista: list)-> None:
    '''
    brief: Permite al usuario modificar un dato de un personaje existente.
    Parámetros: lista (list) - lista de diccionarios con los personajes
    '''
    bandera = True
    mostrar_lista(lista)

    while bandera:
        nombre_personaje = input("Ingrese el nombre del personaje: ")

        for i in range(len(lista)):
            if lista[i]["nombre"] == nombre_personaje:
                bandera = False
                opcion = validar_opcion("""
    1_ Nombre
    2_ Raza
    3_ Nivel_poder
    4_ Planeta
    5_ Edad
    6_ Alineacion
    7_ Transformaciones
    8_ Tecnicas
    Ingrese el numero del dato a modificar:  
     """, 1, 8)

                claves = []
                for clave in lista[i]:
                    claves.append(clave)
                clave = claves[opcion - 1]
                valor = lista[i][clave]

                if type(valor) == list:
                    print(f"Valores actuales de {clave}:")
                    for j in range(len(valor)):
                        print(f"{j + 1}. {valor[j]}")

                    sub_opcion = validar_opcion("Cual desea modificar?: ", 1, len(valor))
                    valor[sub_opcion - 1] = input(f"Ingrese el nuevo valor: ")
                    print(f"{clave} actualizado correctamente.")
                else:
                    print(f"Valor actual de '{clave}': {valor}")
                    if type(valor) == int:
                        dato_valido = False
                        while dato_valido == False:
                            nuevo_valor = input(f"Ingrese el nuevo valor para {clave}: ")
                            if validar_numero(nuevo_valor) == False:
                                print("Error, debe ingresar un numero valido...")
                            else:
                                dato_valido = True
                        lista[i][clave] = int(nuevo_valor)
                    else:
                        lista[i][clave] = input(f"Ingrese el nuevo valor para {clave}: ")
                    print(f"'{clave}' actualizado correctamente.")

        if bandera:
            print("Personaje no encontrado... Los personajes disponibles son: ")
            mostrar_lista(lista)



def eliminar_personaje(lista: list)-> None:
    '''
    Permite al usuario eliminar un personaje de la lista.
    Parametros: lista (list) - lista de diccionarios con los personajes
    Retorno: None
    '''
    bandera = False

    while bandera == False:
        print("Personajes disponibles: ")
        mostrar_lista(lista)

        nombre_personaje = input("\nIngrese el nombre del personaje a eliminar: ")

        for i in range(len(lista)):
            if lista[i]["nombre"] == nombre_personaje:
                bandera = True
                lista.pop(i)
                print(f"\nEl personaje {nombre_personaje} fue eliminado correctamente...")
                print("\nPersonajes restantes: ")
                mostrar_lista(lista)
                break

        if bandera == False:
            print("Personaje no encontrado, intente nuevamente...")


def ordenar_personajes(lista: list)-> None:
    '''
    Ordena una copia de la lista de personajes por el criterio elegido,
    recibe una lista de diccionarios como parametro.
    
    '''
    copia = deepcopy(lista)

    opcion = validar_opcion("""
    1_ Nombre
    2_ Raza
    3_ Edad
    Ingrese una opcion de ordenamiento: """, 1, 3)

    datos = {1: "nombre", 2: "raza", 3: "edad"}
    clave = datos[opcion]

    for i in range(len(copia)):
        for j in range(len(copia) - 1):
            if copia[j][clave] > copia[j + 1][clave]:
                aux = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = aux

    print(f"\nLista ordenada por {clave}:\n")
    for i in range(len(copia)):
        mostrar_personaje(copia[i])
        print("-------------")    




def buscar_max_min(lista: list, clave: str, mayor: bool, mensaje: str)-> None:

    '''
    Busca y muestra los personajes con mayor o menor cantidad de elementos en una clave
    del diccionario. Utilizando un booleano True busca mayor o False busca menor  
    '''
    indice = 0

    for i in range(len(lista)):
        if mayor == True:
            if len(lista[i][clave]) > len(lista[indice][clave]):
                indice = i
        else:
            if len(lista[i][clave]) < len(lista[indice][clave]):
                indice = i

    cantidad = len(lista[indice][clave])

    print(mensaje)
    for i in range(len(lista)):
        if len(lista[i][clave]) == cantidad:
            mostrar_personaje(lista[i])
            print("--------")
    
    
def guardar_json(lista: list) -> None:
    '''
    Guarda la lista de personajes en el archivo JSON.
    Parametros: lista (list) - lista de diccionarios con los personajes
    Retorno: None
    '''
    with open("Parcial2/dragon_ball.json", "w") as archivo:
        json.dump(lista, archivo, indent=4)
    print("\nDatos guardados correctamente.\n")    