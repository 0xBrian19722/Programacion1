# Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los 
# guarde en una lista y la retorne.  El programa principal debe invocar a la función y 
# mostrar por pantalla el retorno.


def pedir_lista():
    nombres = []
    for i in range(10):
        nombre = input("Ingrese el nombre: ")
        nombres.append(nombre)
    return nombres

lista = pedir_lista()

print(f"la lista de nombres es {lista}")

