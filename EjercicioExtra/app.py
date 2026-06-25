from juegos import *
from funciones import *


def mostrar_menu()-> None:
    bandera = True

    while bandera:
      print ('''MENU

               1_ Mostrar lista
               2_ Calcular precio mas caro
               3_ Agregar Juego nuevo
               4_ Eliminar Juego
               5_ Salir
         ''')
      opcion = int(input("Ingrese una opcion: "))
      if opcion == 1:
         mostrar_lista(videojuegos)
      elif opcion == 2:
         calcular_precio(videojuegos)
      elif opcion == 3:
         agregar_juego(videojuegos)  
      elif opcion == 4:
         eliminar_juego(videojuegos)
      elif opcion == 5:
         print("Saliendo del programa...")
         bandera = False
      else:
         print("Opcion invalida...")



print(mostrar_menu())
    
           

   
