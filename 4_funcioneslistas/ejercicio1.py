def pedir_lista():
    nombres = []
    for i in range(10):
        nombre = input("Ingrese el nombre: ")
        nombres.append(nombre)
    return nombres

lista = pedir_lista()

print(f"la lista de nombres es {lista}")