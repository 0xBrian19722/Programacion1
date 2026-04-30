# Define una función que encuentre el máximo de tres números. 
# La función debe aceptar tres argumentos y devolver el número más grande.



def max(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3 
    return (f"El numero mas grande es {max} ") 
  

print(max(5, 7, 2))