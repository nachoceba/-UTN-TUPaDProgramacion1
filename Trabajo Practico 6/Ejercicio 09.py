"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

def celsius_a_fahrenheit(celsius):

    farenheit = (celsius * 9/5) + 32 


    return print(f"La temperatura ingresada en celsius fue: {celsius}, y su equivalente en farenheit es: {farenheit}")



print("HOLA BIENVENIDO")
print("----------------")

celsius = int(input("Ingrese la temperatura en grados celsius porfavor: "))

celsius_a_fahrenheit(celsius)