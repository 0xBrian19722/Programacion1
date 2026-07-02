from archivos import leer_json, guardar_json
from validaciones import *
from buscar import *
import copy







def mostrar_menu():

    bandera = True
    lista_personajes = []
    while bandera:
        print('''
        1)_ Importar archivos 
        2)_ Listar personajes por epoca
        3)_ Modoficar personaje 
        4)_ Eliminar personaje
        5)_ Ordenar personas
        6)_ Ver personaje con mayores logros
        7)_ Ver personaje con menor participes de eventos historicos
        8)_ Salir del programa
        ''')
        opciones = input("Ingrese una opcion del menu: ")

        if opciones == "1":
            leer_json(lista_personajes,"recuperatorio2/personajes.json","r")
            print("\nDatos guardados correctamente..")

        elif opciones == "2":
            if lista_personajes:
                mostrar_epoca(lista_personajes)
            else:
                print("Error, primero debe importar los datos (opcion 1)") 

        elif opciones == "3":
            if lista_personajes:
                modificar_personaje(lista_personajes,"Ingrese el nombre del" \
                "personaje que desee modificar: ")
            else:
                print("Error, primero debe importar los datos (opcion 1)")


        elif opciones == "4":
            if lista_personajes:
                eliminar_personaje(lista_personajes)
            else:
                print("Error, primero debe importar los datos (opcion 1)") 

           
        elif opciones == "5":
            if lista_personajes:
                ordenar_personajes(lista_personajes)
            else:  
                print("Error, primero debe importar los datos (opcion 1)")   

        elif opciones == "6":
            if lista_personajes:
                print("\nPersonaje con mayor logros: ")
                indice = buscar_max_min(lista_personajes, "logros", "max")
                mostrar_personajes([lista_personajes[indice]])
            else:
                print("Error, primero debe importar los datos (opcion 1)")

        elif opciones == "7":
            if lista_personajes:
                print("\nPersonaje con menor eventos historicos: ")
                indice = buscar_max_min(lista_personajes, "eventos", "min")
                mostrar_personajes([lista_personajes[indice]])
            else:
                print("Error, primero debe importar los datos (opcion 1)")

        elif opciones == "8":
                guardar_json(lista_personajes, "recuperatorio2/personajes.json", "w")
                bandera = False
                print("FIN DEL PROGRAMA...")
            

            

def mostrar_lista(lista:list)->str:
    '''   
    brief: Recorre la lista y arma un texto donde cada elemento 
    aparece en una linea marcado con un guion. Devuelve un string 
    con todos los elementos juntos
    '''
    mensaje = ""
    for i in range(len(lista)):
        mensaje += f"  - {lista[i]}\n"
    return mensaje
        
        
 

def mostrar_personajes(lista:list)->None:
    '''
    brief: Recorre una lista de diccionarios de personajes 
    y muestra por terminal sus datos principales 
    '''
    for i in range(len(lista)):
        mensaje = ""
        mensaje += f"Nombre: {lista[i]['nombre']}\n"
        mensaje += f"Epoca: {lista[i]['epoca']}\n"
        mensaje += f"Pais: {lista[i]['pais']}\n"
        mensaje += f"Nacimiento: {lista[i]['anio_nacimiento']}\n"
        mensaje += f"Profesion: {lista[i]['profesion']}\n"
        mensaje += "Logros:\n"
        mensaje += mostrar_lista(lista[i]["logros"])
        mensaje += "Eventos:\n"
        mensaje += mostrar_lista(lista[i]["eventos"])
        print("----------------------")
        print(mensaje)
        print("----------------------")
    
    




def mostrar_epoca(lista: list) -> None:
    '''
    brief: Muestra las epocas en la lista de personajes, 
    permite elegir una y luego imprime los personajes que 
    pertenecen a esa epoca.
    '''
    lista_epoca = buscar_epoca(lista)
    for i in range(len(lista_epoca)):
        print(f"{i + 1}_ {lista_epoca[i]}")
    
    ingreso = validar_opcion("\nIngrese un numero de lista: ", 1, len(lista_epoca))
    epoca_elegida = lista_epoca[ingreso - 1]

    for i in range(len(lista)):
        if lista[i]["epoca"] == epoca_elegida:
            mostrar_personajes([lista[i]])

  



def mostrar_nombres(lista:list)-> None:
    '''
    brief: Recorre una lista de diccionario y muestra en pantalla
    los nombres de cada uno enumerados en orden
    '''

    for i in range(len(lista)):
        print(f"{i+1}_ {lista[i]['nombre']}\n")



