while True:
    a = int(input("Ingrese 1 para verificar un número o 0 para salir: "))

    if a == 1:
        numero = int(input("Ingrese un número: "))

        if numero % 2 == 0:
            print("El número es PAR")
        else:
            print("El número es IMPAR")

    elif a == 0:
        print("Saliendo del programa...")
        break  # ← esto te saca del while

    else:
        print("Opción inválida, intente de nuevo")