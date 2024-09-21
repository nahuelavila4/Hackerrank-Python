import socket
import threading

# calculate how many bytes to receive from client
def receive_msg(client):
    message = ""
    while True:
        part = client.recv(1024).decode()  # Recibe en fragmentos
        message += part
        if '\n' in part:  # Verifica si hay un delimitador
            break
    return message.strip() 

# send message
def send_msg(client, message):
    formatted_msg = f"{len(message):02}"
    client.send(formatted_msg.encode())

# Manage specific client message
def handle_client(client):
    while True:
        try:
            # Transform bytes to text - recv receive up to 1024 bytes
            message = receive_msg(client)
            if message == "EXIT" or not message:
                print("Client disconnect")
                break # If client close connection
            print(f"Client message: {message}")
            send_msg(client, message) # Response to the client
        except (Exception, KeyboardInterrupt) as e:
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
        (clientsocket, addr) = server.accept() # Wait Connections
        print(f"Connection accepted for: {addr}")
    
        client_thread = threading.Thread(target=handle_client, args=(clientsocket,))
        client_thread.start()

if __name__ == "__main__":
    main()