# op = 0
# total = 0
# while op != 4:
#     print("1.- PC Razen $800.000")
#     print("2.- LGTV 55 Pulgadas $450.000")
#     print("3.- Parlante JBL Pure Sound $90.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     op = int(input())
#     match op:
#         case 1:
#             print(f"Tiene que pagar {800000 * 1.19}")
#             total += 800000 * 1.19
#         case 2:
#             print(f"Tiene que pagar {450000 * 1.19}")
#             total += 450000 * 1.19
#         case 3:
#             print(f"Tiene que pagar {90000 * 1.19}")
#             total += 90000 * 1.19
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar es {total}")
#         case _:
#             print("Opcion invalida")

# def suma():
#     n1 = int(input("Escoja un numero: "))
#     n2 = int(input("Escoja otro numero: "))
#     print(f"El total es: {n1 + n2}")
# def resta():
#     n1 = int(input("Escoja un numero: "))
#     n2 = int(input("Escoja otro numero: "))
#     print(f"El total es: {n1 - n2}")
# def multiplicar():
#     n1 = int(input("Escoja un numero: "))
#     n2 = int(input("Escoja otro numero: "))
#     print(f"El total es: {n1 * n2}")
# def dividir():
#     n1 = int(input("Escoja un numero: "))
#     n2 = int(input("Escoja otro numero: "))
#     print(f"El total es: {n1 * n2}")
# def calculadora():
#     op = 0
#     while op != 5:
#         print("1.- Sumar")
#         print("2.- Restar")
#         print("3.- Multiplicar")
#         print("4.- Dividir")
#         print("5.- Salir")
#         op = int(input("Seleccione una opcion: "))
#         match op:
#             case 1:
#                 suma()
#             case 2:
#                 resta()
#             case 3:
#                 multiplicar()
#             case 4:
#                 dividir()
#             case 5:
#                 print("Saliendo")
#             case _:
#                 print("Opcion invalida")
# calculadora()

# def cuentaVocales():
#     n_vocales = 0
#     n_conso = 0
#     nombre = input("Ingrese su nombre: ")
#     for i in nombre:
#         if i in "aeiouAEIOU":
#             n_vocales += 1
#         else:
#             n_conso += 1
#     print(f"El numero de vocales es: {n_vocales}")
#     print(f"El numero de consonantes es: {n_conso}")

# def tablaM():
#     num = int(input("Ingrese un numero: "))
#     cont = 1
#     while cont <= 10:
#         print(f"{num} x {cont} = {num * cont}")
#         cont += 1

# def promedio():
#     n_notas = int(input("Ingrese el numero de notas: "))
#     suma = 0
#     for nota in range(n_notas):
#         nota = float(input("Ingrese una nota: "))
#         suma += nota
#     if n_notas > 0:
#         print(f"El promedio final es: {suma / n_notas}")
#     else:
#         print("No se ingresaron notas.")

# hacer una tabla de multiplicar con for
# num = int(input("Ingrese un numero: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")
# hacer una tabla de multiplicar con while
# num = int(input("Ingrese un numero: "))
# cont = 1
# while cont <= 10:
#     print(f"{num} x {cont} = {num * cont}")
#     cont += 1
# hacer una verificacion de edad con if
# edad = int(input("Ingrese su edad: "))
# if edad >= 18 and edad < 100:
#     print("Eres mayor de edad")
# elif edad < 18 and edad >= 1:
#     print("Eres menor de edad")
# elif edad == 0:
#     print("Guaren culiao")
# else:
#     print("WHERE IS OMNIMAN!!!!!")

# op = 0
# total_a_pagar = 0
# while op != 4:
#     print("Bienvenido")
#     print("1.- Manzanas $500")
#     print("2.- Naranjas $600")
#     print("3.- Sandia $2000")
#     print("4.- Salir")
#     op = int(input("Ingrese su opcion: "))
#     match op:
#         case 1:
#             print("Usted compro Manzanas")
#             total_a_pagar += 500
#         case 2:
#             print("Usted compro naranja")
#             total_a_pagar += 600
#         case 3:
#             print("Usted compro Sandia")
#             total_a_pagar += 2000
#         case 4:
#             print("Saliendo del sitstema")
#             print("Gracias por comprar")
#         case _:
#             print("Opcion invalida")
# print(f"El total a pagar es {total_a_pagar}")

# def sumar():
#     num1 = int(input("Ingrese un numero: "))
#     num2 = int(input("Ingrese otro numero: "))
#     suma = num1 + num2
#     print(f"El resultado es: {suma}")
# sumar()

# def dividir():
#     num1 = int(input("Ingrese un numero: "))
#     num2 = int(input("Ingrese otro numero: "))
#     div = num1 // num2
#     print(f"El resultado es: {div}")
# dividir()

import random
import time
# j1 = input("Ingrese su nombre: ")
# j2 = input("Ingrese su nombre: ")
# j3 = input("Ingrese su nombre: ")

# dado1 = random.randint(1,6)
# dado2 = random.randint(1,6)
# dado3 = random.randint(1,6)

# if dado1 > dado2 and dado1 > dado3:
#     print(f"El ganador es {j1} con {dado1} puntos")
#     print(f"La puntuacion de {j2} fue de {dado2}")
#     print(f"La puntuacion de {j3} fue de {dado3}")
# elif dado2 > dado3:
#     print(f"El ganador es {j2} con {dado2} puntos")
#     print(f"La puntuacion de {j1} fue de {dado1}")
#     print(f"La puntuacion de {j3} fue de {dado3}")
# else:
#     print(f"El ganador es {j3} con {dado3} puntos")
#     print(f"La puntuacion de {j1} fue de {dado1}")
#     print(f"La puntuacion de {j2} fue de {dado2}")

#Tienes que pedir dos peleadores con 100 de vida cada uno
# e ir restandole un golpe por cada turno
# el valor del golpe debe estar entre 7 y 15

j1 = "Alacran"
j2 = "Subcerro"
vida_j1 = 100
vida_j2 = 100
turno = 1
barra1 = "=" * vida_j1
barra2 = "=" * vida_j2
while vida_j1 > 0 and vida_j2 > 0:
    golpe1 = random.randint(7,15)
    golpe2 = random.randint(7,15)
    if turno % 2 == 0:
        print("Turno de Subcerro")
        time.sleep(1)
        vida_j1 = max(0, vida_j1 - golpe2)
        barra1 = "=" * vida_j1
        print(f"{j2} le quita {golpe2} a {j1}, vida restante: {vida_j1} {barra1}")
        turno -= 1
        time.sleep(2)
    else:
        print("Turno de Alacran")
        time.sleep(1)
        vida_j2 = max(0, vida_j2 - golpe1)
        barra2 = "=" * vida_j2
        print(f"{j1} le quita {golpe1} a {j2}, vida restante: {vida_j2} {barra2}")
        turno += 1
        time.sleep(2)
if vida_j1 > vida_j2:
    print(f"Alacran gana la batalla, con una vida restante de: {vida_j1} {barra1}")
else:
    print(f"Subcerro gana la batalla, con una vida restante de: {vida_j2} {barra2}")
