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
    