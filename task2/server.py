import socket
import threading
import sys

clients = []
clients_lock = threading.Lock()
subscribers = []

def handle_client(conn, addr, role):
    global clients, subscribers
    print(f"{role} connected from {addr}")
    if role == "SUBSCRIBER":
        with clients_lock:
            subscribers.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            if message.strip().lower() == "terminate":
                break
            if role == "PUBLISHER":
                with clients_lock:
                    for sub in subscribers:
                        try:
                            if sub != conn:
                                sub.sendall(message.encode())
                        except:
                            pass
            print(f"Received from {role} {addr}: {message}")
    finally:
        conn.close()
        with clients_lock:
            if conn in subscribers:
                subscribers.remove(conn)
            if conn in clients:
                clients.remove(conn)

def main():
    if len(sys.argv) != 2:
        print("Usage: python server.py <PORT>")
        return

    PORT = int(sys.argv[1])
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen(5)
    print(f"Server listening on port {PORT}...")

    while True:
        conn, addr = server_socket.accept()
        role = conn.recv(1024).decode()
        with clients_lock:
            clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr, role)).start()

if __name__ == "__main__":
    main()
