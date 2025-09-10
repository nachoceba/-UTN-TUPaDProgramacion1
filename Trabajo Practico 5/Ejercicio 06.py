"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros."""

lista = []

for i in range(10,31,5):

    lista.append(i)

print(lista[0:2])