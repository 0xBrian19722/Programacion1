from abm import *
from estadisticas import *
from lista_heroes import *




bandera = True
lista_heroes = []  

while bandera:
    print('''\nMENU 
    [1]- Importar lista de heroes
    [2]- Mostrar heroes
    [3]- Agregar heroe
    [4]- Eliminar heroe
    [5]- Ordenar por nombre
    [6]- Ver heroe mas alto
    [7}- Ver heroe mas fuerte
    [8]- Ver heroe menos pesado                       
    [9]- Salir\n''')

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        from lista_heroes import lista_heroes
        print("\nLista de heroes importada correctamente.\n")
    elif opcion == "2":
        if lista_heroes:
            mostrar_heroes(lista_heroes)
        else:
            print("Primero debe importar la lista (opcion 1).\n")
    elif opcion == "3":
        if lista_heroes:
            agregar_heroe(lista_heroes)
        else:
            print("Primero debe importar la lista (opcion 1).\n")
    elif opcion == "4":
        if lista_heroes:
            eliminar_heroe(lista_heroes)
        else:
            print("Primero debe importar la lista (opcion 1).\n")
    elif opcion == "5":
        if lista_heroes:
            ordenar_por_nombre(lista_heroes)
        else:
            print("Primero debe importar la lista (opcion 1).\n")
    elif opcion == "6":
        if lista_heroes:
            buscar_mas_alto(lista_heroes)
        else:
            print("Primero debe importar la lista (opcion 1).\n")
    elif opcion == "7":
        if lista_heroes:
            buscar_mas_fuerte(lista_heroes)
        else:
            print("Primero debe importar la lista (opcion 1).\n")
    elif opcion == "8":
        if lista_heroes:
            buscar_menos_pesado(lista_heroes)
        else:
            print("Primero debe importar la lista (opcion 1).\n")
    elif opcion == "9":
        print("FIN DEL PROGRAMA...")
        bandera = False
    else:
        print("Opcion invalida.\n")