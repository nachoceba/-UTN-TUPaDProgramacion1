"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno."""


alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)


for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} - Notas: {notas} - Promedio: {promedio}")