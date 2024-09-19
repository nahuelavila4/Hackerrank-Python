import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('localhost', 8080))

#Send message
client.send("Hello im the client".encode())

# Receive server response
response = client.recv(1024).decode()
print(f"Server response: {response}")

client.close()