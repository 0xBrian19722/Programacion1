# lista = [1,2,3,3]
# tuplas = ("hola",5,False) #ordenada , es inmutable: no se puede modificar
# sett = set({2,2,5,5,"hola"}) # desordenada, es mutable, sin repeticiones, se agregan elementos con add sett.add() (nombre de la varibla + .add) (con .remove los mismo)
# diccionario = {1:"Brian", 2:"Gerk", 3:"Nelsin"} # no tiene orden y es mutable (Key : value). Para modificar un valor se llama al diccionario y a su key por ejemplo diccionario[1] = "Leo". 
#                                                 # Para ver um valor del diccionario se lo llama por la key: print(diccionaio[1])


# casteo = set(lista)
# print(casteo)


#la funcion item me duevelve una lista de tuplas


user_dict = {'id': 1, 'nombre': 'nicolas', 'apellido': 'garcia', 'pais': 'argentina', 'dni': 37564333}

def agregar_diccionario(diccionario: dict, clave: str, valor) -> dict:
    diccionario[clave] = valor
    return user_dict

clave = input("Ingrese la clave: ")
Value = input("Ingrese el valor: ")

print(agregar_diccionario(user_dict,clave,Value))

