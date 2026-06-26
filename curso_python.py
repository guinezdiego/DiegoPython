print("Hola mundo")

# pan con mayo

# Variables

puntuacion = 100

precio = 4.99

texto = "Wipig"

bools = True / False

score = None
nombre = None

pi = 3.14

# Operadores

suma = 3 + 2
resta = 3 - 2
multi = 3 * 2
division = 4 / 2

a = 3
b = 5
c = a + b

d = 5.2
e = 2.6
f = d / e

x = 12.5
y = 3.5
z = x * y

# El operador % te indica el resto que queda despues de dividir un numero por otro
# Por ejemplo

resultado = 10 % 3

# El 3 cabe en el 10 tres veces, con un resto de 1
# Por lo tanto, resultado sera 1

# Normalmente, el modulo se usa para comprobar
# Si un numero es par o impar

# Si al dividirlo por 2, el resto es 0, el numero es par
# Si el resto da 1, el numero es impar

a = 9
b = 2
c = 11

d = a % 2
e = b % 3
f = c % 10

x = 15
y = 4
z = 23

w = x % y
v = z % x
u = z % y

# Atajos aritmeticos

cont = 0
cont += 4
cont *= 2
cont -= 1

score = 100
score /= 2
score += 10
score *= 3

a = 12
b = 2
c = a * b

# Operadores de comparacion
# Se utilizan para comparar entre dos operandos

1 == 2 = False
1 != 2 = True
1 > 2 = False
1 < 2 = True
1 >= 2 = False
1 <= 2 = True

var1 = 13
var2 = 12
var3 = var1 != var2

n1 = 8
n2 = 9
n3 = n1 > n2

x = 15
y = 10
z = x <= y

# Operadores logicos

# El operador "and" devuelve "True" si ambas declaraciones son verdaderas

x = True
y = True

resultado = x and y

# Si uno de los valores es falso devolvera "False"

edad = 20
tiene_licencia = True
resultado = edad >= 18 and tiene_licencia

x1 = True
x2 = False
x3 = x1 and x2

# El operador "or" devuelve "True" si solo una declaracion es verdadera
# El operador "not" devuelve el valor contrario

b1 = 2
b2 = 3
b3 = (b1 * b2) > (b1 + b2)

a = True
b = False
c = False
resultado = (a or b) and not c

b1 = True
b2 = True
b3 = False
b4 = b1 and b2 and (not b3)

num = 6
es_positivo = num > 0
es_par = num % 2 == 0
resultado = es_positivo and es_par

# Enfoque mas directo
resultado = num > 0 and num % 2 == 0

num = -4
es_negativo_o_impar = num < 0 or num % 2 != 0

edad = int(input("Ingrese su edad: "))
tiene_licencia = input("si/no: ").lower() == "si"
tiene_seguro = input("si/no: ").lower() == "si"
resultado = edad >= 18 and tiene_licencia and tiene_seguro

esta_soleado = input("si/no: ").lower() == "si"
temperatura = float(input("Ingrese la temperatura: "))
velocidad_viento = float(input("Ingrese la velocidad del viento: "))
temperatura_agua = float(input("Ingrese la temperatura del agua: "))

can_hiking = esta_soleado and temperatura > 15 and velocidad_viento < 20
can_swimming = esta_soleado and temperatura > 20 and temperatura_agua > 18
cannot_outside = esta_soleado == False or temperatura < 10 or velocidad_viento > 30

has_license = True
has_space = True
has_experience = False

can_sell_regular_pet = has_license or has_experience and has_space
can_sell_exotic_pet = has_license and has_experience and has_space
cannot_sell_any_pet = (not has_license and not has_experience) or not has_space

print(f"Can sell regular pet: {can_sell_regular_pet}")
print(f"Can sell exotic pet: {can_sell_exotic_pet}")
print(f"Cannot sell any pet: {cannot_sell_any_pet}")


# Toma de decisiones

age = 20
status = "Child"

if age > 18:
    status = "Adult"

print(status)


a = 15
b = 12
c = 0

if a >= b and not b < 10:
    c = 2

c += 1
print(f"c = {c}")


a = 12
b = 11
c = 0

if a < b or b >= 10:
    c = 2

c += 1
print(f"c = {c}")


age = 68
status = "Ninguno"

if age < 18:
    status = "Joven"
elif age >= 18 and age <= 65:
    status = "Adulto"
else:
    status = "Old"
    

wind = float(input("Ingrese la velocidad del viento: "))
status = "Nada"

if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <= 31:
    status = "Breeze"
elif wind >= 32 and wind <= 63:
    status = "Gale"
else:
    status = "Storm"

print(f"Status = {status}")


temperatura = float(input("Ingrese la temperatura: "))
clima = "Ninguno"

if temperatura < 0:
    clima = "Freezing"
elif temperatura >= 0 and temperatura <= 15:
    clima = "Cold"
elif temperatura >= 16 and temperatura <= 25:
    clima = "Mild"
else:
    clima = "Hot"

print(f"Clima = {clima}")


age = 18
title = "None"
allowed_to_drink = False

if age >= 18:
    title = "Adult"
    if age >= 21:
        allowed_to_drink = True
    else:
        allowed_to_drink = False
else:
    title = "Minor"
    

age = int(input("Ingrese su edad: "))
with_parent = True/False
message = "None"

if age >= 18:
    message = "You can watch any movie"
else:
    if age < 18:
        if with_parent == True:
            message = "You can watch PG-13 movies"
        else:
            message = "You can only watch G- rated movies"

print(message)


level = int(input("Ingrese su nivel: "))
has_training = input("Entrenaste?: ")
level_message = "None"

if 1 <= level <= 5:
    level_message = "Basic weapons only"
elif 6 <= level <= 10:
    if has_training == False:
        level_message = "Need weapon training first"
    else:
        level_message = "Access to advanced weapons granted"
elif level >= 11:
    level_message = "Acces to all weapons granted"
else:
    level_message = "Invalid level"
    
print(level_message)


