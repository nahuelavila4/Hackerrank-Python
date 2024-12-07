import os

def fbn():
    ruta = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta, "logs_test/webserver.log")
    with open(ruta_archivo) as f:
        lista = f.readlines()
        for i in range(0, len(lista)):
            s = lista[i].split()
            status = s[-2]
            if int(status) != 200:
                print(f"La peticion {i+1} devolvio un codigo de estado erroneo")
            else:
                print(f"La peticion {i+1} devolvio un codigo de estado correcto")


fbn()