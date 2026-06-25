lista = []
lista2 = []

while True:
     print("MENU PRINCIPAL")
     print("1- Registrarse")
     print("2- Iniciar sesion")
     print("3- Salir")
     opcion = input("Elija una opcion: ")
     if opcion.isdigit():
          opcion = int(opcion)
     else:
          print("Error, ingrese una opcion valida: ")
          continue
     if opcion == 1:
          nombre = input("Crea el usuario: ")
          while nombre in lista:
               input("Error, el nombre de usuario ya existe")
               nombre = input("Crea otro usuario: ")
          else:
           lista.append(nombre)
           lista2.append(input("Crea una contraseña: "))
           print("Usuario creado con exito!")


     
     
          




