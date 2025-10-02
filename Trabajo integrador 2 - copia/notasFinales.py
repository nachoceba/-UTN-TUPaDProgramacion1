def notasfinales(alumnos):
   mejor_nota_general = -1
   mejor_materia_general = None
   mejor_alumno = None

   promedio_final = 0

   for legajo, datos in alumnos.items():
      nombre = datos["nombre"]
      materias = datos["materias"]
        
      mejor_nota_personal = -1
      mejor_materia_personal = None

      for materia in materias:
         if materia[3] > mejor_nota_personal:
             mejor_nota_personal = materia[3]
             mejor_materia_personal = materia[0]

        # Mostrar mejor materia de este alumno
      print("-----------------------------------------------")
      print(f"ALUMNO: {nombre} → su asignatura más alta es {mejor_materia_personal} con nota {mejor_nota_personal}")

        # Comparar con mejor nota general
      if mejor_nota_personal > mejor_nota_general:
            mejor_nota_general = mejor_nota_personal
            mejor_alumno = nombre
            mejor_materia_general = mejor_materia_personal

   print("-----------------------------------------------")
   print(f"Y el mejor alumno es {mejor_alumno} con {mejor_nota_general} en {mejor_materia_general}")

   return (alumnos)
