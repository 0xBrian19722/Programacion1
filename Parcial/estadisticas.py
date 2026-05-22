def heroe_mas_alto(lista)->None:
    '''brief: Muestra el heroe con mayor altura.
       lista: Lista de heroes.
       retorno: No retorna nada.
    '''
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

    '''brief: Muestra el héroe con mayor fuerza.
       lista: Lista de héroes.
       retorno: No retorna nada.
    '''
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
    '''brief: Muestra el héroe con menor peso.
       lista: Lista de héroes.
       retorno: No retorna nada.
    '''
    menor = lista[0]
    for h in lista:
        if h[4] < menor[4]:
            menor = h
    print(f"\nHéroe menos pesado:\n"
          f"Nombre: {menor[0]}\n"
          f"Identidad: {menor[1]}\n"
          f"Empresa: {menor[2]}\n"
          f"Peso: {menor[4]} kg\n")    