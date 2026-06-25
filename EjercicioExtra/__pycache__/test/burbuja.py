lista = [5, 1, 2, 8, 7, 9]
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
           "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

for i in range(len(lista)-1):
    for j in range(len(lista)-1-i):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux



print(lista)