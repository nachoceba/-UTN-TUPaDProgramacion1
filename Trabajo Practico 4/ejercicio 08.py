"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

num = 0
par = 0
impar = 0
negativos = 0
positivos = 0
cantidadnums = 0

while cantidadnums <= 4:
    num = int(input("Ingrese un numero "))

    if num % 2 == 0:
        par += 1
    else:
        impar += 1

    if num > 0:
        positivos += 1
    else:
        negativos += 1

    cantidadnums += 1


print(f"La cantidad de numeros pares es: {par}")

print(f"La cantidad de numeros impares es: {impar}")

print(f"La cantidad de numeros positivos es: {positivos}")

print(f"La cantidad de numeros negativos es: {negativos}")