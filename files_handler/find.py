import os
import matplotlib.pyplot as plt
import numpy as np


def main_handler():
    print("Bienvenido\n")
    inicio = input("Seleccione la cantidad de archivos que va a analizar\n1. Un archivo\n2. Varios\n\n")
    if inicio == "1":
        archivo = input("Nombre del archivo: ") 
        general(archivo)
    elif inicio == "2": 
        analizar_varios()
    else: 
        print("Por favor ingrese un valor valido.")
        main_handler()

def general(log):
    ruta = os.path.dirname(os.path.abspath(__file__)) # Ruta de script
    ruta_archivo = os.path.join(ruta, f"logs_test/{log}")
    metodos_peticiones = {
        "GET": {}, "POST": {},
        "PUT": {}, "HEAD": {},
        "DELETE": {}, 
    }
    with open(ruta_archivo) as f:
        lista = f.readlines()
        for i in range(0, len(lista)):
            status, ruta, metodo = lista[i].split()[-2], lista[i].split()[-4], lista[i].split()[-5]
            e = metodo.split('"')
            metodo = "".join(e)
            print(metodo)
            
            buscar_ataques(ruta)
            for met in metodos_peticiones:
                if metodo == met:
                    if status in metodos_peticiones[met].keys():
                        metodos_peticiones[met][status] += 1
                    else:
                        metodos_peticiones[met][status] = 1
            
            print(f"El codigo de estado de la peticion {i+1} es {status}")
            if int(status) >= 200 and int(status) <= 299: 
                print("Success: la solicitud fue recibida, entendida y aceptada con éxito")
            elif int(status) >= 300 and int(status) <= 399: 
                print("Redirección: se deben tomar medidas adicionales para completar la solicitud")
            elif int(status) >= 400 and int(status) <= 499: 
                print("Error de cliente: la solicitud contiene una sintaxis incorrecta o no se puede cumplir")
            elif int(status) >= 500 and int(status) <= 599: 
                print("Error de servidor: el servidor no pudo cumplir con una solicitud aparentemente válida")
            print(f"La ruta solicitada es {ruta}\n")
        print(metodos_peticiones)
        grafico = input("¿Quieres ver el grafico comparativo de este archivo? (y/n): ")
        if grafico == "y":
            matplot(metodos_peticiones)
        print("\n--------------------------------------------\n")

def analizar_varios():
    archivos = os.listdir("./logs_test")
    for archivo in archivos:
        if archivo.endswith(".log"):
            print(f"Iniciando analisis del archivo {archivo}")
            general(archivo)

# XSS y SQL Injection
def buscar_ataques(ruta):
    sql = [";--", "union select", "order by", "OR 1 = 1", "--'"]
    ataques_detectados = {"SQL": 0, "XSS": 0}
    for ataque in sql:
        if ataque in ruta:
            ataques_detectados["SQL"] += 1
        elif "<script>" in ruta:
            ataques_detectados["XSS"] += 1
        total = sum(ataques_detectados.values())
    if total > 0:
        print(f"Amenazas totales encontradas: {total}")
        for ataques in ataques_detectados:
            print(ataques+": "+str(ataques_detectados[ataques]))
    else:
        print(f"No hay amenazas en la ruta solicitada")

def matplot(metodos_dic):
    metodos = list(metodos_dic.keys()) # ["GET", "POST", "PUT"]
    codigos = set() # ("200", "400", "500")
    for valores in metodos_dic.values(): 
        codigos.update(valores.keys()) # Guarda codigos unicos
    codigos = sorted(codigos)
    valores_codigos = {codigo: [] for codigo in codigos}
    # Estructura: {codigo: [cant_en_get, cant_en_post, etc]}
    for metodo in metodos:
        for codigo in codigos:
            valores_codigos[codigo].append(metodos_dic[metodo].get(codigo, 0))
    print(valores_codigos)

    eje_x = np.arange(len(metodos)) # Crea posiciones para cada metodo
    plt.figure(figsize=(10, 6))
    bottom = np.zeros(len(metodos)) # Posicion inicial para las barras de cada metodo

    for codigo, valores in valores_codigos.items():
        plt.bar(eje_x, valores, label=f"Codigo {codigo}", bottom=bottom) # Agrega una barra
        bottom += np.array(valores)
    
    plt.xticks(eje_x, metodos)  # Etiquetas en el eje X
    plt.xlabel("Métodos HTTP")  # Etiqueta del eje X
    plt.yticks(range(0, int(max(bottom)) + 2, 1))
    plt.ylabel("Cantidad de Peticiones")  # Etiqueta del eje Y
    plt.title("Relación entre Métodos HTTP y Códigos de Estado")  # Título del gráfico
    plt.legend(title="Códigos de Estado")  # Leyenda con título
    plt.tight_layout()  # Ajuste automático para que todo se vea bien
    plt.show()

if __name__ == "__main__":
    main_handler()


