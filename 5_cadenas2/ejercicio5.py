def quitar_vocales(cadena: str) -> str:
    nueva_cadena = ""   

    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter != "a" and caracter != "e" and caracter != "i" and caracter != "o" and caracter != "u":   
            nueva_cadena = nueva_cadena + caracter
    return nueva_cadena
    
           
print(quitar_vocales("programacion")) 




