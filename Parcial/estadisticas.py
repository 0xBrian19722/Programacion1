def buscar_mas_alto(lista: list) -> None:
    '''brief: Muestra el heroe con mayor altura.
       lista: Lista de heroes.
       retorno: No retorna nada.
    '''
    mayor = lista[0]   
    for i in range(len(lista)):   
        if lista[i][3] > mayor[3]:   
            mayor = lista[i]         
    print(f"\nHeroe mas alto:\n"
          f"Nombre: {mayor[0]}\n"
          f"Identidad: {mayor[1]}\n"
          f"Empresa: {mayor[2]}\n"
          f"Altura: {mayor[3]} cm\n")
    
def buscar_mas_fuerte(lista: list) -> None:
    '''brief: Muestra el héroe con mayor fuerza.
       lista: Lista de héroes.
       retorno: No retorna nada.
    '''
    mayor = lista[0]   
    for i in range(len(lista)):   
        if lista[i][8] > mayor[8]:   
            mayor = lista[i]         
    print(f"\nHeroe mas fuerte:\n"
          f"Nombre: {mayor[0]}\n"
          f"Identidad: {mayor[1]}\n"
          f"Empresa: {mayor[2]}\n"
          f"Fuerza: {mayor[8]}\n")

def buscar_menos_pesado(lista: list) -> None:
    '''brief: Muestra el heroe con menor peso.
       lista: Lista de heroes.
       retorno: No retorna nada.
    '''
    menor = lista[0]   
    for i in range(len(lista)):   
        if lista[i][4] < menor[4]:   
            menor = lista[i]        
    print(f"\nHeroe menos pesado:\n"
          f"Nombre: {menor[0]}\n"
          f"Identidad: {menor[1]}\n"
          f"Empresa: {menor[2]}\n"
          f"Peso: {menor[4]} kg\n")   