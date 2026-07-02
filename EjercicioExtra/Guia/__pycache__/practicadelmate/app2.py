import json

def leer_json():
    with open("practicadelmate/juegos.json", "r") as archivo:
        datos = json.load(archivo)
        return (datos)



def eliminar_dato(datos):
    eliminar = input("Ingrese un juego a eliminar: ")
    for i in range (len(datos)):
        if datos[i]["titulo"] == eliminar:
            datos.pop(i)
            print("\njuego eliminado\n")
            break
            
            

def guardar_json(datos):
    with open("practicadelmate/juegos.json","w") as archivo:
        json.dump(datos , archivo, indent=4)


def cambiar_puntaje(datos):
    cambiar = input("ingrese el nombde del juego a cambiar el puntaje: ")
    for i in range (len(datos)):
       if datos[i]["titulo"] == cambiar:
            print("El puntaje es:", datos[i]["puntaje"])
            nuevo_puntaje = int(input("Ingrese nuevo puntaje: "))
            datos[i]["puntaje"] = nuevo_puntaje
            print("Ahora es: ",datos[i]["puntaje"])
            


lista_juegos = leer_json()



# for i in range (len(lista_juegos)):
#     print (lista_juegos[i])
#     print ("-----")

# # cambiar_puntaje(lista_juegos)  
# # guardar_json(lista_juegos)  


# for i in range (len(lista_juegos)):
#     print (lista_juegos[i])
#     print ("-----")



leer_json()


