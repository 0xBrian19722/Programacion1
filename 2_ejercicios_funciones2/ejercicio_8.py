

def mostrar_primos(hasta: int) -> int:
    contador = 0
    for num in range(2, hasta + 1):      
        es_primo = True
        for i in range(2, num):         
            if num % i == 0:
                es_primo = False         
        if es_primo:
            print(num)
            contador += 1
    return contador


mostrar_primos(20)