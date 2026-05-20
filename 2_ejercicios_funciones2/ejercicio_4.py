# Crea una función que verifique si un número dado es par o impar. La función retorna 
# True si el número es par, False en caso contrario. 

def verificar(numero:int):
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False  
    return (resultado)    

numero = 5
print (verificar(numero))