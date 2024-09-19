import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(5)
print("The server is waiting for connections")

# Manage client message
def handle_client(client):
    while True:
        message = clientsocket.recv(1024).decode()
        if not message:
            break
        print(f"Client message: {message}")
    client.close()


while True:
    # Wait Connections
    (clientsocket, clientaddress) = server.accept()
    print(f"Connection accepted for: {clientaddress}")
    
    # Transform bytes to text - .recv() receive up to 1024 bytes
    message = clientsocket.recv(1024).decode()
    print(f"Client message: {message}")

    clientsocket.send("Hello mister client".encode())

