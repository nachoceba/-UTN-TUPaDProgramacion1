"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Ejemplo:"""

agenda = {("Lunes", "09:00"): "Trabajo",
          ("Martes", "08:00"): "Turno barberia",
          ("Miercoles", "12:00"): "Almuerzo con abuela",
          ("Jueves", "22:00"): "Cena con amigos",
          ("Viernes", "23:00"): "Fiesta con amigos",
          ("Sabado", "13:00"): "Trabajo",
          ("Domingo", "14:00"): "Almuerzo familia",}


dia = input("Ingrese el dia que quiera saber que actividad tiene: ")

for (cuando,hora), actividad in agenda.items():

    if dia == cuando:
        print(f"En el dia {dia} a las {hora}, tenes la siguiente actividad: {actividad}")
