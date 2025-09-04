"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

num1 = int(input("Ingrese un primer numero: "))

suma = 0

for i in range(0 , num1+1): 
    suma += i

print(f"La suma de todos los números enteros entre 0 y {num1} es: {suma}")
