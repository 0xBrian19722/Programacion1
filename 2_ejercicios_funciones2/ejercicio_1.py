# Escribir una función que calcule el área de un rectángulo. La función recibe la base y 
# la altura y retorna el área. 

def calcular(numoero1:int,numero2:int)->int:
    area = (numoero1 * numero2) / 2 
    return area

print(calcular(10, 10))