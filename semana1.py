# # Ejercicio 1

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))
# carrera = input("Ingrese su carrera: ")

# print(f"Hola {nombre}")
# print(f"Tienes {edad} años")
# print(f"Estudias {carrera}")

# # Ejercicio 2

# n1 = int(input("Ingrese un numero: "))
# n2 = int(input("Ingrese otro numero: "))

# while n2 == 0:
#     print("No se puede dividir por 0")
#     n2 = int(input("Ingrese otro numero: "))

# print(f"La suma de los numeros es: {n1 + n2}")
# print(f"La resta de los numeros es: {n1 - n2}")
# print(f"EL total del la multiplicacion es: {n1 * n2}")
# print(f"El total de la division es: {n1 / n2}")

# # Ejercicio 3

# notas = int(input("Ingrese el numero de notas: "))
# suma_total = 0

# for nota in range(notas):
#     nota = float(input("Ingrese su nota: "))
#     suma_total += nota

# promedio = suma_total / notas

# print(f"El promedio final es de: {promedio}")

# # Ejercicio 4

# celsius = int(input("Ingrese los grados C°: "))
# fahren = celsius * (9 / 5) + 32

# print(f"Grados Fahrenheit: {fahren}")

# # Ejercicio 5

# num = int(input("Ingrese un numero: "))

# if num % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

# # Mini desafio

# nombre = input("Ingrese su nombre: ")
# notas = int(input("Ingrese el numero de notas: "))
# suma_notas = 0

# for i in range(notas):
#     nota = float(input("Ingrese su nota: "))
#     suma_notas += nota

# promedio = suma_notas / notas

# if promedio >= 4:
#     print(f"{nombre} tu promedio final es: {promedio} estas aprobado")
# else:
#     print(f"{nombre} tu promedio final es: {promedio} estas reprobado")

# # Mini prueba
# # Pregunta 1
# base = int(input("Ingrese la base: "))
# altura = int(input("Ingrese la altura: "))
# area = base * altura
# print(f"El area total es de: {area}")

# # Pregunta 2

# num = int(input("Ingrese un numero: "))
# print(f"El doble de {num} es: {num * 2} y el triple de {num} es: {num * 3}")

# # Pregunta 3

# segundos = int(input("Ingrese los segundos: "))
# minutos = segundos // 60

# print(f"El total de minutos es: {minutos}")

# # Reto final del dia

# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))

# while num2 == 0:
#     print("No se puede dividir por 0")
#     num2 = int(input("Ingrese otro numero: "))
    
# print(f"El total de la suma es: {num1 + num2}")
# print(f"El total de la resta es: {num1 - num2}")
# print(f"El total de la multiplicacion es: {num1 * num2}")
# print(f"El total de la division es: {num1 / num2}")
# print(f"El total de la potencia es: {num1 ** num2}")

# Dia 2

# Ejercicio 1

# num = int(input("Ingrese un numero: "))

# if num < 0:
#     print("Es negativo")
# elif num > 0:
#     print("Es positivo")
# else:
#     print("Es cero")

# Ejercicio 2

# nota = float(input("Ingrese su nota: "))

# if nota >= 6 and nota <= 7:
#     print("Excelente")
# elif nota >= 5 and nota < 6:
#     print("Bueno")
# elif nota >= 4 and nota < 5:
#     print("Relugar")
# elif nota >= 1 and nota < 4:
#     print("Reprobado")
# else:
#     print("Nota invalida")

# Ejercicio 3

# password = "Hoplita3119"

# clave = input("Ingrese la contraseña: ")

# while password != clave:
#     print("Contraseña incorrecta, intente denuevo")
#     clave = input("Ingrese la contraseña: ")

# print("Bienvenido")

# Ejercicio 4

# cont = 1

# while cont <= 20:
#     print(cont)
#     cont += 1

# Ejercicio 5

# suma_total = 0
# num = 1

# while num != 0:
#     num = int(input("Ingrese un numero: "))
#     suma_total += num
# print(f"La suma total de los numeros es: {suma_total}")

# mini desafio

# op = 0

