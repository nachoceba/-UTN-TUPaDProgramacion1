"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

i = 0

for i in range(100,0,-2):
    if i % 2 == 0:
        print(i)