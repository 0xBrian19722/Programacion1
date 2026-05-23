def mostrar_menu()->None:
    bandera = True
    while bandera:
     menu = int(input('''
          
        Menu de Opciones :

        1_  Listar los datoas de los usuarios de Mexico por nombre
        2_  Listar los datos de los usuarios mas joven
        3_  Mostar usuarios de México y Brasil cuyo codigo postal sea mayor a 8000     
        4_  Salir           
     '''))
     if menu == 1:
      listar_mexico()  
     if menu == 2:
       listar_edad() 
     if menu == 4:
       print("Saliendo...")
       bandera = False
               
          
          
          
          
          
print(mostrar_menu())   
    
    
def listar_mexico(lista:list)->list:
  for i in range(len(lista)):
    for j in range(len(lista)-1):
      if lista[j] > lista[j+1]:
        aux = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = aux      

  return lista    

def listar_edad(lista:list,edad:list) -> list:
  for i in range(len(lista)):
    for j in range(len(lista)-1):
      if edad[j] > edad[j+1]:
        aux = edad[j]
        edad[j] = edad[j+1]
        edad[j+1] = aux     

        aux = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = aux  

  return lista , edad
  