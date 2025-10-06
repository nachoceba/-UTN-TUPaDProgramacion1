"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe."""


numeros_telefonicos = {"Nacho": "2617026601", "Dai": "2615597032", "Majo": "2613890044", "Matias": "2617114789", "Momo": "2617778899"}

nombre = input("Ingresa el nomnbre de la persona que desee su numero: ")

encontro = False

for clave,valor in numeros_telefonicos.items():

    if nombre == clave:
        print(f"El numero de {clave}: {valor}")

        encontro = True


if encontro == False:
    print("El nombre de la persona ingresada no ha sido encontrado")