# while op != 5:
#     print("1.- Sumar")
#     print("2.- Restar")
#     print("3.- Multiplicar")
#     print("4.- Dividir")
#     print("5.- Salir")
#     op = int(input("Ingrese su opcion: "))
#     if op == 1:
#         n1 = int(input("Ingrese un numero: "))
#         n2 = int(input("Ingrese otro numero: "))
#         suma = n1 + n2
#         print(f"El total de la suma es {suma}")
#     elif op == 2:
#         n1 = int(input("Ingrese un numero: "))
#         n2 = int(input("Ingrese otro numero: "))
#         resta = n1 - n2
#         print(f"El total de la resta es: {resta}")
#     elif op == 3:
#         n1 = int(input("Ingrese un numero: "))
#         n2 = int(input("Ingrese otro numero: "))
#         multi = n1 * n2
#         print(f"El total de la multiplicacion es: {multi}")
#     elif op == 4:
#         n1 = int(input("Ingrese un numero: "))
#         n2 = int(input("Ingrese otro numero: "))
#         while n2 == 0:
#             print("No se puede dividir por 0")
#             n2 = int(input("Ingrese otro numero: "))
#         division = n1 / n2
#         print(f"El total de la disivion es: {division}")
#     elif op == 5:
#         print("Saliendo del sistema")
#     else:
#         print("Opcion invalida")

# Mini prueba
# Pregunta 1

# cont = 1
# num = int(input("Ingrese un numero: "))

# while cont <= 10:
#     print(f"{num} x {cont} = {num * cont}")
#     cont += 1

# Pregunta 2

# clave = "admin123"
# password = input("Ingrese la contraseña: ")

# while password != clave:
#     print("Contraseña incorrecta")
#     password = input("Ingrese la contraseña: ")

# print("Bienvenido")

# Reto final del dia

# saldo = 100000
# op = 0

# while op != 4:
#     print("1.- Ver Saldo")
#     print("2.- Depositar")
#     print("3.- Retirar")
#     print("4.- Salir")
#     op = int(input("Ingrese su opcion: "))
#     if op == 1:
#         print(f"Su saldo total es: {saldo}")
#     elif op == 2:
#         deposito = int(input("Ingrese monto a depositar: "))
#         saldo += deposito
#         print(f"Su saldo actual es de: {saldo}")
#     elif op == 3:
#         retiro = int(input("Ingrese monto a retirar: "))
#         saldo -= retiro
#         print(f"Su saldo actual es de: {saldo}")
#     elif op == 4:
#         print("Saliendo del sistema")
#     else:
#         print("Opcion invalida")

# Dia 3
# Ejercicio 1

# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# Ejercicio 2

# suma_total = 0

# for i in range(5):
#     num = int(input("Ingrese un numero: "))
#     suma_total += num
#     promedio = suma_total / 5
# print(f"El promedio total es: {promedio}")

# Ejercicio 3

# mayor = int(input("Ingrese un numero: "))

# for i in range(9):
#     num = int(input("Ingrese un numero: "))
#     if num > mayor:
#         mayor = num
# print(f"El numero mayor es {mayor}")

# Ejercicio 4

# num = int(input("Ingrese un numero: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# Ejercicio 5

# simbolo = "*"

# for i in range(1, 6):
#     print(simbolo * i)

# Mini desafio

# m_alumno = " "
# p_alumno = " "
# total = 0
# m_nota = 0
# p_nota = 7
# c_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# for i in range(c_alumnos):
#     nombre = input("Ingrese su nombre: ")
#     promedio = float(input("Ingrese su promedio: "))
#     total += promedio
#     if promedio > m_nota:
#         m_nota = promedio
#         m_alumno = nombre
#     if promedio < p_nota:
#         p_nota = promedio
#         p_alumno = nombre
    
# promedio_g = total / c_alumnos
# print(f"El promedio general es: {promedio_g}")
# print(f"El mejor alumno fue {m_alumno} con un promedio de: {m_nota}")
# print(f"El peor alumno fue: {p_alumno} con un promedio de: {p_nota}")

# Mini prueba
# Pregunta 1

# n_pares = 0
# n_impares = 0

# for i in range(1, 8):
#     num = int(input("Ingrese un numero: "))
#     if num % 2 == 0:
#         n_pares += 1
#     else:
#         n_impares += 1

# print(f"El total de numeros pares fue: {n_pares}")
# print(f"El total de numeros impares fue: {n_impares}")

# Pregunta 2

# suma_total = 0
# num = 0
# n_ingresados = -1

