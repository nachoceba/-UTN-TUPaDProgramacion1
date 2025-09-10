"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range."""

lista = [] 

for i in range(0,101):
    if i % 4 == 0:
        lista.append(i)
    else:
        continue

print("La lista con los numeros del 1 al 100 multiplos de 4 quedaria asi: ")

print(lista)

