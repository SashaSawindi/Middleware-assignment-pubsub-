import socket
import sys

if len(sys.argv) != 2:
    print("Use the format: python server.py <PORT>")
    sys.exit(1)

HOST = "0.0.0.0" 
PORT = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST} : {PORT}")
    conn, addr = s.accept() 

    with conn:
        print(f"Connected by {addr}") 
        while True:
            data = conn.recv(1024)
            message = data.decode()

            if message == "terminate":
                print("Connection terminated by client.")
                break

            if not data:
                break
            message = data.decode()
            print(f"Received: {message}")  