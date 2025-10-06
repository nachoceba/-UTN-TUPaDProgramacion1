"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200

precios_frutas["Manzana"] = 1500

precios_frutas["Pera"] = 2300

print(precios_frutas)

print("------------------------")

print("PRECIOS MODIFICADOS")

precios_frutas["Banana"] = 1330

precios_frutas["Manzana"] = 1700

precios_frutas["Melon"] = 2800

print(precios_frutas)

print("--------------------------")

print("LISTA DE FRUTAS POR SU NOMBRE")

nombres_frutas = ["Banana", "Ananá", "Melon", "Uva", "Naranja", "Manzana" ,"Pera"]

print(nombres_frutas)