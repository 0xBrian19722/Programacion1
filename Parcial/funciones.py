def mostrar_heroes(lista):
    print(f"{'N°':<6}{'Nombre':<20}{'Identidad':<25}{'Empresa':<20}")
    print("-" * 75)
    for i, h in enumerate(lista, start=1):
        print(f"Heroe {i:<2}:  {h[0]:<20}{h[1]:<25}{h[2]:<20}")


def agregar_heroe(lista):
    nombre = input("Nombre: ")
    identidad = input("Identidad: ")
    empresa = input("Empresa (DC Comics / Marvel Comics): ")
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    genero = input("Género (M/F/NB): ")
    ojos = input("Color de ojos: ")
    pelo = input("Color de pelo: ")
    fuerza = int(input("Fuerza: "))
    inteligencia = input("Inteligencia (low/average/good/high/genius): ")

    if nombre != "" and identidad != "" and empresa in ["DC Comics","Marvel Comics"] \
       and altura > 0 and peso > 0 and fuerza > 0 \
       and genero in ["M","F","NB"] \
       and inteligencia in ["low","average","good","high","genius"]:
        lista.append([nombre, identidad, empresa, altura, peso, genero,
                      ojos, pelo, fuerza, inteligencia])
        print("Héroe agregado con éxito.\n")
    else:
        print("Datos inválidos, no se agregó el héroe.\n")

def eliminar_heroe(lista):
    nombre = input("Ingrese el nombre a eliminar: ")
    encontrado = False
    for i in range(len(lista)):
        if lista[i][0] == nombre:
            lista.pop(i)
            encontrado = True
            print("Héroe eliminado.\n")
            break
    if not encontrado:
        print("No se encontró el héroe.\n")

def ordenar_por_nombre(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][0] > lista[j][0]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print("Lista ordenada por nombre.\n")

def heroe_mas_alto(lista):
    mayor = lista[0]
    for h in lista:
        if h[3] > mayor[3]:
            mayor = h
    print(f"\nHéroe más alto:\n"
          f"Nombre: {mayor[0]}\n"
          f"Identidad: {mayor[1]}\n"
          f"Empresa: {mayor[2]}\n"
          f"Altura: {mayor[3]} cm\n")

def heroe_mas_fuerte(lista):
    mayor = lista[0]
    for h in lista:
        if h[8] > mayor[8]:
            mayor = h
    print(f"\nHéroe más fuerte:\n"
          f"Nombre: {mayor[0]}\n"
          f"Identidad: {mayor[1]}\n"
          f"Empresa: {mayor[2]}\n"
          f"Fuerza: {mayor[8]}\n")

def heroe_menos_pesado(lista):
    menor = lista[0]
    for h in lista:
        if h[4] < menor[4]:
            menor = h
    print(f"\nHéroe menos pesado:\n"
          f"Nombre: {menor[0]}\n"
          f"Identidad: {menor[1]}\n"
          f"Empresa: {menor[2]}\n"
          f"Peso: {menor[4]} kg\n")