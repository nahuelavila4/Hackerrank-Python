import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 8080))

#Send message
client.send(input("Message:").encode())

# Receive server response
response = client.recv(1024).decode()
print(f"Server response: {response}")

client.close()