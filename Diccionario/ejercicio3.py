# Al diccionario eliminarle un par clave valor (el usuario ingresará una clave y 
# debe borrarse del diccionario) (pop) 

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
    lista.pop(clave_eliminar)
    print(f"La clave {clave_eliminar} se elimino correctamente..\n")     

eliminar_elemento(user)
print(user)     


