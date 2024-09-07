# ---------------------------------------------
# Ejercicio 9: Encontrar las vocales en una cadena

cadena = "Thmtlkytmlk unbgb E"
vocales = ["a", "e", "i", "o", "u"]

vocales_cadena = [caract for caract in cadena for elem in vocales if caract.lower() == elem]

#print("Vocales de la cadena")
#print(vocales_cadena)   

# ---------------------------------------------
# Ejercicio 10: Crear una lista con el reverso de las palabras

palabras = ["Hola", "Mundo", "Python"]
reverso = [palab[::-1] for palab in palabras ]
print("Palabras al reverso")
print(reverso)

# ---------------------------------------------
# Ejercicio 10: Crear una lista con el reverso de las palabras











