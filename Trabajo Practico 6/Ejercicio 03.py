"""3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados."""


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


print("HOLA BIENVENIDO")
print("----------------")

nombre = input("Ingresa tu nombre: ")

apellido = input("Ingresa tu apellido: ")

edad = input("Ingresa tu edad: ")

residencia = input("Ingresa tu residencia: ")


informacion_personal(nombre, apellido, edad, residencia)