
deuda = 100000
op = 0

while op != 3:
    print("1.- Pagar deudas")
    print("2.- Comprar")
    print("3.- Salir")
    while True:
        try:
            op = int(input("Ingrese su opcion: "))
            break
        except ValueError as er:
            print("Solo numeros enteros y positivos")

    match op:
        case 1:
            print(f"El monto total de la deuda es de {deuda}")
            while True:
                try:
                    monto = int(input("Ingrese el monto a pagar: "))
                    break
                except:
                    print("Solo numeros enteros y positivos")
                
            if monto >= 0 and monto <= deuda:
                deuda -= monto
                print(f"El total actual de la deuda es: {deuda}")
            else:
                print("El monto debe ser mayor a 0 y menor o igual a la deuda a pagar")

        case 2:
            while True:
                try:
                    compras = int(input("Ingrese la cantidad de compras: "))
                    break
                except:
                    print("Solo numeros enteros y positivos")
            for i in range(compras):
                while True:
                    try:
                        monto = int(input("Ingrese el monto de la compra: "))
                        break
                    except:
                        print("Solo numeros enteros y positivos")
                if monto >= 0:
                    deuda += monto
                else:
                    print("El pago debe ser mayor a 0")
        
        case 3:
            print("Saliendo del sistema")
