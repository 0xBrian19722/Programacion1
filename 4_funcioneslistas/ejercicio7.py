# Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de 
# compras on-line recientemente lanzado al mercado para ello necesita un programa 
# que le permita acceder a los datos relevados. 
# Realizar una función con el siguiente Menú de Opciones: 
# 1-Importar listas 
# 2-Listar los datos de los usuarios de México 
# 3-Listar los nombre, mail y teléfono de los usuarios de Brasil 
# 4-Listar los datos del/los usuario/s más joven/es 
# 5-Obtener un promedio de edad de los usuarios 
# 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad 
# 7-Listar los datos de los usuarios de México y Brasil cuyo código postal 
# sea mayor a 8000 
# 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
# años. 


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
                print("Importar listas")
            case 2:
                print("Usuarios de Mexico")
            case 3:
                print("Usuarios de Brasil")
            case 4:
                print("Usuarios mas jovenes")
            case 5:
                print("Promedio de edades")
            case 6:
                print("Usuario de Brasil con mayor edad")
            case 7:
                print("Usuarios Mexico/Brasil con CP mayor a 8000")
            case 8:
                print("Italianos mayores de 40")
            case 9:
                print("Saliendo del programa...")
                bandera = False

print(mostrar_menu())








