def sumar_naturales(numero: int) -> int:
    if numero == 1:            
        return 1
    else:                       
        return numero + sumar_naturales(numero - 1)
    


numero = int(input("Ingrese un numero: "))
resultado = sumar_naturales(numero)

print(f"la suma de los primeros {numero} numeros naturales es {resultado}")