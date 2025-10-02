def mostrarnotas(alumnos):
    for legajo, datos in alumnos.items():
            print(f"\nLegajo: {legajo}")
            print(f"Alumno: {datos['nombre']}")
            print("Materias y notas:")
            for materia in datos["materias"]:
                nombre_materia = materia[0]
                notas = materia[1:]
                print(f"  {nombre_materia:<12} -> {notas}")

    return(alumnos)