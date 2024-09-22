import socket
import threading

list_clients = []

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
def send_msg(sender_client, message):
    # formatted_msg = f"{message}. Lenght: {len(message):02}"
    for c in list_clients:
        if c != sender_client: # Si client es otro q no envio el mensaje
            try:
                c.send(message.encode())
            except Exception as e:
                print(f"Error: {e}")

# Manage specific client message
def handle_client(client):
    try:
        # Client name
        name = client.recv(1024).decode()
        while True:
            # Transform bytes to text - recv receive up to 1024 bytes
            message = receive_msg(client)
            if message.strip().lower() == "exit" or not message:
                print(f"Client {name} disconnected.")
                break # If client close connection
            print(f"{name}: {message}")
            send_msg(client, f"{name}: {message}") # Response to the client
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if client in list_clients:
            list_clients.remove(client)
        client.close()

# Principal function to server
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    print("Waiting for connections...")
    # list_clients = []
    # Principal Loop
    try:
        while True:
            (client_socket, addr) = server.accept() # Wait Connections
            list_clients.append(client_socket)
            print(f"Connection accepted for: {addr}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt: # Eg ctrl+c
        print("\n Shutting down the server.")
    except ConnectionError:
        print("Connection error. The server might not be available.")
    except Exception as e:  # Any other exception
        print(f"Ocurrió un error: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    main()