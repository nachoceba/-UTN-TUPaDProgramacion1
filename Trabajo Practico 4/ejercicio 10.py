"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = int(input("Ingresa un número: "))
inverso = int(str(numero)[::-1])
print("El número invertido es:", inverso)
