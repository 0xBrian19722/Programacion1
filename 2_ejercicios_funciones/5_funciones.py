# Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la 
# función Restar en sus 4 combinaciones. 
#  Restar1(int, int)->int: 
#  Restar2()->int: 
#  Restar3(int, int): 
#  Restar4(): 

def restar1(numero:int, numero2:int)->int:
    return numero - numero2
    
def restar2() -> int:
    numero = int(input("Ingrese un numero: "))
    numero2= int(input("Ingrese otro numero: "))
    return numero - numero2

def restar3(numero:int, numero2:int):
    resta = numero - numero2
    print(f"La resta es: {resta}")


def restar4():
    numero = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    print("La resta es:", numero - numero2)





resultado1 = restar1(10, 4)
print("Restar1:", resultado1)

resultado2 = restar2()
print("Restar2:", resultado2)

restar3(15, 5)

restar4()

