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

# while True:
#     try:
#         num = int(input("Ingrese un numero: "))
        
#         for i in range(1, 11):
#             print(f"{num} x {i} = {num * i}")
            
#     except ValueError as Er:
#         print("Debes ingresar numeros enteros")
#         print(Er)
















# Ejercicio 8

# Crea un menu con: 1.- Saludar, 2.- Decir adios, 3.- Salir
# Usando while True
# Mostrar "Hola", "Adios" y "Saliendo del sistema" segun la opcion
# Si escribe letras mostrar el error

# while True:
#     print("1.- Saludar")
#     print("2.- Despedirse")
#     print("3.- Saliendo")
#     try:
#         op = int(input("Ingrese una opcion: "))
#         match op:
#             case 1:
#                 print("Hola weko")
#             case 2:
#                 print("Adios autista")
#             case 3:
#                 print("Saliendo del sistema")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except ValueError as Er:
#         print("Debes ingresar solo numeros enteros")
#         print(Er)














# Ejercicio 9

# Pida numeros infinitamente
# El Usuario puede escribir "fin" para terminar el programa
# Al final mostrar cuantos numeros ingreso y la suma total de ellos

# cantidad_numeros = 0
# suma = 0

# while True:
#     try:
#         num = input("Ingrese un numero: ")
        
#         if num == "fin":
#             print("Programa terminado")
#             break
        
#         num = int(num)
#         cantidad_numeros += 1
#         suma += num
#     except ValueError as Er:
#         print("Solo ingresar numeros enteros")
#         print(Er)

# print(f"La cantidad de numeros que ingreso fue: {cantidad_numeros}")
# print(f"La suma total de ellos es: {suma}")
        

















# Nivel 4 - Ejercicios tipo prueba
# Ejercicio 10

# Haz un sistema de login, con un usuario fijo y contraseña fija
# Pedirle a la persona que ingrese el usuario y contraseña
# Seguir preguntando hasta que ambos sean correctos
# Si falla, mostrar "Datos incorrectos"
# Si acierta, mostrar "Acceso permitido"

# user = "Hoplita"
# password = "Wipig"

# while True:
#     usuario = input("Ingrese el usuario: ")











# Ejercicio 11

# Pida un numero, validalo con try-except
# Mostrar si es par o impar
# Y mostrar si es positivo o negativo

# while True:
#     try:
#         num = int(input("Ingrese un numero: "))
        
#         if num % 2 == 0:
#             print("El numero es par")
#         else:
#             print("El numero es impar")
        
#         if num >= 1:
#             print("El numero es positivo")
#         elif num == 0:
#             print("El numero es 0")
#         else:
#             print("El numero es negativo")
#     except ValueError as Er:
#         print("Solo ingresar numeros enteros")
#         print(Er)
    











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

# saldo = 100000

# while True:
#     print("1.- Ver saldo")
#     print("2.- Depositar dinero")
#     print("3.- Retirar dinero")                
#     print("4.- Salir del sistema")
#     try:
#         op = int(input("Ingrese una opcion: "))
#         match op:
#             case 1:
#                 print(f"Su saldo total es de {saldo}")
#             case 2:
#                 dep = int(input("Ingrese el monto a depositar: "))
                
#                 while dep < 1:
#                     print("El deposito debe ser mayor a 0")
#                     dep = int(input("Ingrese el monto a depositar: "))
                
#                 saldo += dep
#                 print(f"El saldo actual es de {saldo}")
#             case 3:
#                 retirar = int(input("Ingrese el monto a retirar: "))
                
#                 while retirar > saldo:
#                     print("No puedes retirar mas de lo que tienes")
#                     retirar = int(input("Ingrese el monto a retirar: "))
                    
                    
#                 saldo -= retirar
#                 print(f"El saldo actual es: {saldo}")
#             case 4:
#                 print("Saliendo del sistema")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except ValueError as er:
#         print("Debes ingresar numeros enteros")
#         print(er)
        























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

# nombres = ["Diego", "Matias", "Fernando"]
# apellidos = ["Mussolini", "Hitler","Nigger"]

# for i in range(len(nombres)):
#     print(nombres[i], apellidos[i])

# no = input("Agregue un nombre: ")
# ap = input("Agregue un apellido: ")

# nombres.append(no)
# apellidos.append(ap)

# for i in range(len(nombres)):
#     print(nombres[i], apellidos[i])

# juguetes = ["yo-yo", "tetris"]

# def mostrar():
#     c = 1
#     for j in juguetes:
#         print(f"El juguete {c} es: {j}")
#         c += 1
#     print("-" * 20)

