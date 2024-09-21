import socket
import threading

# Manage specific client message
def handle_client(client):
    while True:
        try:
            # Transform bytes to text - recv receive up to 1024 bytes
            message = client.recv(1024).decode()
            if not message:
                break # Exit loop if client close connection
            print(f"Client message: {message}")
            client.sendall(b"message received")
        except Exception as e:
            print(f"Error: {e}")
    client.close()

# Principal function to server
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    print("Waiting for connections...")

    # Principal Loop
    while True:
        (clientsocket, clientaddress) = server.accept() # Wait Connections
        print(f"Connection accepted for: {clientaddress}")
    
        client_thread1 = threading.Thread(target=handle_client, args=(clientsocket,))
        client_thread1.start()

if __name__ == "__main__":
    main()