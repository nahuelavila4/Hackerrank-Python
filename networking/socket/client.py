import socket
from pwn import *

def run_client():
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 2354

    r = remote(HOST, PORT)
    #client.connect((HOST, PORT))

    while True:
        #Message to the server
        msg = input("Enter message: ")
        r.sendline(msg.encode("utf-8"))

        #Receive message
        response = r.recv(1024)

        if (response.lower() == "closed"):
            break
        print(response.decode("utf-8"))

    #close client socket (connection to the server)
    r.close()
    print("Connection to server closed")

run_client()