# def actualizar():
#     mostrar()
#     act = int(input("Ingrese el juguete a actualizar: "))
#     new_toy = input("Ingrese el nuevo juguete")
#     juguetes[act - 1] = new_toy

# def eliminar():
#     mostrar()
#     eliminar = int(input("Que juguete desea eliminar: "))
#     juguetes.pop(eliminar - 1)
#     print("Juguete eliminado")

# def agregar():
#     mostrar()
#     toy = input("Ingrese el juguete: ")
#     juguetes.append(toy)

# def menuJuguetes():
#     while True:
#         print("1.- Agregar juguete")
#         print("2.- Eliminar juguete")
#         print("3.- Actualizar juguete")
#         print("4.- Mostrar juguetes")
#         print("5.- Salir")
#         try:
#             op = int(input("Ingrese su opcion: "))
#             match op:
#                 case 1:
#                     agregar()
#                 case 2:
#                     eliminar()
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     print("Saliendo del sistema")
#                     break
#                 case _:
#                     print("Opcion invalida")
#         except ValueError as Er:
#             print("Debes ingresar numeros enteros")
#             print(Er)

# menuJuguetes()
# pares = []
# impares = []

# def validar_lista_numeros():
#     lista = input("Ingrese una lista de numeros separados por espacios: ")
#     lista_numeros = lista.split()   

#     for i in lista_numeros:
#         if int(i) % 2 == 0:
#             pares.append(i)
#         else:
#             impares.append(i)
    
#     print(f"Los numeros pares son: {pares}")
#     print(f"Los numeros impares son: {impares}")

# validar_lista_numeros()


# lista = [3, 56, 77, 67, 1]
# lista.sort(reverse = True)
# print(lista)

# Diccionario

# productosDicc = {
#     1:{"nombre": "Maracuya", "precio": 3000},
#     2:{"nombre": "Pera", "precio": 1500},
#     3:{"nombre": "Cebolla", "precio": 1200}
# }

# productosDicc[4] = {"nombre": "Piña", "precio": 3500}

# # suma = 0

# # for producto in productosDicc.values():
# #     suma += producto["precio"]
# # print(f"La suma total es: {suma}")

# carrito = []

# def agregarProducto():
#    print("Cual es el nombre del producto?")
#    nombre = input()
#    print("cual es el precio?")
#    precio = int(input())
#    nuevoKey=list(productosDicc.keys())
#    nuevoKey.sort()
#    productosDicc[nuevoKey[-1]+1]= {"nombre": nombre, "precio": precio}
# def MostrarProducto():
#    for key, producto in productosDicc.items():
#     print(f"{key} .{producto}")
# def eliminarProducto():
#    MostrarProducto()
#    try:
#       borrar=int(input("Cual Producto borrará?: "))
#       if borrar in productosDicc.keys():
#          del productosDicc[borrar]
#       else:
#          print("No existe")
#    except Exception as e:
#       print("Erro", e)
# def actualizarProducto():
#    MostrarProducto()
#    try:
#       num=int(input("Que producto desea actualizar?: "))
#       if num in productosDicc.keys():
#          nombre = input("Cual es el nombre nuevo: ")
#          precio = int(input(""))
#          productosDicc[num]={"nombre": nombre, "precio": precio}
#       else:
#          print("No existe")
#    except Exception as e:
#       print("Error", e)

# def comprar():
#    while True:
#       MostrarProducto()
#       try:  
#          compra = int(input("Ingrese el producto a comprar (0 para salir): "))
#          if compra == 0:
#             break
#          if compra in productosDicc.keys():
#             carrito.append(productosDicc[compra])
#             print(f"Producto agregado al carrito")
#          else:
#             print("Producto no encontrado")
#       except Exception as e:
#          print("Error", e)
      
# def boleta_salir():
#    total = 0
#    print("-" * 30, "0", "-" * 30)
#    for prod in carrito:
#       print(f"{prod["nombre"]}___${prod["precio"]}")
#       total += prod["precio"]
#    print("-" * 30, "0", "-" * 30)
#    print(f"El total neto es: {total} y el IVA es: {total * 0.19}")
#    print("-" * 30, "0", "-" * 30)
#    print(f"El total a pagar es: {total * 1,19}")

# def vegetalesMenuDiccionario():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Comprar")
#          print("6.- Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarProducto()
#                case 2:
#                   eliminarProducto()
#                case 3:
#                   actualizarProducto()
#                case 4:
#                   MostrarProducto()
#                case 5:
#                   comprar()
#                case 6:
#                   boleta_salir()
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)
# vegetalesMenuDiccionario()


