def mostrar_heroes(lista: list) -> None:
    for i in range(len(lista)):
        print("Nombre:", lista[i][0], "\n",
              "Identidad:", lista[i][1], "\n",
              "Empresa:", lista[i][2], "\n",
              "---------------------------")


def es_numero(cadena: str) -> bool:
    if cadena == "":
        return False
    punto = 0
    for i in range(len(cadena)):   
        caracter = cadena[i]
        if caracter == ".":
            punto += 1
            if punto > 1:   
                return False
        elif caracter < "0" or caracter > "9":
            return False
    return True         


def agregar_heroe(lista) -> None:
    nombre = input("Nombre: ")
    identidad = input("Identidad: ")

    bandera = True
    while bandera:
        empresa = input("Empresa (DC Comics / Marvel Comics): ")
        if empresa == "DC Comics" or empresa == "Marvel Comics":
            bandera = False
        else:
            print("Error: la empresa debe ser 'DC Comics' o 'Marvel Comics'.")
            
    bandera = True
    while bandera:
        altura_str = input("Altura: ")
        if es_numero(altura_str):
            altura = float(altura_str)
            bandera = False
        else:
            print("Error: la altura debe ser un numero válido.")

    bandera = True
    while bandera:
        peso_str = input("Peso: ")
        if es_numero(peso_str):
            peso = float(peso_str)
            bandera = False
        else:
            print("Error: el peso debe ser un numero válido.")

    bandera = True
    while bandera:
        fuerza_str = input("Fuerza: ")
        if es_numero(fuerza_str):
            fuerza = int(fuerza_str)
            bandera = False
        else:
            print("Error: la fuerza debe ser un número válido.")

    genero = input("Genero (M/F/NB): ")
    ojos = input("Color de ojos: ")
    pelo = input("Color de pelo: ")
    inteligencia = input("Inteligencia (low/average/good/high/genius): ")

    if nombre != "" and identidad != "" \
       and altura > 0 and peso > 0 and fuerza > 0 \
       and (genero == "M" or genero == "F" or genero == "NB") \
       and (inteligencia == "low" or inteligencia == "average" or inteligencia == "good" \
            or inteligencia == "high" or inteligencia == "genius"):
        lista.append([nombre, identidad, empresa, altura, peso, genero,
                      ojos, pelo, fuerza, inteligencia])
        print("Héroe agregado con éxito.\n")
    else:
        print("Datos inválidos, no se agregó el héroe.\n")
    
    

    


        

def eliminar_heroe(lista) -> None:
    nombre = input("Ingrese el nombre a eliminar: ")
    for i in range(len(lista)):
        if lista[i][0] == nombre:
            lista.pop(i)
            print("Héroe eliminado.\n")
            break
    else:   
        print("No se encontró el héroe.\n")

def ordenar_por_nombre(lista)->None:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][0] > lista[j][0]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print("Lista ordenada por nombre.\n")

def heroe_mas_alto(lista)->None:
    mayor = lista[0]
    for h in lista:
        if h[3] > mayor[3]:
            mayor = h
    print(f"\nHéroe más alto:\n"
          f"Nombre: {mayor[0]}\n"
          f"Identidad: {mayor[1]}\n"
          f"Empresa: {mayor[2]}\n"
          f"Altura: {mayor[3]} cm\n")

def heroe_mas_fuerte(lista)->None:
    mayor = lista[0]
    for h in lista:
        if h[8] > mayor[8]:
            mayor = h
    print(f"\nHéroe más fuerte:\n"
          f"Nombre: {mayor[0]}\n"
          f"Identidad: {mayor[1]}\n"
          f"Empresa: {mayor[2]}\n"
          f"Fuerza: {mayor[8]}\n")

def heroe_menos_pesado(lista)-> None:
    menor = lista[0]
    for h in lista:
        if h[4] < menor[4]:
            menor = h
    print(f"\nHéroe menos pesado:\n"
          f"Nombre: {menor[0]}\n"
          f"Identidad: {menor[1]}\n"
          f"Empresa: {menor[2]}\n"
          f"Peso: {menor[4]} kg\n")