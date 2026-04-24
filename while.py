# count = 0
# while count < 3:
#     print(f"Contador {count}")
#     count += 1
# pin = 3535
# code = int(input("Ingrese su pin: "))
# while pin!=code:
#     print("Error, intente de nuevo")
#     code = int(input("Ingrese su pin: "))
# print("Bienvenido")

# num = int(input("Ingrese un numero: "))
# cont = 1
# while cont <= 10:
#     print(f"{num} x {cont} = {num * cont}")
#     cont += 1

toon1 = input("Ingrese el toon 1: ")
toon2 = input("Ingrese el toon 2: ")

v1 = 0
v2 = 0

votantes = int(input("Cuantos votantes son?"))

while votantes > 0:
    voto = int(input(f"Por quien votaras? 1.- {toon1} 2.- {toon2} "))
    if voto == 1:
        v1 += 1
    elif voto == 2:
        v2 += 1
    else:
        print("Voto nulo")