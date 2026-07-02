
Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"] 
Apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa", "Ramirez", "Perez", "Lopez", "Arregui", "Mitre", "Andrade", "Loza", "Antares", "Roca", "Perez"]                
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8] 

def ordenar(apellido:list,estudiante:list,nota:list)-> list:
    for i in range(len(apellido)):
        for j in range(len(apellido)-1):
            if apellido[j] > apellido[j+1]:
                aux = apellido[j]
                apellido[j] = apellido[j+1]
                apellido[j+1] = aux
            elif apellido[j] == apellido[j+1] and estudiante[j] > estudiante [j+1]:
                aux = apellido[j]
                apellido[j] = apellido[j+1]
                apellido[j+1] = aux

                aux2 = estudiante[j]
                estudiante[j] = estudiante[j+1]
                estudiante[j+1] = aux2
            elif apellido[j] == apellido[j+1] and estudiante[j] == estudiante [j+1] and nota[j] < nota [j+1]:   
                aux = apellido[j]
                apellido[j] = apellido[j+1]
                apellido[j+1] = aux

                aux2 = estudiante[j]
                estudiante[j] = estudiante[j+1]
                estudiante[j+1] = aux2

                aux3 = nota[j]
                nota[j] = nota[j+1]
                nota[j+1] = aux3

    return (f"Apellidos: {apellido}\nNombres: {estudiante}\nNotas: {nota}\n")

print(ordenar(Apellidos,Estudiantes,Nota))

                



         
            


    