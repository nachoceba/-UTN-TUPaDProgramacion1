def gestionNotas1 (alumnos):
   
   print("===================================")

   print("Usted a ingresado al apartado gestion notas")
   
   for legajo, datos in alumnos.items():
    nombre = datos["nombre"]
    materias = datos["materias"]
    print(f"ALUMNO: {nombre}")

    for i in range(len(materias)):
        print("-------------------------------------------")
        print(f"Notas de {materias[i][0]} del alumno {nombre}")

        # Nota 1
        materias[i][1] = float(input(f"Ingrese la nota 1 de {materias[i][0]}: "))
        while materias[i][1] <= 0 or materias[i][1] >= 11:
            materias[i][1] = float(input(f"Ingrese una nota válida para {materias[i][0]}: "))

        # Nota 2
        materias[i][2] = float(input(f"Ingrese la nota 2 de {materias[i][0]}: "))
        while materias[i][2] <= 0 or materias[i][2] >= 11:
            materias[i][2] = float(input(f"Ingrese una nota válida para {materias[i][0]}: "))

        # Promedio
        materias[i][3] = (materias[i][1] + materias[i][2]) / 2

        print(f"El promedio en {materias[i][0]} es {materias[i][3]}")



        if i == len(materias) - 1:
           break

    

   return(alumnos)