#  Al diccionario usuario, agregarle un par clave valor que el usuario quiera (el 
# usuario decidirá la clave y el valor) 

user = {

 "id" : 1 ,
 "nombre" : "Nicolas",
 "apellido" : "Garcia",
 "nacionalidad" : "Argentina",
 "dni" : 37564333



} 

def agregar_dato(lista:dict)->dict:
    clave = input("Ingrese la clave: ")
    valor = input(f"Ingrese {clave}: ")
    lista[clave] = valor
    print(lista)
    return lista
    

  


agregar_dato(user)




