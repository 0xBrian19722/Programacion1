#  Desarrollar una función que reciba por parámetro, una lista de números 
# y un número especificado.  La misma debe buscar el número especificado en la lista 
# y retornar “True” si existe.

lista = [1, 3, 4, 10, 21]
numero = 3

def buscar_numero(lista:list,num:int)->bool:
    for i in range(len(lista)):
        if lista[i] == num:
            return True
    return False
        


print(buscar_numero(lista,numero))

