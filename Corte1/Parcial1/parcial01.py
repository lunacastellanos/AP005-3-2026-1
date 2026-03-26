
# REQUERIMIENTO 7: TUPLA — información fija del sistema

INFO_SISTEMA = ("¡Hola! Bienvenido al Sistema de Inventario Luna Paola Castellanos Santisteban 20231005146", "Programación Aplicada", "2025")

# REQUERIMIENTO 7: TUPLA — categorías fijas (no se pueden modificar)
CATEGORIAS = ("Electrónica", "Ropa", "Alimentos", "Hogar", "Deportes", "Otros")

# REQUERIMIENTO 6: LISTA 

productos = []

# REQUERIMIENTO 1: MENSAJE DE BIENVENIDA

def mostrar_bienvenida():
    print("=" * 55)
    print(f"   {INFO_SISTEMA[0]}")        
    print(f"   Curso: {INFO_SISTEMA[1]}  |  Año: {INFO_SISTEMA[2]}")
    print("=" * 55)
    print("  Categorías disponibles:")
    for i, cat in enumerate(CATEGORIAS, 1):  # REQUERIMIENTO 9: CICLO FOR, recorre la tupla categorias
        print(f"    {i}. {cat}")
    print("=" * 55)


# REQUERIMIENTO 2: MENÚ PRINCIPAL (la función que se llama dentro del while)

def mostrar_menu():
    print("\n" + "-" * 40)
    print("         MENÚ PRINCIPAL")
    print("-" * 40)
    print("  1. Agregar producto")
    print("  2. Mostrar todos los productos")
    print("  3. Buscar producto")
    print("  4. Eliminar producto")
    print("  5. Salir")
    print("-" * 40)


# REQUERIMIENTO 10: VALIDACIÓN DE DATOS — verifica que sea entero positivo

def validar_entero(mensaje):
    while True:
        valor = input(mensaje).strip()          # REQUERIMIENTO 3: input()
        if valor.isdigit() and int(valor) > 0:  # REQUERIMIENTO 4: int() 
            return int(valor)
        print("  Ingrese un número entero positivo válido.")


def validar_flotante(mensaje):
    while True:
        valor = input(mensaje).strip()    # REQUERIMIENTO 3: input()
        try:
            numero = float(valor)         # REQUERIMIENTO 4: float() 
            if numero > 0:
                return numero
            print(" El valor debe ser mayor a 0.")
        except ValueError:
            print(" Ingrese un número válido (ej: 12.99).")



# REQUERIMIENTO 10: VALIDACIÓN DE DATOS, verifica rango 1-6

def seleccionar_categoria():
    print("\n  Categorías:")
    for i, cat in enumerate(CATEGORIAS, 1):   # REQUERIMIENTO 9: FOR — itera sobre tupla
        print(f"    {i}. {cat}")
    while True:
        opcion = input("  Seleccione categoría (1-6): ").strip()  # REQUERIMIENTO 3: input()

        # REQUERIMIENTO 5: CONDICIONAL if — valida la opción ingresada

        if opcion.isdigit() and 1 <= int(opcion) <= len(CATEGORIAS):
            return CATEGORIAS[int(opcion) - 1]   # Acceso a tupla por índice
        print(" Opción inválida. Elija entre 1 y 6.")



def codigo_existe(codigo):

    for p in productos:   # REQUERIMIENTO 9: FOR 
        if p["codigo"] == codigo:
            return True
    return False


# REQUERIMIENTO 8: DICCIONARIO 

def imprimir_producto(p):

    print(f"""
  ┌─────────────────────────────────────┐
  │ Código   : {p['codigo']:<26}│
  │ Nombre   : {p['nombre']:<26}│
  │ Precio   : ${p['precio']:<25.2f}│
  │ Cantidad : {p['cantidad']:<26}│
  │ Categoría: {p['categoria']:<26}│
  └─────────────────────────────────────┘""")



def agregar_producto():
    print("\n  ── AGREGAR PRODUCTO ──")

    # REQUERIMIENTO 10: VALIDACIÓN — código no vacío y no duplicado
    while True:
        codigo = input("  Código del producto: ").strip().upper()  # REQUERIMIENTO 3: input()
        # REQUERIMIENTO 5: CONDICIONAL if / elif / else
        if codigo == "":
            print("  El código no puede estar vacío.")
        elif codigo_existe(codigo):
            print(f"  Ya existe un producto con el código '{codigo}'.")
        else:
            break

    nombre = input("  Nombre del producto: ").strip()  # REQUERIMIENTO 3: input()

    # REQUERIMIENTO 10: VALIDACIÓN
    # REQUERIMIENTO 5: CONDICIONAL while
    while nombre == "":
        print("  El nombre no puede estar vacío.")
        nombre = input("  Nombre del producto: ").strip()

    precio = validar_flotante("  Precio ($): ")       # REQUERIMIENTO 4: float() 
    cantidad = validar_entero("  Cantidad en stock: ") # REQUERIMIENTO 4: int() 
    categoria = seleccionar_categoria()

    # REQUERIMIENTO 8: DICCIONARIO 
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }

    # REQUERIMIENTO 6: LISTA
    productos.append(producto)
    print(f"\n  ✔  Producto '{nombre}' agregado correctamente.")


