"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

def tabla_multiplicar(numero):

    print(f"La tabla de multiplicar del numero {numero}, quedaria asi:")

    for i in range(0,11):

        print(f"{i} * {numero} = {i * numero}")



print("HOLA BIENVENIDO")
print("----------------")

numero = int(input("Ingrese el numero que quiera saber su tabla de multiplicar hasta 10: "))

tabla_multiplicar(numero)