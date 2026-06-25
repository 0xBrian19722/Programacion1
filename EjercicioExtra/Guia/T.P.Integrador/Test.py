

usuarios = ["brian"]
contraseñas = []


while True:
     print("--Menu principal--")
     print("1- registrarse")
     print("2- login")
     print("3- salir")
     opcion = input("Ingrese una opcion: ")

     if opcion.isdigit():             
         opcion = int(opcion)
     else:
         print("Error, ingrese una opcion valida.")
         continue    
     
     if opcion == 1:
         nombre = (input("Crea un usuario: "))
         while nombre in usuarios:
            print("Error: el nombre de usuario ya existe...")
            nombre = input("Crea un usuario diferente: ")
         usuarios.append(nombre)   
         contraseñas.append(input("Crea la contraseña: ")) 
         print("Usiario creado con  exito!")
         
         
     elif opcion == 2:
         usuario = input("Usuario: ")
         contraseña = input("Contraseña: ")
     elif opcion == 3:
         print("Saliendo...")
         break
     else:
         print("Opcion invalida")

     


         

             
















   

