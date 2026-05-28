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