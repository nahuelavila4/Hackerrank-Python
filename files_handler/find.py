import os

def fbn():
    ruta = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta, "logs_test/webserver.log")
    codigo_estado = {200: 0, 300: 0, 400: 0, 500: 0}
    urls = {}
    with open(ruta_archivo) as f:
        lista = f.readlines()
        for i in range(0, len(lista)):
            status = lista[i].split()[-2]
            ruta = lista[i].split()[-4]
            for x in codigo_estado: # Guarda cantidad de veces que se devolvio un codigo
                if int(status) == x: codigo_estado[x] += 1
            if ruta in urls: urls[ruta] += 1
            else: urls[ruta] = 1
            print(f"El codigo de estado de la peticion {i+1} es {status}")
            if int(status) >= 200 and int(status) <= 299: print("Success: la solicitud fue recibida, entendida y aceptada con éxito")
            elif int(status) >= 300 and int(status) <= 399: print("Redirección: se deben tomar medidas adicionales para completar la solicitud")
            elif int(status) >= 400 and int(status) <= 499: print("Error de cliente: la solicitud contiene una sintaxis incorrecta o no se puede cumplir")
            elif int(status) >= 500 and int(status) <= 599: print("Error de servidor: el servidor no pudo cumplir con una solicitud aparentemente válida")
            print(f"La ruta solicitada es {ruta}\n")
        mayor = max(urls, key=urls.get) 
        print(f"La ruta mas solicitada en las peticiones es {mayor}")

fbn()


