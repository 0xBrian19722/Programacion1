#  Escribe una función que calcule el área de un círculo. La función debe recibir el radio 
# como parámetro y devolver el área. 

def calcular(radio:int)->int:
    area = 3.14 * radio**2
    return area

print(calcular(4))