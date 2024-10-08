import socket
import os

STATIC_DIR = "./static"

def build_response(status, content_type, body):
    # Si el cuerpo es un string, lo codificamos en bytes
    if isinstance(body, str):
        body = body.encode()
    response = (
        f"HTTP/1.1 {status}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
    ).encode() + body
    return response

def get_content_type(file_path):
    if file_path.endswith(".html"):
        return "text/html"
    elif file_path.endswith(".css"):
        return "text/css"
    elif file_path.endswith(".js"):
        return "application/javascript"
    elif file_path.endswith(".png"):
        return "image/png"
    elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
        return "image/jpeg"
    else:
        return "application/octet-stream" 
    
def handle_static_file(client_socket, file_path):
    try:
        if file_path == "/":
            file_path = "index.html"
        else:
            # Eliminar el "/" inicial de la URL para crear correctamente la ruta
            if file_path.startswith("/"):
                file_path = file_path[1:]

        full_path = os.path.join("static", file_path).replace("\\", "/")
        print("path "+file_path)
        print(f"Full path: {full_path}")
        if os.path.exists(full_path) and os.path.isfile(full_path):
            with open(full_path, "rb") as file:  # Abrir en modo binario para archivos de imagen
                content = file.read()
            content_type = get_content_type(full_path)
            response = build_response("200 OK", content_type, content)
            client_socket.sendall(response)
        else: 
            response = build_response("404 Not found", "text/html", "<h1>404 Not Found</h1>")
            client_socket.sendall(response)
    except Exception as e:
        print(f"Error: {e}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))

server_socket.listen(5)
print("Server is running...")

while True:
    (client_socket, addr) = server_socket.accept() # Wait Connections
    print(f"Connection accepted for: {addr}")
    try:
        # Receive
        request = client_socket.recv(1024).decode()
        request_line = request.splitlines()[0]
        # Extract method and URL
        method, url, http_version = request_line.split()

        if url == "/":
            url = "/index.html"  # Redirigir a index.html si es la raíz
        handle_static_file(client_socket, url)  
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
   