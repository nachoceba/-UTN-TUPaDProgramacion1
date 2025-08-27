"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

edad = int(input("Ingresa tu edad "))

if edad >= 18:
    print("Es mayor de edad")

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""

nota = int(input("Ingresa tu nota "))

if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")


"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""

numero = int(input("Ingrese un numero par "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Porfavor ingrese un numero par")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años."""

edad = int(input("Ingresa tu edad porfavor "))

if edad<12:
    print("Eres un niño")

elif edad>=12 and edad<18:
    print("Eres un adolescente")

elif edad >= 18 and edad < 30:
    print("Eres un adulto joven")

else:
    print("Eres un adulto mayor")

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string."""

contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres ")

longitud = len(contraseña)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña valida")

else:
    print("Porfavor ingrese una contraseña de entre 8 y 14 caracteres")

"""6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:"""

from statistics import mode, median, mean

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda =mode (numeros_aleatorios)

mediana = median (numeros_aleatorios)

media = mean (numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")

elif media < mediana and mediana < moda:
    print("Sesgo negativo")

elif media == mediana and mediana == moda:
    print("Sin sesgo")

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla."""

palabra = input("Ingrese una frase o palabra: ")
longitud = len(palabra)
letra = palabra[longitud-1] 
letra = letra.lower() 
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    palabra = palabra + "!" 
print(palabra)

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

nombre = input("Ingrese su nombre ")
print(" Ingrese 1 si desea su nombre en mayusculas ")
print(" Ingrese 2 si desea su nombre en minisculas ")
num = int(input("Ingrese 3 si quiere solo la primera letra de su nombre en mayusculas "))

if num == 1:
    nombre = nombre.upper()
    print(f"El nombre te queda tal que asi, {nombre}")
elif num == 2:
    nombre = nombre.lower()
    print(f"El nombre te queda tal que asi, {nombre}")

elif num == 3:
    nombre = nombre.title()
    print(f"El nombre te queda tal que asi, {nombre}")

else:
    print("Opcion incorrecta")


"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

terremoto = int(input("Ingrese la magnitud del terremoto: "))

if terremoto < 3:
    print("Muy leve, (imperceptible).")

elif terremoto >=3 and terremoto < 4:
    print("Leve,(ligeramente perceptible). ")

elif terremoto >=4 and terremoto < 5:
    print("Moderado, (sentido por personas, pero generalmente no causa daños).")

elif terremoto >= 5 and terremoto < 6:
    print("Fuerte, (puede causar daños en estructuras débiles).")

elif terremoto >=6 and terremoto < 7:
    print("Muy Fuerte,(puede causar daños significativos). ")

elif terremoto > 7:
    print("Extremo, (puede causar graves daños a gran escala).")


"""10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

"""10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = input("En cuál hemisferio se encuentra (N/S)? ")
mes = input("En que mes del año se encuentra? ")
dia = int(input("En que dia del mes se encuentra? "))
mes = mes.lower()
hemisferio = hemisferio.upper()
if (mes == "diciembre" and dia >= 21 and dia <= 31) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20 and dia > 0):
    if hemisferio == "N":
        print("Invierno")
    elif hemisferio == "S":
        print("Verano")
elif (mes == "marzo" and dia >= 21 and dia <=31) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20 and dia > 0):
    if hemisferio == "N":
        print("Primavera")
    elif hemisferio == "S":
        print("Otoño")
elif (mes == "junio" and dia >= 21 and dia <= 30) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20 and dia > 0):
    if hemisferio == "N":
        print("Verano")
    elif hemisferio == "S":
        print("Invierno")
elif (mes == "septiembre" and dia >= 21 and dia < 30) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20 and dia > 0):
    if hemisferio == "N":
        print("Otoño")
    elif hemisferio == "S":
        print("Primavera")
else:
    print("Ingrese los datos nuevamente")









