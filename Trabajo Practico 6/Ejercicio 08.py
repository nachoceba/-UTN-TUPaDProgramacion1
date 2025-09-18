"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""

def calcular_imc(peso, altura):

    print("Vamos a calcular tu IMC")
    print("----------------------------------------------------------")
    print("Los rangos del IMC (Índice de Masa Corporal) según la OMS son:")
    print("Menos de 18.5 → Bajo peso")
    print("18.5 – 24.9 → Peso normal")
    print("25 – 29.9 → Sobrepeso")
    print("30 – 34.9 → Obesidad grado I")
    print("35 – 39.9 → Obesidad grado II")
    print("40 o más → Obesidad grado III (obesidad mórbida)")
    print("-----------------------------------------------------------")

    imc = peso / altura**2

    return print(f"Dado su peso y altura tu IMC es de: {imc}")

print("HOLA BIENVENIDO")
print("----------------")

peso = int(input("Ingrese su peso en kilogramos porfavor: "))

altura = float(input("Ingrese su altura en metros porfavor: "))

calcular_imc(peso, altura)