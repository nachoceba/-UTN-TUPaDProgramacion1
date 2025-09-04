"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

num = int(input("Ingrese un numero distinto de 0 y los sumo en secuencia: "))

suma = 0

while num != 0:

    print("Si quiere detener la suma en la proxima ponga 0 ")

    suma += num
    
    num = int(input("Ingrese otro numero  y lo sumo en secuencia: "))

print(suma)