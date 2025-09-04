"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

num = int(input("Ingrese un numero "))
contador_digitos = 0

while num >= 1:

    num = num // 10

    contador_digitos += 1

print(contador_digitos)