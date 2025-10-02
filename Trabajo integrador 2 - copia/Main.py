from gestionNotas2 import gestionNotas1
from mostrarNotas import mostrarnotas
from notasFinales import notasfinales

materias1 = [
            ["Ciencias", "", "", ""],
            ["Historia", "", "", ""],
            ["Geografia", "", "", ""],
            ["Matematicas", "", "", ""],
            ["Fisica", "", "", ""],
              ]

materias2 = [
            ["Ciencias", "", "", ""],
            ["Historia", "", "", ""],
            ["Geografia", "", "", ""],
            ["Matematicas", "", "", ""],
            ["Fisica", "", "", ""],
              ]

materias3 = [
            ["Ciencias", "", "", ""],
            ["Historia", "", "", ""],
            ["Geografia", "", "", ""],
            ["Matematicas", "", "", ""],
            ["Fisica", "", "", ""],
              ]

materias4 = [
            ["Ciencias", "", "", ""],
            ["Historia", "", "", ""],
            ["Geografia", "", "", ""],
            ["Matematicas", "", "", ""],
            ["Fisica", "", "", ""],
              ]

alumnos = {
    60902: {"nombre": "Rodolfo Fernandez", "materias": materias1},
    61654: {"nombre": "Luis Gomez", "materias": materias2},
    61852: {"nombre": "Andrea Pereira", "materias": materias3},
    61754: {"nombre": "Juan Cruz Gonzales", "materias": materias4}
}

print("------------------------------------------")
print("Bienvenido al programa de las notas de sus alumnos ")
print("------------------------------------------")

print("A continuacion le doy las opciones a elegir: ")
print("a) Para gestionar las notas ")
print("b) Si desea ver las notas")
print("c) Ver notas finales alumnos")
print("d) Si desea salir del sistema")

opcion = input("Elija una opcion: ")

while opcion not in ["a","A","b","B","c","C","d","D"]:

    opcion = input("Ingrese una opcion valida porfavor: ")

if opcion == "d" or opcion == "D":
    print("HAS SALIDO DEL SISTEMA")

while opcion != "d" and opcion != "D":

    if opcion == "a" or opcion == "A":

        notasalumnos = gestionNotas1(alumnos) 

        opcion = input("Desea hacer otra operacion?: a) gestion notas, b) mostrar notas ,c) Ver nota final alumno o d) Salir ")
        while opcion not in ["a","A","b","B","c","C"]:
            opcion = input("Ingrese una opcion valida porfavor: ")

    if opcion == "b" or opcion == "B":

        mostrarnotas(alumnos)

        opcion = input("Desea hacer otra operacion?: a) gestion notas, b) mostrar notas ,c) Ver nota final alumno o d) Salir ")
        while opcion not in ["a","A","b","B","c","C"]:
            opcion = input("Ingrese una opcion valida porfavor: ")


    if opcion == "c" or opcion == "c":
        
        notasfinales(alumnos)
        opcion = input("Desea hacer otra operacion?: a) gestion notas, b) mostrar notas ,c) Ver nota final alumno o d) Salir ")
        while opcion not in ["a","A","b","B","c","C"]:
            opcion = input("Ingrese una opcion valida porfavor: ")
                           

    if opcion == "d" or opcion == "d":
        
        print("HAS SALIDO DEL SISTEMA")

        break





