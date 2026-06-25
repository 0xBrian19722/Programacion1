# 4) Hacer una validación de que la key que ingresa el usuario existe antes de 
# eliminarlo o agregarlo (ya que si elimina sin verificar rompe y si agrega y, por 
# ejemplo, ya existe, no crea sino que modifica)

user = {

 "id" : 1 ,
 "nombre" : "Nicolas",
 "apellido" : "Garcia",
 "nacionalidad" : "Argentina",
 "dni" : 37564333



} 

def eliminar_elemento(lista:dict):
    print(lista)
    
    clave_eliminar = input("Ingrese la clave a eliminar: ")
    bandera = verificar_clave(lista,clave_eliminar)
    
    if bandera == True:
        lista.pop(clave_eliminar)
        print(f"El/La {clave_eliminar} se elimino correctamente..\n")  
        
    else:
        bandera == False
        print("Clave no encontrada..\n")     

    return lista







def agregar_elemento(lista:dict):
 
    clave = input("Agregar la clave: ")
    bandera = verificar_clave(lista,clave)


    if bandera == False:
        valor = input("Ingrese el valor: ")
        lista[clave] = valor
    else:
        print("Ya existe la clave ingresada")
    print(lista)        



  




def verificar_clave(lista:dict,clave:str):
    bandera = False
    for key in lista:
        if key ==  clave:
            bandera = True
    return bandera        


eliminar_elemento(user)
print(user)





# def eliminar_elemento(lista:dict):
#     print(lista)
#     bandera = False
#     clave_eliminar = input("Ingrese la clave a eliminar: ")
#     for clave in lista:
#         if clave_eliminar  == clave:
#             bandera = True
#             if bandera == True:
#                 lista.pop(clave_eliminar)
#                 print(f"El/La {clave_eliminar} se elimino correctamente..\n")  
#                 break
#     if bandera == False:
#         print("Clave no encontrada..\n")   












