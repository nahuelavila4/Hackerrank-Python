import socket

def handle_client(client, url):
    if url == "/":
        # Ruta principal
        response_body = "<h1>Welcome to the Home Page!</h1>"
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{response_body}"
    elif url == "/about":
        response_body = "<h1>About we</h1>"
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{response_body}"
    elif url == "/service":
        response_body = "<h1>Ours services</h1>"
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{response_body}"
    else:
        response_body = "<h1>404 Not Found</h1>"
        response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n{response_body}"
    client.sendall(response.encode())
    

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))

server_socket.listen(5)
print("Server is running...")

while True:
    (client_socket, addr) = server_socket.accept() # Wait Connections
    print(f"Connection accepted for: {addr}")

    # Receive
    request = client_socket.recv(1024).decode()
    request_line = request.splitlines()[0]
    # Extract method and URL
    method, url, http_version = request_line.split()

    handle_client(client_socket, url)
    client_socket.close()
   