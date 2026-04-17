n_vocales = 0
n_conso = 0
nombre = input("Ingrese su nombre: ")
for i in nombre:
    if i in "aeiouAEIOU":
        n_vocales += 1
    else:
        n_conso += 1
print(f"El numero de vocales es: {n_vocales}")
print(f"El numero de consonantes es: {n_conso}")