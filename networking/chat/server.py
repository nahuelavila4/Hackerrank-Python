import socket
import threading

# Thread send msg to all clients

list_clients = []

# calculate how many bytes to receive from client
def receive_msg(client):
    try:
        message = ""
        while True:
            part = client.recv(1024).decode()  # Recibe en fragmentos
            message += part
            if '\n' in part:  # Verifica si hay delimitador
                break
        return message.strip()
    except Exception as e:
        print(f"Error receiving message: {e}")

# send message
def send_msg(sender_client, message, name):
    formatted_msg = f"{name}: {message}\n"
    for client, sender_name in list_clients:
        if client != sender_client: # Si client es otro q no envio el mensaje
            try:
                client.send(formatted_msg.encode())
            except Exception as e:
                print(f"Error: {e}")

# Manage specific client message
def handle_client(client):
    try:
        name = client.recv(1024).decode().strip()
        list_clients.append((client, name))
        print(f"Client {name} connected")
        while True:
            # Transform bytes to text 
            message = receive_msg(client)
            if message.strip().lower() == "exit" or not message:
                print(f"Client {name} disconnect")
                break
            print(f"{name}: {message}") # What you see in server
            send_msg(client, message, name) # Response to the client
    except Exception as e:
        print(f"Error handling client {name}: {e}")
    finally:
        list_clients.remove((client, name))
        client.close()
        print(f"Client {name} has been removed from the list.")

# Principal function to server
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    print("Waiting for connections...")
    try:
        while True:
            (client_socket, addr) = server.accept() # Wait Connections
            print(f"Connection accepted for: {addr}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt: # Eg ctrl+c
        print("\n Shutting down the server.")
    except ConnectionError:
        print("Connection error. The server might not be available.")
    except Exception as e:  # Any other exception
        print(f"Error: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    main()