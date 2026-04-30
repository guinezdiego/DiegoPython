# enteros = 200
# texto = "Hola"
# flotante = 4.6
# booleanos = True/False

# Pide al usuario un numero
# Si el numero es par,

# color = input("Ingrese un color: ")

# if color == "rojo":
#     print("Ve con cuidado")
# elif color == "amarillo":
#     print("Apresurate")
# elif color == "verde":
#     print("Puedes pasar")
# else:
#     print("Color desconocido")

# LE van a pedir un numero al usuario
# Si van a el numero es negativo, positivo o es cero

# num = int(input("Ingrese su numero: "))
# if num > 0:
#     print("Es positivo")
# elif num < 0:
#     print("Es negativo")
# else:
#     print("Es cero")

#Le piden un numero al usuario y verifican si es mayor de edad o menor de edad

# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Eres mayor de edad")
# elif edad < 18 and edad > 0:
#     print("Eres menor de edad")
# else:
#     print("Edad invalida")

# Pide al usuario un numero y muestra la tabla de multiplicar

# Le van a pedir una palabra al usuario y tienen que mostrar cuantas letras tiene la palabra
# palabra = input("Ingrese una palabra: ")
# n_letras = 0
# for letra in palabra:
#     print(letra)
#     n_letras += 1
# print(f"El total de letras es: {n_letras}")

# i = 1
# suma = 0

# while i <= 5:
#     suma += i
#     i += 1
# print(suma)

# palabra = input("Ingrese una palabra: ")
# print(palabra.capitalize())

# password = "CANGRI"

# clave = input("Ingrese la clave: ").upper()

# while clave != password:
#     print("Contraseña incorrecta")
#     clave = input("Ingrese la clave: ").upper()
    
# print("Bienvenido")

# pide al usuario el nombre
# pide al usuario el apellido
# Muestra el nombre completo
# Ej: "Diego Guiñez"

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombre = nombre.capitalize()
apellido = apellido.capitalize()

print(nombre, apellido)