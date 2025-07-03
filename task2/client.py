import socket
import sys
import threading

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(f"[Received]: {data.decode()}")
        except:
            break

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <SERVER_IP> <PORT> <PUBLISHER/SUBSCRIBER>")
        return

    SERVER_IP = sys.argv[1]
    PORT = int(sys.argv[2])
    ROLE = sys.argv[3].upper()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    client_socket.sendall(ROLE.encode())

    if ROLE == "SUBSCRIBER":
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input("Enter message (type 'terminate' to exit): ")
        client_socket.sendall(message.encode())
        if message.strip().lower() == "terminate":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
