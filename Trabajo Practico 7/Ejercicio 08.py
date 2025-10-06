"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe"""


productos = {"Ajo": 8,"Tomate": 4,"Limon": 2}


print("BIENVENIDO A LA VERDULERIA QUE DESEA HACER")

print("----------------------------------")
print(" 1 si desea consultar el stock de algun producto")
print(" 2 si desea agregar unidades al stock de algun producto")
print(" 3 si desea agregar un nuevo producto")
print("Si desea salir del programa ingrese 4")

opcion = int(input("Ingrese la opcion: "))

while opcion != 1 and opcion != 2 and opcion != 3:
  opcion = int(input("Ingrese una opcion valida (1,2,3) "))

entro = False

if opcion == 1 :
  producto = input("Ingrese el producto del que quiere revisar su stock: ")

  for clave, valor in productos.items():
    if producto == clave:
      print(f"El stock del {clave}: {valor}")
      print("Has salido del sistema, vuelva pronto")
      print(productos)
      entro = True
      break

  if entro == False:
      print("El producto ingresado no esta en la lista, desea añadirlo?")
      si_no = input("Ingrese S para añadirlo Y N para salir" )
      if si_no == "s" or si_no == "S":
        unidades = int(input("Ingrese la cantidad de unidades que le quiere poner al producto nuevo"))
        productos[producto] = unidades
        print("La lista renovada quedaria tal que asi: ")
        print(productos)
      else:
        print("HAS SALIDO DEL SISTEMA, VUELVA PRONTO")


if opcion == 2 :
  producto = input("Ingrese el producto del que quiere rellenar su stock: ")
  unidades = int(input("Ingrese la cantidad de unidades que quiere agregar: "))
  
  for clave, valor in productos.items():
    if producto == clave:
      valor = valor + unidades
      print(f"El stock renovado del {clave}: {valor}")
      print("Has salido del sistema reinicielo para hacer otra operacion")
      entro = True
      break


  if entro == False:
      print("El producto ingresado no esta en la lista, desea añadirlo? ")
      si_no = input("Ingrese S para añadirlo Y N para salir ")
      if si_no == "s" or si_no == "S":
        productos[producto] = unidades
        print("La lista renovada quedaria tal que asi: ")
        print(productos)
      else:
        print("HAS SALIDO DEL SISTEMA, VUELVA PRONTO")


if opcion == 3:
  print("La lista de productos es esta, agregue productos que no esten en la lista")
  print(productos)
  print("--------------------------------------------")
  producto = input("Ingrese el nombre del nuevo producto: ")
  unidades = int(input("Ingrese la cantidad de unidades que le quiere poner al producto nuevo: "))
  productos[producto] = unidades

  print("Has salido del sistema, vuelva pronto")
  print(productos)


if opcion == 4:
  print("HAS SALIDO DEL SISTEMA, VUELVA PRONTO")

  print(productos)
