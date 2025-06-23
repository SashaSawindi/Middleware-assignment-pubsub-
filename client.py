import socket
import sys

if len(sys.argv) != 3:
    print("Use the format: python client.py <HOST> <PORT>")
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    try:
        s.connect((HOST, PORT))
        print(f"Connected to server at {HOST} : {PORT}")
    except socket.error as e:
        print(f"Connection failed: {e}")
        sys.exit(1)
    
    while True:
        message = input("Type a message (or 'terminate' to exit): ")
        s.sendall(message.encode())
        
        if message.strip().lower() == "terminate":
            print("Closing connection...")
            break