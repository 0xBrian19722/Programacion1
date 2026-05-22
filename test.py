lista = [20, 50, 12, 56, 45, 12, 45]


def promediar(lista:list)->float:
    suma = 0
    for i in range(len(lista)):
       suma += lista[i]
    promedio = suma / len(lista)
    return promedio


print(promediar(lista))