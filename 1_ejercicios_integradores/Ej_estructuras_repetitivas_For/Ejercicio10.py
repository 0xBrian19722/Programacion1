n = int(input("Ingrese un número: "))
flag = True   

for i in range(2, n):
    if n % i == 0:        
        flag = False 
        break             

if n <= 1:
    print(n, "No es primo")
elif flag:            
    print(n, "Es primo")
else:
    print(n, "No es primo")