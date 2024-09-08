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
#print("Palabras al reverso")
#print(reverso)

# ---------------------------------------------
# Anotaciones Hackerrank - Ejercicio 1

a = 1
b = 2
c = 1
n = 3

valores = []
combinaciones = [[x, y, z] for x in range(0, a+1) for y in range(0, b+1) for z in range(0, c+1) if (x+y+z) != n]

# ---------------------------------------------
# Anotaciones Hackerrank - Ejercicio 2

numeros = [1241, 45, 16, 15475, 2640]
mayor = None
runner_up = None

for index, val in enumerate(numeros):
    if mayor == None or val > mayor:
        runner_up = mayor
        mayor = val
    elif runner_up == None or (val < mayor and val > runner_up):
        runner_up = val

#print("Numero mayor: "+ str(mayor))
#print("Segundo numero mayor: "+ str(runner_up))





