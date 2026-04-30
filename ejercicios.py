# debes pedirle al usuario que ingrese 3 numeros y luego se reste y se sume
# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))
# num3 = int(input("Ingrese otro numero: "))
# print(f"El total de la suma es: {num1 + num2 + num3}")
# print(f"El total de la resta es: {num1 - num2 - num3}")

# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres un pendejo culiao")

# 1 a 17 = Eres menor de edad
# 18 a 60 = Eres adulto
# 61 para arriba = Eres Adulto mayor

# edad = int(input("Ingrese su edad: "))
# if edad <= 17 and edad >=1:
#     print("Eres un cabro culiao")
# elif edad >= 18 and edad <= 60:
#     print("Eres un adulto")
# elif edad >= 61 and edad <= 100:
#     print("Eres un adulto mayor")
# else:
#     print("Edad invalida")

# nombre = input("Ingrese su nombre: ")
# c_letras = 0
# for letra in nombre:
#     print(letra)
#     c_letras += 1
# print(f"El total de letras es: {c_letras}")

# pedir el nombre del usuario
# contar la cantidad de vocales
# contar la cantidad de consonantes

# nombre = input("Ingrese su nombre: ")
# c_vocales = 0
# c_conso = 0
# for letra in nombre:
#     if letra in "AEIOUaeiou":
#         c_vocales += 1
#     else:
#         c_conso += 1
# print(f"El total de vocales es: {c_vocales}")
# print(f"El total de consonantes es: {c_conso}")

# num = int(input("Ingrese un numero: "))
# for i in range(10):
#     print(f"{num} X {i+1} = {num * (i+1)}")

# def promedio():

#     notas = int(input("Ingrese el numero de notas: "))
#     promedio = 0
#     for nota in range(notas):
#         nota = float(input("Ingrese la nota: "))
#         promedio += nota
#     print(f"El promedio final es: {round(promedio / notas, 2)}")
    
# promedio()


# color = input("Ingrese un color: ")

# if color.lower() == "rojo":
#     print("Color de peligro")
# elif color.lower() == "verde":
#     print("Puedes avanzar")
# elif color.lower() == "amarillo":
#     print("Precaucion")
# else:
#     print("Color desconocido") 


# for i in range(1,21):
#     if i % 2 == 0:
#         print(f"{i} es par")
#     else:
#         print(f"{i} es impar")


# num = 1
# n_ingresados = 0
# suma = 0
# while num != 0:
#     num = int(input("Ingrese un numero: "))
#     if num != 0:
#         suma += num
#         n_ingresados += 1
# print(f"El total de la suma es: {suma}")
# print(f"El total de numeros ingresados es: {n_ingresados}")

# def es_mayor_edad():
#     edad = int(input("Ingrese su edad: "))
#     if edad >= 18:
#         print("Mayor de edad")
#     else:
#         print("Menor de edad")
# es_mayor_edad()