# pacientes = [
#    {"nombre": "Aquiles", "prevision": "Fonasa", "temperatura": 34.6, "grave": False}
# ]
# precio = 25000

# def validTemp(t):
#    if t > 39:
#       return True
#    else:
#       return False

# def mostrarPaciente():
#    c = 1
#    for paciente in pacientes:
#       print(f"{c} .- {paciente}")
#       c += 1
#    print("-" * 30)

# def agregarPaciente():
#    nombre = input("Cual es el nombre del paciente: ")
#    while nombre == "" or len(nombre) < 9:
#       print("El nombre no debe estar vacio y debe tener mas de 8 letras")
#       nombre = input("Cual es el nombre del paciente: ")

#    prevision = input("Cual es la prevision del paciente: ")
#    while prevision.lower() not in ("fonasa", "isapre", "fodesa"):
#       print("Prevision invalida")
#       prevision = input("Cual es la prevision del paciente: ")

#    temperatura = float(input("Cual es la temperatura del paciente: "))

#    pacientes.append({"nombre": nombre, "prevision": prevision, "temperatura": temperatura, "grave": validTemp(temperatura)})

# def eliminarPaciente():
#    mostrarPaciente()
#    eliminado = int(input("Ingrese el paciente a eliminar: "))
#    pacientes.pop(eliminado - 1)
#    print("Paciente eliminado")

# def cobrarPaciente():
#    mostrarPaciente()
#    cobrar = int(input("A quien le va a cobrar?: "))
#    if pacientes[cobrar - 1]["prevision"] == "fonasa":
#       total = 25000 * 0.46
#    elif pacientes[cobrar - 1]["prevision"] == "isapre":
#       total = 25000 * 0.73
#    elif pacientes[cobrar - 1]["prevision"] == "fodesa":
#       total = 25000 * 0.875
#    else:
#       print("Prevision invalida")

#    print(f"El total a pagar es: {total}")

# def tomarTemperatura():
#    mostrarPaciente()
#    p = int(input("A que paciente le tomara la temperatura?: "))
#    t = float(input("Ingrese la temperatura nueva: "))
#    pacientes[p - 1]["temperatura"] = t
#    pacientes[p - 1]["grave"] = validTemp(t)

# while True:
#    try:
#       print("1.- Agregar paciente")
#       print("2.- Quitar paciente")
#       print("3.- Tomar temperatura")
#       print("4.- Cobrar paciente")
#       print("5.- Mostrar pacientes")
#       print("6.- Salir")
#       op = int(input("Ingrese su opcion: "))
#       match op:
#          case 1:
#             agregarPaciente()
#          case 2:
#             eliminarPaciente()
#          case 3:
#             tomarTemperatura()
#          case 4:
#             cobrarPaciente()
#          case 5:
#             mostrarPaciente()
#          case 6:
#             print("Saliendo del sistema")
#             break
#    except Exception as e:
#       print(f"Error, {e}")


# frutas = ["Manzana", "Pera", "Uva"]

# for fruta in frutas:
#    print(fruta)
   

# persona = {
#    "nombre": "Diego",
#    "edad": 20
# }

# for key, value in persona.items():
#    print(f"{key} = {value}")


# alumnos = []

# nombre = input("Ingrese el nombre del alumno: ")

# alumnos.append(nombre)


alumnos = [
   {"nombre": "Diego", "nota": 6.0},
   {"nombre": "Daniel", "nota": 6.9},
   {"nombre": "Fernando", "nota": 5.1},
   {"nombre": "Matias", "nota": 4.8},
   {"nombre": "Alexis", "nota": 4.3},
]

def mostrarAlumnos():
   count = 1
   for alumno in alumnos:
      print(f"{count}.- {alumno["nombre"]} = {alumno["nota"]}")
      count += 1
      
def eliminarAlumno():
   mostrarAlumnos()
   eliminado = int(input("Ingrese la opcion a eliminar: "))
   alumnos.pop(eliminado - 1)
   print("Alumno eliminado")

def agregarAlumno():
   nombre = input("Ingrese el nombre del alumno: ")
   nota = float(input("Ingrese la nota del alumno: "))
   alumnos.append({"nombre": nombre, "nota": nota})
   print("Alumno agregado")
   
def actualizarAlumno():
   mostrarAlumnos()
   act = int(input("Ingrese el alumno a actualizar: "))
   nombre = input("Ingrese el nombre del alumno: ")
   nota = float(input("Ingrese la nota del alumno: "))
   
   alumnos[act-1]["nombre"] = nombre
   alumnos[act-1]["nota"] = nota
   
   print("Alumno actualizado")
   print("-" * 30)

actualizarAlumno()

mostrarAlumnos() 