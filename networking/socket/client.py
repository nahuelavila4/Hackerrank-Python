import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    HOST = "127.0.0.1"
    PORT = 2354

    client.connect((HOST, PORT))

    while True:
        #Message to the server
        msg = input("Enter message: ")
        client.send(msg.encode("utf-8")[:1024])

        #Receive message
        response = client.recv(1024)
        response = response.decode("utf-8")

        if (response.lower() == "closed"):
            break
        print(f"Received: {response}")

    #close client socket (connection to the server)
    client.close()
    print("Connection to server closed")

run_client()