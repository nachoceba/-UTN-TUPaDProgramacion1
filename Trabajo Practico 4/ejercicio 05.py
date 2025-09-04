"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

numero = int(input("Ingrese un numero del 0 al 9: "))

numero_aleatorio = random.randint(0, 9)

while numero != numero_aleatorio:
  
  print("NO ACERTASTE SIGUE INTENTANDOLO!")

  numero = int(input("Ingrese un numero del 0 al 9: "))


print("FELICIDADES!!!!!! GANASTE EL JUEGO ADIVINASTE EL NUMERO ALEATORIO")

