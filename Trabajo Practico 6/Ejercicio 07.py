"""7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

def operaciones_basicas(a, b):

    suma = a + b

    resta = a - b
    resta2 = b - a

    division = a / b
    division2 = b / a

    multiplicacion = a * b

    lista_num= (suma,resta,resta2,division,division2,multiplicacion)

    for i in range(0,6):
        if i == 0:
          print(f"{a} + {b} = {lista_num[i]}")

        if i == 1:
           print(f"{a} - {b} = {lista_num[i]}")

        if i == 2:
           print(f"{b} - {a} = {lista_num[i]}")

        if i == 3:
           print(f"{a} / {b} = {lista_num[i]}")

        if i == 4:
           print(f"{b} / {a} = {lista_num[i]}")

        if i == 5:
           print(f"{a} * {b} = {lista_num[i]}")

    return


print("HOLA BIENVENIDO")
print("----------------")

a = float(input("Porfavor ingrese el primer numero: "))

b = float(input("Porfavor ingrese el segundo numero: "))


operaciones_basicas(a, b)