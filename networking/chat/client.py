import socket
import threading

# Send msg to the server
# Multi-threading is for communicating simultaneously

def receive_msg(client):
    # Receive server response
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print("\n" + message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_msg(client):
    #Send message to server
    while True:
        try:
            new_message = input()
            if new_message.strip().lower() == "exit" or not new_message:
                print("Disconnecting...")
                break
            client.send((new_message + "\n").encode())
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name = input("Enter your name:")
    try:
        client.connect(('127.0.0.1', 8080)) # Connect to the server
        client.send((name + "\n").encode())

        receive_thread = threading.Thread(target=receive_msg, args=(client,))
        send_thread = threading.Thread(target=send_msg, args=(client,))

        send_thread.start()
        receive_thread.start()

        send_thread.join()
        receive_thread.join()
    except KeyboardInterrupt:
        print("\nDisconnect from the server")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()