# while num != -1:
#     num = int(input("Ingrese un numero: "))
#     suma_total += num
#     n_ingresados += 1
    
# promedio = suma_total / n_ingresados
# print(f"La suma total es: {suma_total}")
# print(f"EL promedio de los numeros es: {promedio}")

# Pregunta 3

# simbolo = "*"

# for i in range(5, 0, -1):
#     print(simbolo * i)

# Reto final del dia

# c_alumnos = int(input("Ingrese la cantidad de alumnos: "))
# m_promedio = 0
# p_promedio = 7
# m_alumno = " "
# p_alumno = " "
# suma_total = 0

# for i in range(c_alumnos):
#     suma = 0
#     nombre = input("Ingrese su nombre: ")
#     for i in range(3):
#         nota = float(input("Ingrese su nota: "))
#         suma += nota
#         promedio = suma / 3
#         suma_total += promedio
#     if promedio > m_promedio:
#         m_promedio = promedio
#         m_alumno = nombre
#     if promedio < p_promedio:
#         p_promedio = promedio
#         p_alumno = nombre
#     if promedio >= 4:
#         print(f"Tu promedio es: {promedio}, aprobado")
#     else:
#         print(f"Tu promedio es: {promedio}, reprobado")

# promedio_g = suma_total / c_alumnos
# print(f"El promedio general del curso es: {promedio_g}")
# print(f"EL mejor promedio fue: {m_promedio}, del alumno {m_alumno}")
# print(f"El peor promedio fue: {p_promedio}, del alumno {p_alumno}")

# Dia 4
# Ejercicio 1

# nombres = []
# c_nombres = int(input("Ingrese la cantidad de nombres: "))

# for i in range(c_nombres):
#     nombre = input("Ingrese el nombre: ")
#     nombres.append(nombre)

# print(nombres)

# Ejercicio 2

# lista = []
# suma_total = 0
# c_numeros = int(input("Ingrese la cantidad de numeros: "))

# for i in range(c_numeros):
#     numero = int(input("Ingrese el numero: "))
#     suma_total += numero

# promedio = suma_total / c_numeros

# print(f"La suma total es: {suma_total}")
# print(f"EL promedio es: {promedio}")

# Ejercicio 3

# mayor = 0
# menor = 999

# c_numeros = int(input("Ingrese la cantidad de numeros: "))

# for i in range(c_numeros):
#     numero = int(input("Ingrese el numero: "))
#     if numero > mayor:
#         mayor = numero
#     if numero < menor:
#         menor = numero

# print(f"El numero mayor fue: {mayor}")
# print(f"El numero menor es: {menor}")

# Ejercicio 4

# nombres = ["Ana", "Luis", "Pedro", "Maria"]
# persona = input("Ingrese el nombre: ").capitalize()

# if persona in nombres:
#     print("Si existe")
# else:
#     print("No existe")

# Ejercicio 5

# pares = 0
# impares = 0
# numeros = []

# c_numeros = int(input("Ingrese la cantidad de numeros: "))

# for i in range(c_numeros):
#     numero = int(input("Ingrese el numero: "))
#     numeros.append(numero)

# for j in numeros:
#     if j % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
        
# print(f"El total de pares es: {pares}")
# print(f"El total de impares es: {impares}")

# Mini desafio

# nombres = []
# promedios = []
# suma_promedios = 0
# m_alumno = " "
# p_alumno = " "
# p_promedio = 999
# m_promedio = 0
# c_alumnos = int(input("Ingrese la cantidad de estudiantes: "))

# for i in range(c_alumnos):
#     nombre = input("Ingrese su nombre: ")
#     nombres.append(nombre)
#     promedio = float(input("Ingrese su promedio: "))
#     promedios.append(promedio)
#     suma_promedios += promedio
    
#     if promedio > m_promedio:
#         m_promedio = promedio
#         m_alumno = nombre
    
#     if promedio < p_promedio:
#         p_promedio = promedio
#         p_alumno = nombre

# promedio_g = suma_promedios / c_alumnos

# print(f"El promedio general fue: {round(promedio_g, 1)}")
# print(f"El mejor alumno fue: {m_alumno} con un promedio de: {m_promedio}")
# print(f"El peor alumno fue: {p_alumno} con un promedio de: {p_promedio}")
    
# Mini prueba
# Pregunta 1

