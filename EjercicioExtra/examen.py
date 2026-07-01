# Dada la siguiente lista de diccionarios:  

# productos = [
#    {"nombre": "Mouse", "precio": 1500},
#    {"nombre": "Teclado", "precio": 3000},
#    {"nombre": "Monitor", "precio": 25000},
#    {"nombre": "Auriculares", "precio": 1800}
# ]

# Hacer una funcion que reciba una lista de diccionarios como la de arriba y un numero_maximo, y 
# cuya funcionalidad sea que muestre únicamente los nombres de los productos cuyo precio sea mayor al parámetro

# Nota: Indicar como comentario en el programa los parámetros formales, los parámetros actuales y la invocación. Documentar la función



productos = [
    {"nombre": "Mouse", "precio": 1500},
    {"nombre": "Teclado", "precio": 3000},
    {"nombre": "Monitor", "precio": 25000},
    {"nombre": "Auriculares", "precio": 1800}
]


def filtrar_productos(lista:list,maximo:int)->None:
    '''
    brief: muestra los nombres de los productos con
    el precio mayor al maximo dado como parametro, 
    reciviendo como parametro una lista y un entero.
    '''
    for producto in lista:
        if producto["precio"] > maximo:
            print(producto["nombre"])

# parametros formales: lista, numero_maximo
# parametros actuales: productos, 2000
# invocacion: filtrar_productos()
   



filtrar_productos(productos,1700)
