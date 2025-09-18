"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""

def calcular_area_circulo(radio):

    area = 3.14 * radio**2

    return print(f"El area del circulo es {area}")


def calcular_perimetro_circulo(radio):

    perimetro = 2 * 3.14 * radio
    
    return print(f"El perimetro del circulo es {perimetro}")


print("HOLA BIENVENIDO")
print("----------------")

radio = float(input("Porfavor ingrese un radio: "))

calcular_perimetro_circulo(radio)

calcular_area_circulo(radio)

