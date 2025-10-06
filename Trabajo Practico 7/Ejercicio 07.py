"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""


aprobados_p1 = set()
aprobados_p2 = set()


for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")

    parcial1 = float(input(f"Ingresá la nota del Parcial 1 de {nombre}: "))
    parcial2 = float(input(f"Ingresá la nota del Parcial 2 de {nombre}: "))

    if parcial1 >= 5:
        aprobados_p1.add(nombre)
    if parcial2 >= 5:
        aprobados_p2.add(nombre)


ambos = aprobados_p1 & aprobados_p2
solo_uno = aprobados_p1 ^ aprobados_p2
total = aprobados_p1 | aprobados_p2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos un parcial:", total)