from funciones import *






def mostrar_menu():
    bandera = True
    print('''1- Importar listas 
2- Listar los datos de los usuarios de México 
3- Listar los nombre, mail y teléfono de los usuarios de Brasil 
4- Listar los datos del/los usuario/s más joven/es 
5- Obtener un promedio de edad de los usuarios 
6- De los usuarios de Brasil, listar los datos del usuario de mayor edad 
7- Listar los datos de los usuarios de México y Brasil cuyo código postal 
sea mayor a 8000 
8- Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
años. 
9- Salir          
''')
    while bandera:
        opciones = int(input("Ingrese una opcion del menu: "))
        while opciones > 9 or opciones < 0:
            opciones = int((input("Error, Ingrese una opcion valida: ")))

        match opciones:

            case 1:
                importar_lista()
            case 2:
                mostrar_usuarios_mexico()
            case 3:
                mostrar_usuarios_brasil()
            case 4:
                mostrar_usuarios_jovenes()
            case 5:
                mostrar_promedio()
            case 6:
                mostrar_usuariosmayor_brasil()
            case 7:
                mostrar_codigo_postal()
            case 8:
                mostrar_usuarios_italia()
            case 9:
                print("Saliendo del programa...")
                bandera = False

print(mostrar_menu())


