"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad"""

with open("productos.txt", "w") as archivo:
    
    archivo.writelines([
        "Manzana,150,20\n",
        "Banana,100,35\n",
        "Naranja,120,25\n"
    ])

"""2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30"""

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()


for linea in lineas:
    
    nombre, precio, cantidad = linea.strip().split(",")

    
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
"""

print("¿Desea agregar algun nuevo producto?")

print("Ingrese S para ingresar un nuevo producto o N para salir del programa")

opcion = input()

while opcion != "N" and opcion != "n":

    print("-------------------------------------------------------------------------------")

    print("Ingrese el nombre del nuevo producto: ")

    nuevoproducto = input()

    print("Ingrese el precio de su nuevo producto: ")

    precioproducto = int(input())

    print("Ingrese la cantidad de su nuevo producto: ")

    cantidadproducto = int(input())

    with open("productos.txt", "a") as archivo:
       archivo.write(f"{nuevoproducto},{precioproducto},{cantidadproducto}\n")
       print("Producto agregado exitosamente.")

    print("¿Desea agregar algun nuevo producto?")
    opcion = input("Ingrese S para ingresar un nuevo producto o N para salir del programa: ")

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()


for linea in lineas:
    
    nombre, precio, cantidad = linea.strip().split(",")
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad."""

diccionario = {}
listadiccionarios = []

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    
     productos = linea.strip().split(",")
     diccionario ={ productos[0]: {productos[1] : productos[2]}}

     listadiccionarios.append(diccionario)

print(listadiccionarios)

"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
"""

print("Ingrese el nombre del producto que desea buscar: ")
busqueda = input()
validacion = False

for diccionario in listadiccionarios:

    if busqueda in diccionario:
        print(f"El producto {busqueda} fue encontrado. Sus datos son: {diccionario}")
        validacion = True
        break

if validacion == False:
    print(f"ERROR, el producto {busqueda}, no fue encontrado.")



"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista."""


with open("productos.txt", "w") as archivo:
    for linea in lineas:
        archivo.write(linea)