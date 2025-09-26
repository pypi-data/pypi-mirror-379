import socket
import threading


if __name__ == "__main__":
    address = 'localhost'
    port = 1234
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((address, port))
    
    print(f"Connected to server at {address}:{port}")

    client_socket.sendall(b'$RESTART$')
