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

# ---------------------------------------------
# Anotaciones Hackerrank - Ejercicio 3
# A partir de lista de listas, mostrar notas con segundo valor más bajo

# Obtener las notas únicas:
# En lugar de intentar mantener manualmente las dos notas más bajas, 
# puedes recolectar todas las notas, eliminar duplicados y luego ordenar para encontrar las notas más bajas.
# Filtrar alumnos:
# Una vez que se identifica la segunda nota más baja, se filtran los alumnos que tienen esa nota.
""" 
notas = sorted(set([alumno[1] for alumno in alumnos]))
print(notas)
# Identificar la segunda nota más baja, por orden esta en la posicion 2
if len(notas) > 1:
    segundamenor = notas[1] 
else:
    segundamenor = None 

if segundamenor != None:
    alumnosbajanota = [alumno[0] for alumno in alumnos if alumno[1] == segundamenor]
    alumnosbajanota.sort()  
    print("\n".join(alumnosbajanota))
 """
# ---------------------------------------------
# Anotaciones Hackerrank - Ejercicio 4
# A partir de lista de listas, mostrar notas con segundo valor más bajo

alumnosprom = {
    'Lucas': [92.00, 73.00, 12.00],
    'Camila': [73.00, 19.00, 55.00],
    'Cristian': [46.00, 75.00, 68.00],
    'Gustavo': [12.00, 45.00, 58.00]
}

nombreprom = 'Camila'
notas = alumnosprom[nombreprom]
promedio = sum(notas) / len(notas)


print(f"{promedio:.2f}")


