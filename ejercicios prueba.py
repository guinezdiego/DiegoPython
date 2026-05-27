
# deuda = 100000
# op = 0

# while op != 3:
#     print("1.- Pagar deudas")
#     print("2.- Comprar")
#     print("3.- Salir")
#     while True:
#         try:
#             op = int(input("Ingrese su opcion: "))
#             break
#         except ValueError as er:
#             print("Solo numeros enteros y positivos")

#     match op:
#         case 1:
#             print(f"El monto total de la deuda es de {deuda}")
#             while True:
#                 try:
#                     monto = int(input("Ingrese el monto a pagar: "))
#                     break
#                 except:
#                     print("Solo numeros enteros y positivos")
                
#             if monto >= 0 and monto <= deuda:
#                 deuda -= monto
#                 print(f"El total actual de la deuda es: {deuda}")
#             else:
#                 print("El monto debe ser mayor a 0 y menor o igual a la deuda a pagar")

#         case 2:
#             while True:
#                 try:
#                     compras = int(input("Ingrese la cantidad de compras: "))
#                     break
#                 except:
#                     print("Solo numeros enteros y positivos")
#             for i in range(compras):
#                 while True:
#                     try:
#                         monto = int(input("Ingrese el monto de la compra: "))
#                         break
#                     except:
#                         print("Solo numeros enteros y positivos")
#                 if monto >= 0:
#                     deuda += monto
#                 else:
#                     print("El pago debe ser mayor a 0")
        
#         case 3:
#             print("Saliendo del sistema")


# def menuCamiones():
#     op = 0
#     c_chicos = 0
#     c_medianos = 0
#     c_grandes = 0
#     suma = 0

#     while True:
#         try:
#             print("Seleccione una opcion: ")
#             print("1.- Ingresar camion")
#             print("2.- Mostrar totales")
#             print("3.- Mostrar cantidad de camiones")
#             print("4.- Mostrar capacidad total de los camiones")
#             print("5.- Ingrese la marca del camion")
#             print("6.- Salir")
#             op = int(input())
#             match op:
#                 case 1:
#                     while True:
#                         try:
#                             peso = int(input("Ingrese la capacidad del camion: "))
#                             if peso > 0:
#                                 suma += peso
                                
#                                 if 0 < peso <= 3:
#                                     print("El camion es chico")
#                                     c_chicos += 1
#                                 elif 4 <= peso <= 8:
#                                     print("El camion es mediano")
#                                     c_medianos += 1
#                                 else:
#                                     print("El camion es grande")
#                                     c_grandes += 1
#                                 break
#                             else:
#                                 print("Solo numeros enteros positivos")
#                         except ValueError as er:
#                             print("Solo numeros enteros positivos", er)
#                             break
#                 case 2:
#                     print(f"El total de camiones chicos son: {c_chicos}")
#                     print(f"El total de camiones grandes es: {c_medianos}")
#                     print(f"El total de camiones grandes es: {c_grandes}")

#                 case 3:
#                     print(f"La cantidad de camiones totales es: {c_chicos + c_grandes + c_medianos}")

#                 case 4:
#                     print(f"La capacidad total de los camiones es: {suma}")

#                 case 5:
#                     marca = input("Ingrese la marca: ")

#                     if 3<= len(marca) <= 8:
#                         print("Marca valida")
#                     else:
#                         print("Marca invalida")
#                 case 6:
#                     print("Saliendo del sistema")
#                     break
#                 case _:
#                     print("Opcion invalida")

#         except ValueError as er:
#             print(f"Error {er}")


# galeria = 100
# vistos = 0
# noVistos = 0
# while True:
#     try:
#         personas = int(input("Cuantas personas vinieron?: "))
#         break
#     except ValueError as er:
#         print("Solo numeros enteros")
#         print(f"Error {er}")

# for i in range(personas):
#     while True:
#         try:
#             cant = int(input("Cuantos cuadros vio?: "))
#             vistos += cant
#             noVistos += galeria - cant
#             break
#         except ValueError as er:
#             print("Solo numeros enteros")
#             print("Error: ", er)
# print(f"El total de cuadros vistos es: {vistos}")
# print(f"El total de cuadros no vistos es: {noVistos}")