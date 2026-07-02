from juegos import *




def mostrar_precios(lista1:list)-> None:
    for i in range(len(lista1)):                # PUNTO 1
     print(f"Precio: {lista1[i]}")
        
def calcular_precio(lista:list)-> int:
    mas_caro = lista[0][1]
    juego = lista[0][0]
    for i in range(len(lista)):
        if lista[i][1] > mas_caro:           
           mas_caro = lista[i][1]
           juego = lista[i][0]

    print (f"EL precio del juego mas caro es {mas_caro} $ y se llama {juego}")

def agregar_juego(lista:list)->None:







    
   juego = input("Ingrese un juego: ")
   precio = int(input("Ingrese el precio: "))
   lista.append([juego,precio])
   print("Juego agregado con exito!\n")

def eliminar_juego(lista:list)->None:
   juego = input("Ingrese el juego a elimiar: ")
   for i in range(len(lista)):
        if juego == lista[i][0]:
            lista.pop(i)
            print("Juego eliminado con exito!")
            return
   else:
        print("Juego no encontrado...")    
        
def mostrar_lista(lista:list)->list:










   for i in range(len(lista)):
      print(f"Juego: {lista[i][0]}\nPrecio: {lista[i][1]} $\n----------------")
               

