Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
           "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_por_nombre(nombres: list, edades: list):
  
    for i in range(len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            if nombres[i] > nombres[j]:

                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux
              
                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux
    return nombres, edades
                
nombres_ordenados, edades_ordenadas = ordenar_por_nombre(Nombres, Edades)

print(nombres_ordenados)
print(edades_ordenadas)



