# -UTN-TUPaDProgramacion1
"""Este es mi primer repositorio"""
"""Subo práctica unidad"""

"""1)"""
print("hola mundo")
numero = 78
print (numero)

"""2)"""

nombre = input("Ingresa tu nombre ")
print (f"Hola {nombre}!")

"""3)"""
nombre = input("Ingresa tu nombre ")
apellido = input("Ingresa tu apellido ")
edad = input("Ingresa tu edad ")
residencia = input("Ingresa tu residencia ")
print(f"Soy {nombre} {apellido} tengo {edad} y vivo en {residencia}")

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro."""

radio = int(input("Ingresa el radio "))
area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio
print(f"El area de tu circulo es {area} y su perimetro es {perimetro}")

"""5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale."""

segundos = int(input("Ingrese una cantidad de segundos "))
hora = segundos / 3600

print(f"La cantidad de horas para los segundos ingresados es {int(hora)}")

"""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""

numero = int(input("Ingrese un numero entero "))

print( f"La tabla del {numero} es ")
print( f"1 x {numero} = {1*numero}")
print( f"2 x {numero} = {2*numero}")
print( f"3 x {numero} = {3*numero}")
print( f"4 x {numero} = {4*numero}")
print( f"5 x {numero} = {5*numero}")
print( f"6 x {numero} = {6*numero}")
print( f"7 x {numero} = {7*numero}")
print( f"8 x {numero} = {8*numero}")
print( f"9 x {numero} = {9*numero}")
print( f"10 x {numero} = {10*numero}")

"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""

numero1 = int(input("Ingrese un primer numero, DISTINTO DE 0. "))
numero2 = int(input("Ingrese un segundo numero, DISTINTO DE 0. "))

suma = numero1 + numero2
resta1 = numero1 - numero2
resta2 = numero2 - numero1
dividir1 = numero1/ numero2
dividir2 = numero2 / numero1
multiplicar = numero1 * numero2

print(f"La suma de los numeros es {suma}")
print(f"La primera variante de la resta es {resta1}")
print(f"La segunda variante de la resta es {resta2}")
print(f"La primera variante de la division es {dividir1}")
print(f"La segunda variante de la division es {dividir2}")
print(f"La multiplicacion de los numeros es {multiplicar}")

"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:"""

altura = int(input("Ingrese su altura en centimetros " ))
peso = int(input("Ingrese su peso en kilogramos " ))

altura = altura * 0.01

imc = peso / (altura * altura)

print(f"Tu indice de masa corporal es de {imc}")

"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia """

temperaturacelsius = float(input("Ingrese una temperatura en grados celsius y te dare el equivalente en fahrenheit"))

temperaturafaren = (9 / 5) * temperaturacelsius + 32

print(f"La temperatura ingresada en farenheit es {temperaturafaren}")

"""10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números."""

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los 3 numeros ingresados es {promedio}")
