"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra."""


frase = input("Porfavor ingrese una frase: ")

palabras = frase.split()

# Palabras únicas usando set
unicas = set(palabras)

# Contar cuántas veces aparece cada palabra
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(unicas)    

print(conteo)


