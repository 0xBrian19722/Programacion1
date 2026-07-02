# Ejercicio 5: Dadas las siguientes listas: 
# Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
# ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las 
# personas de menor edad (puede ser más de una) y las retorne.  El programa 
# principal deberá mostrar nombre y edad de los menores. 


Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 

Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 

def buscar_menor_edad(nombres: list, edades: list):
    menor = edades[0]   
    for i in range(1, len(edades)):
        if edades[i] < menor:
            menor = edades[i]   

    resultado = []   
    for i in range(len(edades)):
        if edades[i] == menor:
            resultado.append((nombres[i], edades[i]))

    return resultado

personas = buscar_menor_edad(Nombres, edades)

for nombre, edad in personas:
    print(f"{nombre} tiene {edad} años")
