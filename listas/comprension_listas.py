# Ejercicio 2 - Mostrar solo pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]

#print("Lista de numeros pares")
#print(pares)

# -------------------------------------
# Ejercicio 3 - Convertir en minusculas

cadenas = ["Hola", "Mundo", "PYTHON", "Es", "Genial"]
minus = [n.lower() for n in cadenas]

#print("Cadenas convertidas a minusculas")
#print(minus)

# -------------------------------------
# Ejercicio 4 - Números divisibles por 3 y 5 en una lista

num = [n for n in range(1, 51) if n%3 == 0 and n%5 == 0]
#print("Números divisibles por 3 y 5")
#print(num)

# -------------------------------------
# Ejercicio 5 - Crear una lista de pares (índice, valor)

count = -1
valores = ['a', 'b', 'c', 'd']
keyval = [(index, n) for index, n in enumerate(valores)]

#print(keyval)

# ----------------------------------------------
#Ejercicio 7: Lista de números pares y sus cuadrados

pares2 = [(num, num**2) for num in range(1, 11) if num%2 == 0]
#print(pares2)

# ---------------------------------------------
# Ejercicio 8: Aplanar una lista de listas

listas = [[1, 2, 3], [4, 5], [6, 7, 8]]

lista_individual = [element for sublist in listas for element in sublist]
#print(lista_individual)