def guardar_indice(lista:list,clave:str,ingreso:str) -> int:
    '''
    brief: Recorre una lista de diccionarios y busca el indice del elemento
    cuyo valor en la clave indicada coincide con el dato ingresado.
    '''
    indice = -1
    for i in range(len(lista)):
        if lista[i][clave] == ingreso:
            indice = i
    return indice




def mostrar_claves(lista: list) -> None:
    '''
    brief: Obtiene las claves del diccionario de la lista 
    y las muestra enumeradas en orden.
    '''
   
    claves = []
    for clave in lista[0]:
        claves.append(clave)
    for i in range(len(claves)):
        print(f"{i + 1}_ {claves[i]}")



def modificar_lista(lista_campo: list) -> None:
    '''
    brief: Muestra los elementos de la lista , permite al usuario
    elegir uno por numero y reemplazarlo con un nuevo valor ingresado.
    '''

    for i in range(len(lista_campo)):
        print(f"{i + 1}_ {lista_campo[i]}")
    indice = validar_opcion("Ingrese el numero del dato a moficar: ", 1, len(lista_campo))
    lista_campo[indice - 1] = input("Ingrese el nuevo valor: ")
        



def modificar_valor(personaje:dict,valor:int,min:int,max:int)->None:
    '''
    brief: Permite modificar el valor de un clave específico del diccionario, 
    si la clave contiene una lista, llama a la función modificar_lista. Si es el año
    de nacimiento valida que este dentro de un rango. 
    '''

    claves = []
    for clave in personaje:
        claves.append(clave)

    clave_elegida = claves[valor - 1]

    if type(personaje[clave_elegida]) == list:
        modificar_lista(personaje[clave_elegida])
    elif clave_elegida == "anio_nacimiento":
        personaje[clave_elegida] = validar_opcion(f"Nuevo año: ", min, max)
    else:
        personaje[clave_elegida] = input(f"Nuevo {clave_elegida}: ")    





def modificar_personaje(lista:list, mensaje:str) -> None:
    '''
    brief: Permite modificar los datos de un personaje dentro de una lista,
    muestra los nombres disponibles, solicita el nombre a modificar, valida que
    exista y luego permite elegir que campo actualizar 
    '''

    mostrar_nombres(lista)
    bandera = True
    while bandera:
        nombre = input(mensaje)
        encontrado = buscar_clave(lista, "nombre", nombre)
        if encontrado == False:
            print("ERROR, nombre no encontrado.")
        else:
            bandera = False

    indice = guardar_indice(lista, "nombre", nombre)
    mostrar_personajes([lista[indice]])
    mostrar_claves(lista)
    clave = validar_opcion("Ingrese el dato a modificar: ", 1, 7)
    modificar_valor(lista[indice], clave,-3000,2025)

    print("Personaje modificado correctamente...")



def eliminar_personaje(lista: list) -> None:
    '''
    brief: Permite eliminar un personaje de la lista, muestra los nombres
    disponibles, solicita el nombre a eliminar, valida que exista, muestra
    sus datos y luego lo elimina de la lista.
    '''

    mostrar_nombres(lista)
    bandera = True
    while bandera:
        nombre = input("Ingrese el nombre del personaje a eliminar: ")
        encontrado = buscar_clave(lista, "nombre", nombre)
        if encontrado == False:
            print("ERROR, nombre no encontrado.")
        else:
            bandera = False

    indice = guardar_indice(lista, "nombre", nombre)
    mostrar_personajes([lista[indice]])
    lista.pop(indice)
    print(f"Personaje eliminado correctamente...")
    mostrar_nombres(lista)



def ordenar_personajes(lista: list) -> None:
    '''
    brief: Ordena una copia de la lista de personajes segun el criterio elegido
    (año de nacimiento, nombre o epoca) utilizando el algoritmo
    bubble sort, y luego muestra los personajes ordenados en pantalla
    '''

    print('''
        1_ Año de nacimiento
        2_ Nombre
        3_ Epoca"\n''')
          
    criterio = validar_opcion("Elija un criterio para ordenar la lista: ", 1, 3)

    claves = ["anio_nacimiento", "nombre", "epoca"]
    clave_elegida = claves[criterio - 1]

    copia = copy.deepcopy(lista)

    for i in range(len(copia) - 1):
        for j in range(len(copia) - 1):
            if copia[j][clave_elegida] > copia[j + 1][clave_elegida]:
                aux = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = aux

    mostrar_personajes(copia)















    










        









        




    


