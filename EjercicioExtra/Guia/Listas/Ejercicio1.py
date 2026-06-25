# Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los 
# guarde en una lista y la retorne.  El programa principal debe invocar a la función y 
# mostrar por pantalla el retorno.

def listas_nombre():
    nombres = []
    for i in range(10):
        nombre = input("Ingrese los nombres: ")
        nombres.append(nombre)
    return nombres    

lista = listas_nombre()
print(f"Los nombres ingresados son: {lista}")