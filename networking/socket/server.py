import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 2354
    server.bind((HOST, PORT))
    server.listen(0)
    print(f"Listening on {HOST} in the port {PORT}")
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    #While mantiene servidor en espera de mensajes
    while True:
        #recv obtain client response
        request = client_socket.recv(1024)
        #Convert byte to string
        request = request.decode("utf-8")

        if (request.lower() == "close"):
            client_socket.send("closed".encode("utf-8"))
            break

        print(f"Received: {request}")
        response = "accepted".encode("utf-8")
        client_socket.send(response)
    
    client_socket.close()
    print("Connection closed")
    server.close()

run_server()

    