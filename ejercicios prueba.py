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

# while True:
    
#     print


















# Ejercicio 9

# Pida numeros infinitamente
# El Usuario puede escribir "fin" para terminar el programa
# Al final mostrar cuantos numeros ingreso y la suma total de ellos

# cantidad = 0
# suma = 0

# while True:
    
#     dato = input("Ingrese un numero o escriba fin: ")
    
#     if dato == "fin":
#         print("Saliendo del sistema")
#         break
    
#     try:
#         numero = int(dato)
        
#         cantidad += 1
#         suma += numero
    
#     except ValueError as er:


















# Nivel 4 - Ejercicios tipo prueba
# Ejercicio 10

# Haz un sistema de login, con un usuario fijo y contraseña fija
# Pedirle a la persona que ingrese el usuario y contraseña
# Seguir preguntando hasta que ambos sean correctos
# Si falla, mostrar "Datos incorrectos"
# Si acierta, mostrar "Acceso permitido"

# admin = "Hoplita"
# contraseña = "Wipig"

# while True:
#     usuario = input("Ingrese el usuario: ")
#     clave = input("Ingrese la contraseña: ")
    
#     if usuario == admin and clave == contraseña:
#         print("Bienvenido")
#         break
#     else:
#         print("Datos incorrectos")















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
# No permitir retirar mas dinero del disponible
# Validar numeros con try-except
# Repetir hasta salir

saldo = 100000

while True:
    print("1.- Ver saldo")
    print("2.- Depositar")
    print("3.- Retirar")
    print("4.- Salir")
    
    try:
        op = int(input("Ingrese su opcion: "))
        match op:
            case 1:
                print(f"El saldo total es de: {saldo}")
            case 2:
                monto = int(input("Ingrese el monto a depositar: "))
                saldo += monto
                print(f"El saldo actual es de: {saldo}")
            case 3:
                retiro = int(input("Ingrese el monto a retirar: "))
                if retiro > saldo:
                    print("Saldo insuficiente")
                else:
                    saldo -= retiro
                    print(f"El saldo actual es de: {saldo}")
            case 4:
                print("Saliendo del sistema")
                break
            case _:
                print("Opcion invalida")
    except ValueError as er:
        print("Ingrese solo numeros enteros")
        print(f"Error {er}")
                

























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

