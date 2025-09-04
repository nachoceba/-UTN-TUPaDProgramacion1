"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""


N = 5
suma = 0

for i in range(N):
    num = int(input(f"Ingrese el número entero {i+1}: "))
    suma += num


media = suma / N

# Mostrar el resultado
print(f"La media de los {N} números ingresados es: {media}")
