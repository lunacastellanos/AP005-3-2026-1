# 1. Acceso a valores mediante una clave (Get a Key)
# Se obtiene un valor del diccionario usando su clave
building_heights = {
    "Burj Khalifa": 828, 
    "Shanghai Tower": 632, 
    "Abraj Al Bait": 601, 
    "Ping An": 599, 
    "Lotte World Tower": 554.5, 
    "One World Trade": 541.3
}

print(building_heights["Burj Khalifa"])  # Accede al valor 828
print(building_heights["Ping An"])       # Accede al valor 599


# 2. Acceso a listas dentro de un diccionario
# Los valores pueden ser listas y se accede igual con la clave
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"], 
    "fire": ["Aries", "Leo", "Sagittarius"], 
    "earth": ["Taurus", "Virgo", "Capricorn"], 
    "air": ["Gemini", "Libra", "Aquarius"]
}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])


# 3. Error al acceder a una clave inexistente
# Esto genera un error (KeyError)
# print(building_heights["Landmark 81"])


# 4. Verificación de existencia de una clave
# Se usa "in" para evitar errores
key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights[key_to_check])


# 5. Agregar nueva clave y verificarla
# Se añade una nueva entrada al diccionario
zodiac_elements["energy"] = "Not a Zodiac element"

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])


# 6. Obtener valores de forma segura con get()
# get() evita errores si la clave no existe
building_heights.get("Shanghai Tower")  # Devuelve 632
building_heights.get("My House")        # Devuelve None


# 7. Uso de get() con condiciones
# Permite asignar valores por defecto si no existe la clave
user_ids = {
    "teraCoder": 100019, 
    "pythonGuy": 182921, 
    "samTheJavaMaam": 123112, 
    "lyleLoop": 102931, 
    "keysmithKeith": 129384
}

if user_ids.get("teraCoder") == None:
    tc_id = 1000
else:
    tc_id = user_ids.get("teraCoder")

print(tc_id)

if user_ids.get("superStackSmash") == None:
    stack_id = 100000

print(stack_id)


# 8. Eliminación de elementos con pop()
# pop elimina una clave y devuelve su valor
raffle = {
    223842: "Teddy Bear", 
    872921: "Concert Tickets", 
    320291: "Gift Basket", 
    412123: "Necklace", 
    298787: "Pasta Maker"
}

print(raffle.pop(320291, "No Prize"))  # Elimina y devuelve valor
print(raffle)

print(raffle.pop(100000, "No Prize"))  # No existe, devuelve valor por defecto
print(raffle)

print(raffle.pop(872921, "No Prize"))  # Elimina otra clave
print(raffle)


# 9. Uso práctico de pop() con operaciones
# Se eliminan elementos y se usan sus valores
available_items = {
    "health potion": 10, 
    "cake of the cure": 5, 
    "green elixir": 20, 
    "strength sandwich": 25, 
    "stamina grains": 15, 
    "power stew": 30
}

health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)


# 10. Obtener todas las claves (keys)
# keys() devuelve todas las claves del diccionario
test_scores = {
    "Grace": [80, 72, 90], 
    "Jeffrey": [88, 68, 81], 
    "Sylvia": [80, 82, 84], 
    "Pedro": [98, 96, 95], 
    "Martin": [78, 80, 78], 
    "Dina": [64, 60, 75]
}

print(list(test_scores))  # Convierte claves a lista

for student in test_scores.keys():
    print(student)


# 11. Obtener claves de diferentes diccionarios
user_ids = {
    "teraCoder": 100019, 
    "pythonGuy": 182921, 
    "samTheJavaMaam": 123112, 
    "lyleLoop": 102931, 
    "keysmithKeith": 129384
}

num_exercises = {
    "functions": 10, 
    "syntax": 13, 
    "control flow": 15, 
    "loops": 22, 
    "lists": 19, 
    "classes": 18, 
    "dictionaries": 18
}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


# 12. Obtener todos los valores (values)
# values() devuelve los valores del diccionario
for score_list in test_scores.values():
    print(score_list)

total_exercises = 0

for exercises in num_exercises.values():
    total_exercises += exercises

print(total_exercises)


# 13. Obtener claves y valores (items)
# items() devuelve pares clave-valor
biggest_brands = {
    "Apple": 184, 
    "Google": 141.7, 
    "Microsoft": 80, 
    "Coca-Cola": 69.7, 
    "Amazon": 64.8
}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")


# 14. Ejemplo práctico con items()
pct_women_in_occupation = {
    "CEO": 28, 
    "Engineering Manager": 9, 
    "Pharmacist": 58, 
    "Physician": 40, 
    "Lawyer": 37, 
    "Aerospace Engineer": 9
}

for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")