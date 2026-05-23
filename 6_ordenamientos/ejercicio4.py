def mostrar_menu()->None:
    bandera = True
    while bandera:
     menu = int(input('''
          
        Menu de Opciones :

        1_  Listar los datoas de los usuarios de Mexico por nombre
        2_  Listar los datos de los usuarios mas joven
        3_  Mostar usuarios de México y Brasil cuyo codigo postal sea mayor a 8000 
        5_  Salir           
     '''))
     if menu == 1:
       print("Saliendo...")
       bandera = False
               
          
          
          
          
          
print(mostrar_menu())   
    
    