# mayor = 0
# menor = 999
# suma_total = 0

# numeros = [12, 23, 34, 45, 56, 67, 78, 89]

# for i in numeros:
#     suma_total += i
    
#     if i > mayor:
#         mayor = i
    
#     if i < menor:
#         menor = i

# promedio = suma_total / len(numeros)

# print(f"El promedio general es: {promedio}")
# print(f"El numero maoyr es: {mayor}")
# print(f"El numero menor es: {menor}")

# Pregunta 2

# nombres = []
# nombre = " "

# while nombre != "salir":
#     nombre = input("Ingrese un nombre: ")
    
#     if nombre != "salir":
#         nombres.append(nombre)

# print(nombres)

# Pregunta 3

# productos = ["pan", "leche", "arroz", "cereal", "fideos"]
# pregunta = input("Ingrese el producto a buscar: ")

# if pregunta in productos:
#     print("Si quedan")
# else:
#     print("No quedan")

# Reto final del dia

# nombres = []
# promedios = []
# m_alumno = " "
# p_alumno = " "
# suma_total = 0
# m_promedio = 0
# p_promedio = 999
# aprobados = 0
# reprobados = 0
# c_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# for i in range(c_alumnos):
#     nombre = input("Ingrese su nombre: ")
#     nombres.append(nombre)
#     suma_notas = 0
    
#     for j in range(3):
#         nota = float(input("Ingrese su nota: "))
#         suma_notas += nota
        
#     promedio = suma_notas / 3
#     promedios.append(promedio)
#     suma_total += promedio
    
#     if promedio > m_promedio:
#         m_promedio = promedio
#         m_alumno = nombre
    
#     if promedio < p_promedio:
#         p_promedio = promedio
#         p_alumno = nombre
    
#     if promedio >= 4:
#         aprobados += 1
#     else:
#         reprobados += 1

# promedio_g = suma_total / c_alumnos

# print(f"El numero de aprobados fue: {aprobados}")
# print(f"El numero de reprobados fue: {reprobados}")
# print(f"El mejor alumno fue: {m_alumno} con un promedio de: {round(m_promedio, 1)}")
# print(f"El peor alumno fue: {p_alumno} con un promedio de: {round(p_promedio, 1)}")
# print(f"El promedio general es: {round(promedio_g, 1)}")

# Dia 5

# def cuadrado(num):
#     return num * num

# resultado = cuadrado(4)

# print(resultado)

# Ejercicio 1

# def saludar(nombre):
#     print(f"Hola {nombre}")

# saludar("Diego")

# Ejercicio 2

# def sumar(a, b):
#     return a + b

# suma = sumar(5, 15)

# print(f"La suma total es {suma}")

# Ejercicio 3

# def mayor(a, b):
#     if a > b:
#         return a
#     else:
#         return b
    
# el_mayor = mayor(5, 7)

# print(f"El numero mayor es: {el_mayor}")

# Ejercicio 4

# def tabla(numero):
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")

# tabla(5)

# Ejercicio 5

# def promedios(lista):
#     suma = 0
    
#     for i in lista:
#         suma += i
    
#     return suma / len(lista)

# notas = [6, 7, 6, 7]
# promedio = promedios(notas)

# print(f"El promedio total es {round(promedio, 1)}")

# Mini desafio

# def sumar():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))
#     suma = n1 + n2
#     print(f"El total de la suma es: {suma}")

# def restar():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))
#     resta = n1 - n2
#     print(f"El total de la resta es: {resta}")

# def multiplicar():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))
#     multi = n1 * n2
#     print(f"El total de la multiplicacion es: {multi}")

# def dividir():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))
    
#     while n2 == 0:
#         print("No se puede dividir por 0")
#         n2 = int(input("Ingrese otro numero: "))
    
#     division = n1 / n2
#     print(f"El total de la division es: {round(division, 1)}")
    
# def calculadora():
#     op = 0
    
#     while op != 5:
#         print("1.- Sumar")
#         print("2.- Restar")
#         print("3.- Multiplicar")
#         print("4.- Dividir")
#         print("5.- Salir")
#         op = int(input("Ingrese su opcion: "))
        
#         match op:
#             case 1:
#                 sumar()
#             case 2:
#                 restar()
#             case 3:
#                 multiplicar()
#             case 4:
#                 dividir()
#             case 5:
#                 print("Saliendo del sistema")
#             case _:
#                 print("Opcion invalida")

