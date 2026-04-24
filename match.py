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
#     n_notas = int(input("Ingrese el numero de notas"))
#     suma = 0

