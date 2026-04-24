# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota
#  es ...


n1 = int(input("Ingrese la primera nota: "))
n2 = int(input("Ingrese la segunda nota: "))
nota = n1 + n2

if nota > 5 and nota < 11:
    print(f"Promocion directa, la nota es = {nota}")
elif nota > 3 and nota < 6:
    print(f"Aprobado, la nota es = {nota}")
elif nota > 0 and nota < 4:
    print(f"Desaprobado, la nota es = {nota}")
else:
    print(nota)

    