# OPCIÓN 2 — MOSTRAR TODOS LOS PRODUCTOS

def mostrar_productos():
    print("\n  ── INVENTARIO COMPLETO ──")
    # REQUERIMIENTO 5: CONDICIONAL if
    if len(productos) == 0:
        print("  (No hay productos registrados aún.)")
        return

    print(f"  Total de productos: {len(productos)}\n")
    for i, p in enumerate(productos, 1):   # REQUERIMIENTO 9: CICLO FOR 
        print(f"  [{i}]", end="")
        imprimir_producto(p)               # REQUERIMIENTO 8: DICCIONARIO 


# OPCIÓN 3 — BUSCAR PRODUCTO

def buscar_producto():
    print("\n  ── BUSCAR PRODUCTO ──")
    # REQUERIMIENTO 5: CONDICIONAL if
    if len(productos) == 0:
        print("  (No hay productos registrados.)")
        return

    termino = input("  Ingrese nombre o código a buscar: ").strip().lower()  # REQUERIMIENTO 3: input()
    encontrados = []

    for p in productos:   # REQUERIMIENTO 9: CICLO FOR 
        # REQUERIMIENTO 5: CONDICIONAL if 
        if (termino in p["codigo"].lower() or   # REQUERIMIENTO 8
                termino in p["nombre"].lower()):
            encontrados.append(p)

    # REQUERIMIENTO 5: CONDICIONAL if / else
    if len(encontrados) == 0:
        print(f"  No se encontraron productos con '{termino}'.")
    else:
        print(f"\n  Se encontraron {len(encontrados)} resultado(s):")
        for p in encontrados:   # REQUERIMIENTO 9: CICLO FOR 
            imprimir_producto(p)


# OPCIÓN 4 — ELIMINAR PRODUCTO

def eliminar_producto():
    print("\n  ── ELIMINAR PRODUCTO ──")
    # REQUERIMIENTO 5: CONDICIONAL if
    if len(productos) == 0:
        print("  (No hay productos registrados.)")
        return

    codigo = input("  Ingrese el código o nombre del producto a eliminar: ").strip().upper()  # REQUERIMIENTO 3: input()
    producto_a_eliminar = None

    for p in productos:   # REQUERIMIENTO 9: CICLO FOR 
        # REQUERIMIENTO 5: CONDICIONAL if 
        if p["codigo"] == codigo: 
            producto_a_eliminar = p
            break

    # REQUERIMIENTO 5: CONDICIONAL if / else
    if producto_a_eliminar is None:
        print(f"  ⚠  No se encontró ningún producto con el código '{codigo}'.")
    else:
        print("\n  Producto encontrado:")
        imprimir_producto(producto_a_eliminar)
        confirmacion = input("  ¿Confirma la eliminación? (s/n): ").strip().lower()  # REQUERIMIENTO 3: input()
        # REQUERIMIENTO 5: CONDICIONAL if / else
        if confirmacion == "s":
            productos.remove(producto_a_eliminar)  # REQUERIMIENTO 6: LISTA — se elimina de la lista
            print("  ✔  Producto eliminado correctamente.")
        else:
            print("  Eliminación cancelada.")


# PROGRAMA PRINCIPAL

def main():
    mostrar_bienvenida()   # REQUERIMIENTO 1: MENSAJE DE BIENVENIDA

    # REQUERIMIENTO 2: CICLO while True
    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()  # REQUERIMIENTO 3: input()

        # REQUERIMIENTO 10: VALIDACIÓN 
        # REQUERIMIENTO 5: CONDICIONAL if
        if not opcion.isdigit() or int(opcion) not in range(1, 6):
            print("  ⚠  Opción inválida. Elija entre 1 y 5.")
            continue

        opcion = int(opcion)   # REQUERIMIENTO 4: CONVERSIÓN DE TIPO — int()

        # REQUERIMIENTO 5: CONDICIONAL if 
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_productos()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            # REQUERIMIENTO 11: SALIDA CORRECTA DEL PROGRAMA
            print("\n  ¡Hasta luego! Gracias por usar el sistema.")
            print(f"  {INFO_SISTEMA[0]} — {INFO_SISTEMA[1]}")
            break   # Termina el ciclo while y finaliza el programa


if __name__ == "__main__":
    main()