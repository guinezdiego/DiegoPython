# Nivel 1 while True


# Ejercicio 1 
# Haz un programa que pida un numero
# Si el numero es mayor que 10
# Mostrar "Numero valido"
# Y terminar el programa
# Si no, volver a pedirlo

# while True:
#     numero = int(input("Ingrese un numero: "))
    
#     if numero > 10:
#         print("Numero valido")
#         break
#     else:
#         print("El numero debe se mayor a 10")
        

# Ejercicio 2
# Crea una contraseña fija
# Pide al usuario ingresar la contraseña
# Mientras sea incorrecta, mostrar "Contraseña incorrecta"
# Cuando sea correcta, mostrar "Bienvenido"

# while True:
#     contraseña = input("Ingrese la contraseña: ")
    
#     if contraseña == "Wipig67":
#         print("Bienvenido :)")
#         break
#     else:
#         print("Contraseña incorrecta")

# Ejercicio 3
# Pide una palabra, si la palabra es "salir", termina el bucle
# Si no, mostrar la palabra escrita por el usuario y repetir

# while True:
#     palabra = input("Ingrese la contraseña: ")
    
#     if palabra == "salir":
#         print("Programa terminado")
#         break
#     else:
#         print(palabra)
        
# Nivel 2 try-except y ValueError
# Ejercicio 4
# Pide un numero entero
# Si el usuario escribe texto, mostrar el error
# Si escribe bien el numero, mostrar el doble y terminar el programa

# while True:
#     try:
#         numero = int(input("Ingrese un numero: "))
        
#         print(f"El doble es: {numero * 2}")
#         break
#     except ValueError as er:
#         print("Ingrese solo numeros enteros")
#         print(er)

# Ejercicio 5

# Pide dos numeros y mostrar la suma
# Si el usuario escribe letras, mostrar "Debes ingresar numeros"














# Ejercicio 6

# Pida la edad del usuario
# Si escribe letras, mostrar el error
# Si la edad es negativa, mostrar "edad invalida"
# Si todo esta correcto, mostrar la edad y terminar el programa










# Nivel 3 Mezclando todo
# Ejercicio 7

# Pide un numero
# Validar con try-except
# Mostrar la tabla de multiplicar de ese numero del 1 al 10










# Ejercicio 8

# Crea un menu con: 1.- Saludar, 2.- Decir adios, 3.- Salir
# Usando while True
# Mostrar "Hola", "Adios" y "Saliendo del sistema" segun la opcion
# Si escribe letras mostrar el error










# Ejercicio 9

# Pida numeros infinitamente
# El Usuario puede escribir "fin" para terminar el programa
# Al final mostrar cuantos numeros ingreso y la suma total de ellos










# Nivel 4 - Ejercicios tipo prueba
# Ejercicio 10

# Haz un sistema de login, con un usuario fijo y contraseña fija
# Pedirle a la persona que ingrese el usuario y contraseña
# Seguir preguntando hasta que ambos sean correctos
# Si falla, mostrar "Datos incorrectos"
# Si acierta, mostrar "Acceso permitido"










# Ejercicio 11

# Pida un numero, validalo con try-except
# Mostrar si es par o impar
# Y mostrar si es positivo o negativo










# Ejercicio 12

# Haz una calculadora simple
# Con: 1.- Sumar, 2.- Restar, 3.- Multiplicar, 4.- Dividir y 5.- Salir
# Usar while True, validar numeros con try-except y usar break para salir










# Desafio final
# Ejercicio 13

# Haz un cajero automatico basico
# Con un saldo inicial de $100000
# Con un menu para ver saldo, depositar, retirar y salir
# No permitir reitrar mas dinero del disponible
# Validar numeros con try-except
# Repetir hasta salir

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


# def sumar():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))
#     return n1 + n2

# res = sumar()
# print(f"El resultado es: {res}")

# def saludo(name):
#     print(f"Hola {name}")

# saludo("Wipig")

# def halfPrice(precio):
#     print(f"El precio es: {precio / 2}")

# p = int(input("Ingrese el precio: "))

# halfPrice(p)

# def sumar(n1, n2):
#     return n1 + n2

# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))

# print(f"El resultado de la suma es: {sumar(num1, num2)}")



# Crear una calculadora con las 4 operaciones basicas

# def sumar(n1, n2):
#     return n1 + n2

# def restar(n1, n2):
#     return n1 - n2

# def multi(n1, n2):
#     return n1 * n2

# def divi(n1, n2):
#     return n1 / n2

# def calculadora():
#     while True:
#         print("1.- Sumar")
#         print("2.- Restar")
#         print("3.- Multiplicar")
#         print("4.- Dividir")
#         print("5.- Salir")
#         try:
#             op = int(input("Ingrese una opcion: "))

#             match op:
#                 case 1:
#                     while True:
#                         try:
#                             num1 = int(input("Ingrese un numero: "))
#                             num2 = int(input("Ingrese otro numero: "))
#                             print(f"La suma total es: {sumar(num1, num2)}")
#                             break
#                         except ValueError as Er:
#                             print("Solo debes ingresar numeros enteros")
#                             print(Er)
#                 case 2:
#                     while True:
#                         try:
#                             num1 = int(input("Ingrese un numero: "))
#                             num2 = int(input("Ingrese otro numero: "))
#                             print(f"La resta total es: {restar(num1, num2)}")
#                             break
#                         except ValueError as Er:
#                             print("Solo debes ingresar numeros enteros")
#                             print(Er)
#                 case 3:
#                     while True:
#                         try:
#                             num1 = int(input("Ingrese un numero: "))
#                             num2 = int(input("Ingrese otro numero: "))
#                             print(f"La multiplicacion total es: {multi(num1, num2)}")
#                             break
#                         except ValueError as Er:
#                             print("Solo debes ingresar numeros enteros")
#                             print(Er)
#                 case 4:
#                     while True:
#                         try:
#                             num1 = int(input("Ingrese un numero: "))
#                             num2 = int(input("Ingrese otro numero: "))

#                             while num2 == 0:
#                                 print("No se puede dividir por 0")
#                                 num2 = int(input("Ingrese otro numero: "))

#                             print(f"La division total es: {divi(num1, num2)}")
#                             break
#                         except ValueError as Er:
#                             print("Solo debes ingresar numeros enteros")
#                             print(Er)
#                 case 5:
#                     print("Saliendo del sistema")
#                     break
#                 case _:
#                     print("Opcion invalida")
#         except ValueError as Er:
#             print("Solo debes ingresar numeros enteros")
#             print(Er)
# calculadora()


# lista = [1, 2, 3, 4, 5]

# for i in lista:
#     print(i * 2)

# pokemons = ["Evee", "Vaporeon", "Psyduck", "Charizad"]

# for i in pokemons:
#     print(i.upper())

# frutas = ["Manzana", "Uva", "Pera", "Limon", "Platano"]

# for i in frutas:
#     if i[-1] == "a":
#         print(f"La fruta {i} termina con a")
#     else:
#         print(f"La fruta {i} no termina con a")