# calculadora()

# Mini prueba
# Pregunta 1

# def par_o_impar():
#     num = int(input("Ingrese un numero: "))
    
#     if num % 2 == 0:
#         print("Par")
#     else:
#         print("Impar")

# par_o_impar()

# Pregunta 2

# def mayor_lista(lista):
#     mayor = 0
#     menor = 999
    
#     for i in lista:
#         if i > mayor:
#             mayor = i
        
#         if i < menor:
#             menor = i
    
#     print(f"El numero mayor es {mayor}")
#     print(f"El numero menor es: {menor}")

# numeros = [10, 12, 18, 30, 24]

# mayor_lista(numeros)

# Pregunta 3

# def contar_vocales():
#     n_vocales = 0
#     n_conso = 0
#     palabra = input("Ingrese una palabra: ")
    
#     for i in palabra:
#         if i in "AEIOUaeiou":
#             n_vocales += 1
#         else:
#             n_conso += 1
    
#     print(f"La cantidad de vocales son: {n_vocales}")
#     print(f"El total de consonantes es: {n_conso}")

# contar_vocales()

# Reto final del dia

# def pedir_notas():
#     cantidad = int(input("Ingrese la cantidad de notas: "))
#     return cantidad
    
# def calcular_promedio(cantidad):
#     suma = 0
    
#     for i in range(cantidad):
#         nota = float(input("Ingrese su nota: "))
#         suma += nota
    
#     promedio = suma / cantidad
    
#     return promedio

# def estado(promedio):
#     if promedio >= 4:
#         return "Aprobado"
#     else:
#         return "Reprobado"

# def mejor_alumno(nombres, promedios):
#     mejor = promedios[0]
#     alumno = nombres[0]
    
#     for i in range(len(promedios)):
#         if promedios[i] > mejor:
#             mejor = promedios[0]
#             alumno = nombres[0]
        
#     return alumno, mejor
    
# def peor_alumno(nombres, promedios):
#     peor = promedios[0]
#     alumno = nombres[0]
    
#     for i in range(len(promedios)):
#         if promedios[i] < peor:
#             peor = promedios[i]
#             alumno = nombres[i]
            
#     return alumno, peor

# def promedio_general(promedios):
#     suma = 0
    
#     for promedio in promedios:
#         suma += promedio
    
#     return suma / len(promedios)

# nombres = []
# promedios = []

# cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# for i in range(cantidad_alumnos):
#     nombre = input("Ingrese el nombre del alumno: ")
#     nombres.append(nombre)
#     cantidad_notas = pedir_notas()
#     promedio = calcular_promedio(cantidad_notas)
#     promedios.append(promedio)
    
#     print(f"{nombre} tiene promedio {round(promedio, 1)}")
#     print(estado(promedio))
#     print("-" * 30)
    
# mejor_nombre, mejor_prom = mejor_alumno(nombres, promedios)
# peor_nombre, peor_prom = peor_alumno(nombres, promedios)
# promedio_curso = promedio_general(promedios)

# print("===== RESULTADOS FINALES =====")
# print(f"Mejor alumno: {mejor_nombre} con promedio {round(mejor_prom, 1)}")
# print(f"Peor alumno: {peor_nombre} con promedio {round(peor_prom, 1)}")
# print(f"Promedio general del curso: {round(promedio_curso, 1)}")

# Dia 6
# Ejercicio 1

# alumno = {
#     "nombre": "Diego",
#     "edad": 20,
#     "carrera": "Informatica"
# }
# alumno["promedio"] = 6.9

# print(alumno.get("nombre"))
# print(alumno.get("edad"))
# print(alumno.get("carrera"))
# print(alumno.get("promedio"))

# Ejercicio 2

# producto = {
#     "nombre": "Ketchup",
#     "precio": 1500,
#     "stock": 50
# }

# producto["stock"] = 60

# print(producto.get("stock"))

# Ejercicio 3

# juego = {
#     "nombre": "Batman Lego",
#     "fecha": 2008,
#     "stock": 2,
#     "consola": "ps2"
# }

# for clave, valor in juego.items():
#     print(clave, valor)

# Ejercicio 4

# agenda = {
#     "Ana": "1234",
#     "Luis": "5678",
#     "Juan": "9182"
# }

