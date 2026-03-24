# 1. Definición y construcción de diccionarios
# Se crean diccionarios
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Se imprimen los diccionarios
print(sensors)
print(num_cameras)


# 2. Diccionario de traducciones
# Ejemplo de diccionario que almacena palabras y sus significados
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations)


# 3. Verificación de errores en diccionarios
# Las listas NO pueden ser claves porque son mutables
# Esto generaría un error si se ejecuta
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}


# 4. Diccionarios con listas como valores
# Un diccionario puede tener listas como valores
children = {
    "von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
    "Corleone": ["Sonny", "Fredo", "Michael"]
}
print(children)


# 5. Creación de un diccionario vacío
# Se puede inicializar un diccionario sin elementos
my_empty_dictionary = {}
print(my_empty_dictionary)


# 6. Agregar un nuevo par clave-valor
# Se añade un elemento al diccionario usando una nueva clave
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before:", menu)

menu["cheesecake"] = 8  # Se agrega un nuevo producto
print("After:", menu)


# 7. Sobrescritura de diccionarios
# Si se redefine un diccionario, se pierde el valor anterior
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)


# 8. Agregar múltiples elementos con update()
# Permite añadir varias claves al mismo tiempo
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before:", sensors)

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After:", sensors)


# 9. Actualización de diccionarios existentes
# Se pueden agregar nuevos usuarios fácilmente
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


# 10. Modificación de valores existentes
# Si la clave ya existe, su valor se reemplaza
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before:", menu)

menu["oatmeal"] = 5  # Se cambia el valor existente
print("After:", menu)


# 11. Ejemplo combinado: agregar y modificar datos
oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

print("Before:", oscar_winners)

oscar_winners.update({"Supporting Actress": "Viola Davis"})  # Agrega nueva clave
print("After1:", oscar_winners)

oscar_winners["Best Picture"] = "Moonlight"  # Modifica valor existente
print("After2:", oscar_winners)


# 12. Uso de zip() para combinar listas
# Une dos listas en pares (tuplas)
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

zipStudents = zip(names, heights)
print("zipStudents:", zipStudents)


# 13. Diccionarios por comprensión (dict comprehension)
# Permite crear diccionarios de forma rápida
students = {key: value for key, value in zip(names, heights)}
print(students)


# 14. Otro ejemplo con bebidas y cafeína
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)


# 15. Aplicación práctica con canciones
# Se crea un diccionario a partir de listas relacionadas
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key: value for key, value in zip(songs, playcounts)}
print(plays)


# 16. Actualización y modificación de datos
# Se agrega una nueva canción y se actualiza otra
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After:", plays)


# 17. Diccionarios anidados
# Un diccionario puede contener otros diccionarios
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)