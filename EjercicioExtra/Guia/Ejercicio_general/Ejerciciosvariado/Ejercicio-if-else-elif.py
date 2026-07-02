altura = int(input("Ingrese la altura en cm para determinar la posicion de jeugo: "))
if altura < 160:
    print ("Posicion Base")
if altura >= 160 and altura <= 179:
    print ("Posicion Escolta")
if altura >= 180 and altura <= 199:
    print ("Posicion Alero")
if altura >= 200:
    print ("Posicion Ala-Pivot o Pivot")
                 