# nombre = input("Ingrese el nombre: ").capitalize()

# if nombre in agenda:
#     print(agenda[nombre])

# Ejercicio 5

# lst_alumnos = [
#     {"nombre": "Diego", "promedio": 6.7},
#     {"nombre": "Daniel", "promedio": 6.9},
#     {"nombre": "Alexis", "promedio": 6.5},
#     {"nombre": "Fernando", "promedio": 6},
#     {"nombre": "Matias", "promedio": 5.5}
# ]

# for i in lst_alumnos:
#     print(i)
    
# Mini desafio

# productos = [
#     {"nombre": "Ketchup", "precio": 1500, "stock": 50},
#     {"nombre": "Mayonesa", "precio": 1600, "stock": 35},
#     {"nombre": "Mostaza", "precio": 1300, "stock": 80}
# ]

# m_caro = 0
# m_barato = 999999

# nombre_caro = " "
# nombre_barato = " "

# suma_precios = 0

# for producto in productos:
    
#     precio = producto["precio"]
    
#     suma_precios += precio
    
#     if precio > m_caro:
#         m_caro = precio
#         nombre_caro = producto["nombre"]
    
#     if precio < m_barato:
#         m_barato = precio
#         nombre_barato = producto["nombre"]

# promedio = suma_precios / len(productos)

# print(f"Producto mas caro: {nombre_caro} - ${m_caro}")
# print(f"Producto mas barato: {nombre_barato} - ${m_barato}")
# print(f"Promedio precios: ${round(promedio, 1)}")

# Mini prueba
# Pregunta 1

# auto = {
#     "marca": "Kuruma",
#     "modelo": "Blindado",
#     "año": 2005
# }

# for clave, value in auto.items():
#     print(clave, value)
    
# Pregunta 2

# agenda = [
#     {"nombre": "Luis", "numero": 1234},
#     {"nombre": "Ana", "numero": 5678},
#     {"nombre": "Deadpool", "numero": 9021}
# ]

# nombre = input("Ingrese el nombre de la persona: ").capitalize()

# for persona in agenda:
#     if nombre in persona["nombre"]:
#         print(persona.get("numero"))

# Pregunta 3

# alumnos = [
#     {"nombre": "Diego", "promedio": 6.8, "carrera": "Analista"},
#     {"nombre": "Daniel", "promedio": 6.6, "carrera": "Analista"},
#     {"nombre": "Alexis", "promedio": 2.1, "carrera": "Analista"},
#     {"nombre": }
# ]

# for alumno in alumnos:
#     if alumno["promedio"] >= 4:
#         print(f"El alumno {alumno["nombre"]} esta aprobado")
#     else:
#         print(f"El alumno {alumno["nombre"]} esta reprobado")

# Reto final del dia

# import time

# alumnos = [
#     {"nombre": "Diego", "promedio": 6.9},
#     {"nombre": "Daniel", "promedio": 6.7},
#     {"nombre": "Alexis", "promedio": 2.1},
#     {"nombre": "Matias", "promedio": 5.8},
#     {"nombre": "Fernando", "promedio": 3.8}
# ]

# m_alumno = " "
# p_alumno = " "

# m_promedio = 0
# p_promedio = 999

# suma_promedios = 0

# for alumno in alumnos:
#     if alumno["promedio"] > m_promedio:
#         m_promedio = alumno["promedio"]
#         m_alumno = alumno["nombre"]
    
#     if alumno["promedio"] < p_promedio:
#         p_promedio = alumno["promedio"]
#         p_alumno = alumno["nombre"]
    
#     if alumno["promedio"] > 4:
#         print(f"El alumno {alumno['nombre']} esta aprobado con un promedio de {alumno['promedio']}")
#     else:
#         print(f"El alumno {alumno['nombre']} esta reprobado con un promedio de {alumno['promedio']}")
    
#     time.sleep(2)
    
#     suma_promedios += alumno["promedio"]

# promedio_general = suma_promedios / len(alumnos)

# print(f"El mejor alumno fue {m_alumno}, con un promedio de {m_promedio}")
# time.sleep(2)

# print(f"El peor alumno fue {p_alumno}, con un promedio de {p_promedio}")
# time.sleep(2)

# print(f"El promedio general fue {round(promedio_general, 1)}")

# Dia 7