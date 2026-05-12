# Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango 
# especificado, validar los números solicitados dentro de ese rango, guardar en una 
# lista y retornarla.  El programa principal debe invocar a la función y mostrar por 
# pantalla el retorno. 

def lista_numeros_validacion():
    lista = []
    min = 1
    max = 50
    for i in range(4):   
        numero = int(input("Ingrese un número entre 1 y 50: "))
        while not (min <= numero <= max):  
            print("Error: número fuera de rango")
            numero = int(input("Ingrese un número entre 1 y 50: "))
        lista.append(numero)
    return lista

print(lista_numeros_validacion())


