"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""


def segundos_a_horas(segundos):
     
     horas = segundos / 3600

     return print(f"La cantidad de horas para los segundos ingresados es: {horas:.1f}")


print("HOLA BIENVENIDO")
print("----------------")

segundos = int(input("Porfavor ingrese los segundos que quiera: "))

segundos_a_horas(segundos)