"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

num1 = int(input("Ingrese un primer numero: "))

num2 = int(input("Ingrese un segundo numero: "))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1 + 1, num2): 
    suma += i

print(f"La suma de todos los números enteros entre {num1} y {num2} es: {suma}")

