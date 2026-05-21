Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura",
           "Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad",
           "Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]

Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_nombres_puntos(nombres: list, puntos: list):
    # Ordenamiento burbuja
    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            # Si el nombre en i es mayor al de j → intercambio
            if nombres[i] > nombres[j]:
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

                aux = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux
            # Si los nombres son iguales → ordenar por puntos descendente
            elif nombres[i] == nombres[j] and puntos[i] < puntos[j]:
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

                aux = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux

    return nombres, puntos

# Ejemplo de uso
nombres_ordenados, puntos_ordenados = ordenar_nombres_puntos(Nombres, Puntos)

print(nombres_ordenados)
print