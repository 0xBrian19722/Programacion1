contador_m = 0
nombre_mayor = ""
tecnologia_mayor = ""
contador_porcentaje = 0
total_encuestas = 10
mayor_edad_masculino = -1

for i in range(total_encuestas):
    print("--Bienvenidos a la encuesta de UTN TECHNOLOGYS--")
    nombre = input("Por favor ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese género, masculino o femenino: ")
    while genero != "masculino" and genero != "femenino":
        genero = input("Error, por favor ingrese con la palabra masculino o femenino: ")

    app = input("Ingrese la aplicación a votar: a: (IA) b: (RV/RA) c: (IOT): ")

    match app:
        case "a":
            tecnologia = "IA"
        case "b":
            tecnologia = "RV/RA"
        case "c":
            tecnologia = "IOT"
    if genero == "masculino" and (app == "a" or app == "c") and 25 <= edad <= 50:
        contador_m += 1
    if app != "a" and (genero != "femenino" or (edad > 33 and edad < 40)):
        contador_porcentaje += 1
    if genero == "masculino" and edad > mayor_edad_masculino:
        mayor_edad_masculino = edad
        nombre_mayor = nombre
        tecnologia_mayor = tecnologia
porcentaje = (contador_porcentaje / total_encuestas) * 100

print(f"Los que votaron por IOT o IA y cuya edad está entre 25 y 50 años inclusive: {contador_m}")
print(f"El porcentaje de empleados que no votaron por la IA es: {porcentaje}%")
print(f"El empleado masculino de mayor edad es {nombre_mayor}, con {mayor_edad_masculino} años, que votó por {tecnologia_mayor}.")



      

  




              
       
 
        

#hacer las listas de la app, terminar el calculo final del punto c-3
     
