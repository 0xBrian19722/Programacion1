# Solicitar al usuario que ingrese como mínimo 5 números. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
corte = ""
acu_numeros = 0

while corte != "00" or contador < 5:
    corte = input("Ingrese un numero, si desea terminar con el programa ingrese 00: ")
    if corte != "00":
        numero = int(corte)
        acu_numeros += numero
        contador += 1
    else:
        if contador < 5:
            print("Se necesita 5 ingresos como minimo")
            corte = ""
promedio = acu_numeros / contador
print (f"La suma de los numeros ingresado es {acu_numeros}, y el promedio es {promedio}")            
    
    
    
    


    







    
    


   
    

