# 1-Listar los alumnos por orden ascendente de apellido, si se repite, 
# ordenar por nombre. Mostrar legajo, nombre, apellido y edad 

estudiantes=[{
  "legajo": 1,
  "nombre": "Juan",
  "apellido": "Linarez",
  "edad": 21,
  "notas": [    8,    9,    6  ],
  "programa": { "nombre": "Ingenieria en Informatica", "nivel": "pregrado" },
  "grupos": [    {"nombre": "Club de Ajedrez","descripcion": "Grupo de jugadores de Ajedrez"},
    			{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia"}]
},
{
  "legajo": 2,
  "nombre": "Carla",
  "apellido": "Salas",
  "edad": 18,
  "notas": [    7,    5  ],
  "programa": {"nombre": "Medicina","nivel": "pregrado"},
  "grupos": [ {"nombre": "Club de Volleyball","descripcion": "Equipo de Volleyball de la universidad."} ]
},
{
  "legajo": 3,
  "nombre": "Jorge",
  "apellido": "Rodriguez",
  "edad": 31,
  "notas": [    4,    9,    6  ],
  "programa": {"nombre": "Ingenieria Civil","nivel": "postgrado"}
},
{
  "legajo": 4,
  "nombre": "Maria",
  "apellido": "Sandoval",
  "edad": 24,
  "notas": [   6,    7,    6,    5  ],
  "programa": {"nombre": "Ingenieria en Informatica","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia" }]
},
{
  "legajo": 5,
  "nombre": "William",
  "apellido": "Smith",
  "edad": 25,
  "notas": [    6,    5,    8  ],
  "programa": {"nombre": "Bachiller","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de PS4","descripcion": "Grupo de jugadores de Playstation 4"}]
},
{
  "legajo": 6,
  "nombre": "Juan",
  "apellido": "Gomez",
  "edad": 21,
  "notas": [   8,    9,    6  ],
  "programa": {"nombre": "Ingenieria en Informatica","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de Ajedrez","descripcion": "Grupo de jugadores de Ajedrez"},
  			{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia"} ]
},
{
  "legajo": 7,
  "nombre": "Maria",
  "apellido": "Cadenas",
  "edad": 18,
  "notas": [    5,    4  ],
  "programa": {"nombre": "Medicina","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de Volleyball","descripcion": "Equipo d eVolleyball de la universidad."}]
},
{
  "legajo": 8,
  "nombre": "Jorge",
  "apellido": "Ayala",
  "edad": 31,
  "notas": [    4,    9,    6  ],
  "programa": {"nombre": "Ingenieria Civil","nivel": "postgrado"}
},
{
  "legajo": 9,
  "nombre": "Luis",
  "apellido": "Sandoval",
  "edad": 24,
  "notas": [    5,    7,    6,    4  ],
  "programa": {"nombre": "Ingenieria en Informatica","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia" }]
},
{
  "legajo": 10,
  "nombre": "Marcos",
  "apellido": "Rojo",
  "edad": 29,
  "notas": [    6,    8,    7  ],
  "programa": {"nombre": "Bachiller","nivel": "pregrado"},
  "grupos": [{"nombre": "Club de PS4","descripcion": "Grupo de jugadores de Playstation 4"}]
}
]


print(estudiantes[9]["grupos"][0]["descripcion"])


# 1-Listar los alumnos por orden ascendente de apellido, si se repite,  --------------------------------
# ordenar por nombre. Mostrar legajo, nombre, apellido y edad 


def listar(lista:dict):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j]["apellido"] > lista[j+1]["apellido"]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

            elif lista[j]["apellido"] == lista[j+1]["apellido"]:
                if lista[j]["nombre"] > lista[j+1]["nombre"]:
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
    mostrar(lista)




def mostrar(lista:list):
    for elementos in lista:
        print(f'''Legajo: {elementos["legajo"]}
Nombre: {elementos["nombre"]}
Apellido: {elementos["apellido"]}
Edad: {elementos["edad"]}
        ''')

                    
# listar(estudiantes)


# Obtener el promedio de notas para cada estudiante    -------------------------------------

def sacar_promedio(lista:list):
  for estudiante in lista:
      acumulador = 0
      for nota in estudiante["notas"]:
        acumulador += nota
      promedio = acumulador /len(estudiante["notas"])    
      print(f"El promedio de {estudiante['nombre']} es: {promedio}")
    
        
# sacar_promedio(estudiantes)


# def buscar_edades(lista:dict):
#     for estudiante in lista:
#       print(f"La edad de {estudiante['nombre']} es: {estudiante['edad']} ")
       
        
                

# buscar_edades(estudiantes)


# 3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el  ---------------------
# programa de “Ingenieria en Informatica” 

def buscar_estudiantesing(lista:list):
    for estudiante in lista:
      if estudiante["programa"]["nombre"] == "Ingenieria en Informatica":
        mostrar([estudiante])      


# buscar_estudiantesing(estudiantes)



# 4-Obtener un promedio de edad de los estudiantes.  ----------

def obtener_promedio(lista: list):
  acumulador = 0
  contador = 0
  for estudiantes in lista:
    acumulador += estudiantes["edad"]
    contador += 1
    promedio = acumulador / contador
  print(f"El promedio de edades es: {promedio}")


# obtener_promedio(estudiantes)    
   
     
# 5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y 
# apellido

def sacar_promedio(lista:list):
  promedio_max = 0
  estudiante_max = ""

  for estudiante in lista:
      acumulador = 0
      for nota in estudiante["notas"]:
        acumulador += nota
      promedio = acumulador /len(estudiante["notas"])
      
      if promedio > promedio_max:
         promedio_max = promedio
         estudiante_max = estudiante["nombre"]
  print(f"El mayor promedio es de {estudiante_max} con: {promedio_max}")
            
      
     

# sacar_promedio(estudiantes)



# 6-Listar nombre y apellido de los alumnos que forman el grupo “Club de 
# Informática” con sus respectivos promedios

def listar(lista:list):
    for estudiante in lista:
      if estudiante["grupos"]["nombre"] == "Club de Informatica":
        mostrar_lis([estudiante])      

       
    
def mostrar_lis(lista:dict):
   for estudiante in lista:
      print(f'''Nombre: {estudiante["nombre"]}
Apellido: {estudiantes["apellido"]}


''')                
 
   
# listar(estudiantes)   

