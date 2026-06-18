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

