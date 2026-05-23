# Crear una función llamada temperatura_media_alta(temperaturas, umbral) que reciba una lista de temperaturas (en grados-int) y un valor umbral.

# La función debe calcular el promedio de las temperaturas y decir si ese promedio es mayor que el umbral.

# Debe retornar True si lo es, y False si no.

# Datos a usar de Ejemplo:
# Salida esperada= True





def temperatura_media_alta(temperaturas: list, umbral: int) -> bool:
    suma_temp = 0
    for i in range(len(temperaturas)):  
        suma_temp += temperaturas[i]     
    promedio = suma_temp / len(temperaturas)  
    return promedio > umbral  




temperaturas = [18, 22, 25, 20, 21]
umbral = 20

print(temperatura_media_alta(temperaturas,umbral))

