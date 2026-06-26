personas = [
    {"nombre": "Diego", "promedio": 6.7, "edad": 20},
    {"nombre": "Ian", "promedio": 6.9, "edad": 18},
    {"nombre": "Daniel", "promedio": 3.3, "edad": 31}
]

def mostrarDatos():
    c = 1
    for p in personas:
        print(f"{c}.- Nombre: {p["nombre"]}, Promedio: {p["promedio"]}, Edad: {p["edad"]}")
        c += 1
    print("-" * 30)

def eliminarPersona():
    mostrarDatos()
    elim = int(input("A quien desea eliminar: "))
    personas.pop(elim - 1)
    print("Persona eliminada")
    print("-" * 30)

def agregarPersona():
    nom = input("Ingrese el nombre nuevo: ")
    prom = float(input("Ingrese el promedio: "))
    edad = int(input("Ingrese la edad: "))
    
    personas.append({"nombre": nom, "promedio": prom, "edad": edad})
    print("Persona agregada")
    print("-" * 30)

def actualizarPersona():
    mostrarDatos()
    act = int(input("Ingrese la persona a actualizar: "))
    nom = input("Ingrese el nombre nuevo: ")
    prom = float(input("Ingrese el promedio: "))
    edad = int(input("Ingrese la edad: "))
    
    personas[act - 1]["nombre"] = nom
    personas[act - 1]["promedio"] = prom
    personas[act - 1]["edad"] = edad
    print("Persona actualizada")
    print("-" * 30)

def menuPersonas():
    while True:
        print("1.- Mostrar personas")
        print("2.- Agregar persona")
        print("3.- Eliminar persona")
        print("4.- Actualizar persona")
        print("5.- Salir")
        try:
            op = int(input("Ingrese su opcion: "))
            match op:
                case 1:
                    mostrarDatos()
                case 2:
                    agregarPersona()
                case 3:
                    eliminarPersona()
                case 4:
                    actualizarPersona()
                case 5:
                    print("Saliendo del sistema")
                    break
                case _:
                    print("Opcion invalida")
        except ValueError as er:
            print("Error", er)

