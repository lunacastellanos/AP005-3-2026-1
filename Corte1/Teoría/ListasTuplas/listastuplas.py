################# LISTAS ####################
############################################

# 1. Definición y creación de listas
# Se crea una lista con varios elementos (colores)
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

# Se imprime la lista y su tipo de dato
print(my_lista)
print(type(my_lista))

# Acceso a un elemento por índice
print(my_lista[2])  # Amarillo


# 2. Tamaño y slicing (sublistas)
# len() devuelve la cantidad de elementos
print("my_lista size:", len(my_lista))

# Slicing: obtiene una parte de la lista
print(my_lista[0:2])
print(my_lista[:2])


# 3. Agregar elementos a la lista
# append() agrega un elemento al final
my_lista.append('Blanco')
print(my_lista)

# insert() agrega en una posición específica
my_lista.insert(3, 'Negro')
print(my_lista)


# 4. Extender listas
# extend() agrega varios elementos (otra lista)
my_lista.extend(['Marron', 'Gris'])
print(my_lista)


# 5. Buscar elementos en la lista
# index() devuelve la posición de un elemento
print(my_lista.index('Azul'))


# 6. Eliminar elementos
# remove() elimina un elemento por valor
my_lista.remove('Marron')
print(my_lista)

# Se vuelve a insertar el elemento
my_lista.insert(8, 'Marron')
print(my_lista)

# pop() elimina el último elemento y lo devuelve
print(my_lista.pop())

# Tamaño actual de la lista
size = len(my_lista)
print("size =", size)


# 7. Repetición de listas
# Se multiplica la lista (se repite)
my_lista_3 = my_lista * 3
print("my_lista_3:", my_lista_3)


# 8. Ordenamiento de listas
print("Sort:")
print()

# sort() ordena la lista (modifica la original)
my_listaSort = my_lista.sort()
print(my_listaSort)  # Devuelve None (error común)


# 9. Ordenamiento de listas numéricas
my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Ordering my_NumList:")
my_NumList.sort()
print(my_NumList)

# Ordenar de mayor a menor
my_NumList.sort(reverse=True)
print("De menor a mayor:", my_NumList)



################# TUPLAS ####################
############################################

# 10. Definición de tuplas
# Son similares a listas pero INMUTABLES (no se pueden modificar)
print("###########################")
print("###########################")
print("###########################")
print("############ TUPLAS #########")

# Convertir lista a tupla
my_tupla = tuple(my_lista)
print("my_tuple:", my_tupla)


# 11. Acceso a elementos en tupla
print(my_tupla[0])
print(my_tupla[2])


# 12. Operaciones con tuplas
# Verificar si un elemento está en la tupla
print('Rojo' in my_tupla)

# Contar cuántas veces aparece un elemento
print(my_tupla.count('Rojo'))


# 13. Tupla con un solo elemento (error común)
# Esto NO es una tupla realmente (falta coma)
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)


# 14. Empaquetado de tuplas
# Se puede crear una tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)


# 15. Desempaquetado de tuplas
# Se asignan los valores a variables en orden
nombre, dia, mes, año = my_tupla

print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre:", nombre, "- Dia:", dia, "- Mes:", mes, "- Año:", año)


# 16. Convertir tupla a lista
# Se puede transformar para poder modificarla
my_lista2 = list(my_tupla)
print(my_lista2)