animes = {
    1:{"nombre": "One Piece", "año": 1999, "capitulos": 1160},
    2:{"nombre": "Naruto", "año": 1999, "capitulos": 220},
    3:{"nombre": "Bleach", "año": 2004, "capitulos": 366}
}

def agregarAnime():
   print("Cual es el nombre del anime?")
   nombre = input()
   print("cual es el año de estreno?")
   estreno = int(input())
   print("Cuantos capitulos tiene?")
   capitulos = int(input())
   nuevoKey=list(animes.keys())
   nuevoKey.sort()
   animes[nuevoKey[-1]+1]= {"nombre": nombre, "año": estreno, "capitulos": capitulos}

def mostrarAnime():
    for key, value in animes.items():
        print(f"{key} = {value}")

def eliminarAnime():
    mostrarAnime()
    try:
      borrar=int(input("Cual es el anime a borrar: "))
      if borrar in animes.keys():
        del animes[borrar]
      else:
        print("No existe")
    except Exception as e:
      print("Erro", e)

def actualizarAnime():
    mostrarAnime()
    try:
        num=int(input("Que producto desea actualizar?: "))
        if num in animes.keys():
            nombre = input("Cual es el nombre nuevo: ")
            precio = int(input(""))
            animes[num]={"nombre": nombre, "precio": precio}
        else:
            print("No existe")
    except Exception as e:
        print("Error", e)

def ordenarCapitulos():
    ordenados = sorted(animes.items())
    for key, value in ordenados:
        print(f"{value['nombre']} - {value['capitulos']} capitulos")
        
while True:
    print("1.- mostrar animes")
    print("2.- Agregar anime")
    print("3.- Eliminar anime")
    print("4.- Actualizar anime")
    print("5.- Mostrar por cantidad capitulos")
    print("6.- Salir del sistema")
    try:
        op = int(input("Ingrese su opcion: "))
        match op:
            case 1:
                mostrarAnime()
            case 2:
                agregarAnime()
            case 3:
                eliminarAnime()
            case 4:
                actualizarAnime()
            case 5:
                ordenarCapitulos()
            case 6:
                print("Saliendo del sistema")
                break
            case _:
                print("Opcion invalida")
    except ValueError as er:
        print(f"Error. {er}")
