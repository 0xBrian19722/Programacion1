import json

with open("archivos/que.json", "r") as archivo:
    dato = json.load(archivo)


nuevo = ({
        "nombre" : "Cristian",
        "apellido": "Gonzalez"

},
{
        "nombre" : "Maxi",
        "apellido": "Gonzalez"

})

dato.append(nuevo)


with open("archivos/que.json", "w") as archivo:
    json.dump(dato,archivo, indent=4)                             #funcion que agrega el diccionario nuevo

# for gente in dato:
#     print(gente)
#     print("-----")
   