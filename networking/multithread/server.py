import socket
import threading

def handle_client(conn, addr):
    print(f"Conexion establecida con {addr}")
    while True:
        #try-except maneja situaciones excepcionales
        try:
            msg = conn.recv(1024)
            
            #Si cliente cerró conexion correctamente
            if not msg:
                print(f"El cliente no envio mensaje")
                break
            print(f"Mensaje recibido del cliente {addr}: {msg.decode("utf-8")}")
        except ConnectionResetError:
            print(f"El cliente {addr} se desconecto abruptamente")
            break
        except Exception as e:
            print(f"Error con el cliente {addr}: {str(e)}")
            break
