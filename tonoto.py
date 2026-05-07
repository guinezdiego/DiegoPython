# import random
# import time
# num = random.randint(1, 10)
# print(num)

# for i in range(num):
#     print("Hola Diego")

# dado = random.randint(1, 6)
# print("El dado salio", dado)
# ejercicio 1
#  
#ejercicio 2

# dado1 = random.randint(1, 6)
# dado2 = random.randint(1, 6)
# print(f"Dado 1 es igual a: {dado1} y dado 2 es igual a: {dado2}")

# if dado1 == dado2:
#     print("Te vas a la carcel")
# else:
#     print("Puedes pasar")

# strike = random.randint(10, 70)

# if strike > 50:
#     print(f"Es un golpe critico. daño: {strike}")
# else:
#     print(f"No es muy eficiente. daño: {strike}")

# golpe1 = random.randint(60, 190)
# golpe2 = random.randint(60, 190)
# golpe3 = random.randint(60, 190)

# j1 = "Cristiano"
# j2 = "Dembele"
# j3 = "Messi"

# if golpe1 > golpe2 and golpe1 > golpe3:
#     print(f"El golpe mas fuerte fue de {j1} de un total de {golpe1}")
# elif golpe2 > golpe3:
#     print(f"El golpe mas fuerte fue de {j2} de un total de {golpe2}")
# else:
#     print(f"El golpe mas fuerte fue de {j3} de un total de {golpe3}")

# turno = 1

# j1 = input("Ingrese el nombre del peleador 1: ")
# j2 = input("Ingrese el nombre del peleador 2: ")

# vida_j1 = 100
# vida_j2 = 100

# golpe1 = random.randint(7, 18)
# golpe2 = random.randint(7, 18)


# while vida_j1 > 0 and vida_j2 > 0:
#     if turno % 2 == 0:
#         print("Turno 1")
#         time.sleep(1)
#         print(f"El jugador {j1} golpeo a {j2}, vida actual de {j2} es {vida_j2 - golpe1}")
#         vida_j2 -= golpe1
#         turno -= 1
#         time.sleep(1)
#     else:
#         print("Turno 2")
#         time.sleep(1)
#         print(f"El jugador {j2} golpeo a {j1}, vida actual de {j1} es {vida_j1 - golpe2}")
#         vida_j1 -= golpe2
#         turno += 1
#         time.sleep(1)

# if vida_j1 > vida_j2:
#     print(f"El ganador es: {j1}")
# else:
#     print(f"El ganador es: {j2}")

import random, time
# num = random.randint(1, 9)

# while abs(-3) != num:
#     print(num)
#     time.sleep(1)
#     num = random.randint(1, 9)

# n1 = int(input("Ingrese el valor de limite inferior: "))
# n2 = int(input("Ingrese el valor de limite superior: "))
# while n2 <= n1:
#     print("Parametros incorrectos")
#     n2 = int(input("Ingrese el valor de limite superior: "))
# print("Parametros correctos")
# num = random.randint(n1, n2)
# print(num)
# lata = 0
# plancha = 0
# pecesCap = random.randint(10, 20)
# print(f"El total de pescados capturados fue: {pecesCap}")
# time.sleep
# for i in range(pecesCap):
#     peso = random.randint(300, 3000)
#     if peso <= 800:
#         lata += 1
#     elif peso >= 801 and peso <= 3000:
#         plancha += 1
#     else:
#         print("Peso invalido")
# time.sleep(2)
# print(f"El total de peces en lata son {lata}")
# time.sleep(2)
# print(f"El total de peces en plancha son {plancha}")

gramos = random.randint(1, 3000)
sodio = random.randint(1, 100)
vender = random.randint(1, 2)

if gramos > 0 and gramos <= 500:
    tamaño = "normal"
elif gramos <= 1500:
    tamaño = "mediana"
elif gramos >= 1501:
    tamaño = "grande"

if sodio >= 5 and sodio <= 8:
    tipo = "especial"
elif sodio >= 9:
    tipo = "acorazada"
else:
    tipo = ""

sticker = ""
if vender == 1:
    sticker = " con sticker sanitario"

print(f"Lata {tamaño} {tipo}{sticker}")