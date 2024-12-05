import os

def fbn():
    ruta = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta, "logs_test/webserver.log")
    with open(ruta_archivo, "r") as f:
        content = f.read()
        print(content)


fbn()