# La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes 
# para la cocina de Industrias Wayne. Realizar el algoritmo que permita ingresar los datos de una compra de 
# ingredientes para preparar comida al por mayor. En total, sabemos que se realizarán 10 compras de ingredientes.
# Se registra por cada compra:
# 1. PESO: (entre 10 y 100 kilos)
# 2. PRECIO POR KILO: (mayor a 0 [cero]).
# 3. TIPO VARIEDAD: (vegetal, animal, mezcla).

# Además, tener en cuenta que si compro más de 100 kilos en total tengo un 15% de descuento sobre el precio bruto, 
# o si compro más de 300 kilos en total, tengo un 25% de descuento sobre el precio bruto.
# Se desea saber:
# A. El importe total a pagar, BRUTO sin descuento.
# B. El importe total a pagar con descuento (Solo si corresponde).
# C. Informar el tipo de alimento más caro.
# D. El promedio de precio por kilo en total.



contador = 0
total_kilo = 0
total_bruto = 0
total_descuento = 0
animal = 0
vegetal = 0
mezcla = 0

while contador < 10:
    kilo = (int(input("ingrese el peso: ")))
    precioxk = (int(input("Ingrese el precio por kg: ")))
    variedad = (str(input("ingrese la variedad: a = animal, b = vegetal c= mezcla")))
    if variedad == "a":
        animal  += 1
    elif variedad == "b":
        vegetal += 1
    elif mezcla == "c":
        mezcla += 1       

    total_bruto1 = kilo * precioxk
    total_kilo += kilo + total_kilo
    total_bruto += total_bruto1 + total_bruto
  

    contador += 1


if total_kilo > 300: 
    total_descuento = total_bruto * 0.75  
if total_kilo > 100:
    total_descuento = total_bruto * 0.85 







