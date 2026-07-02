# Lista de usuarios (cada usuario es un diccionario)
usuarios = []

def registrar_usuario():
    nombre = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    tipo = input("Ingrese tipo de usuario (admin/jugador): ")

    # Validaciones básicas
    if nombre == "" or contraseña == "":
        print("Error: nombre y contraseña no pueden estar vacíos.")
        return
    for u in usuarios:
        if u["nombre"] == nombre:
            print("Error: ese usuario ya existe.")
            return

    # Guardar usuario
    usuarios.append({"nombre": nombre, "contraseña": contraseña, "tipo": tipo})
    print("Usuario registrado con éxito.")

def login():
    nombre = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # Buscar usuario en la lista
    encontrado = None
    for u in usuarios:
        if u["nombre"] == nombre:
            encontrado = u
            break

    if encontrado is None:
        print("Error: el usuario no está registrado.")
    elif encontrado["contraseña"] == contraseña:
        print(f"Login exitoso. Bienvenido {encontrado['tipo']} {nombre}.")
    else:
        print("Error: contraseña incorrecta.")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

# Programa principal
menu()