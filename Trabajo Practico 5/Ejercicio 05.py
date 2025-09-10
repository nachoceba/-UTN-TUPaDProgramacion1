"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza."""

numeros = [8, 15, 3, 22, 7]

numeros.remove(max(numeros))

print(numeros)

#Lo que pasa es que esta funcion max con el uso del remove elimina el valor mas grande de la lista.