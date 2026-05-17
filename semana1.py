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