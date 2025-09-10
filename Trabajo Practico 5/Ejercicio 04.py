"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]"""


lista_animales = ["perro", "gato", "conejo", "pez"]

print(lista_animales)

longitudlista = len(lista_animales)

lista_animales[longitudlista-1] = "loro"

lista_animales[longitudlista-2] = "oso"

print(lista_animales)
