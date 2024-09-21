import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 8080))

#Send message
new_message = input("Message:")
new_message += "\n"
new_message.encode()
client.send(new_message.encode())

# Receive server response
response = client.recv(1024).decode()
print(f"Server: your message has been received. Lenght: {response}")

client.close()