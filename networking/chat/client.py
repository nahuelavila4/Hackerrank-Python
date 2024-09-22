import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080)) # Connect to the server
    name = input("Enter your name:")
    client.send(name.encode())
    while True:
        
        #Send message
        new_message = input("Message:")
        new_message += "\n"
        new_message.encode()
        client.send(new_message.encode())

        # Receive server response
        response = client.recv(1024).decode()
        print(response)
except KeyboardInterrupt:
    print("\nDisconnect from the server")
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()