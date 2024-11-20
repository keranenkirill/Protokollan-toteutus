import socket
import os

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 65432  # Port number (you can change this)


def handle_request(request):
    # Pilko pyyntö osiin
    parts = request.strip().split(' ', 1)
    if len(parts) < 2:
        return "ERROR: Invalid request format"

    method, parameter = parts[0], parts[1]

    # käsitellään GET pyyntö
    if method == "GET":
        if os.path.isfile(parameter):
            with open(parameter, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            return "ERROR: File not found"
    # käsittele ECHO pyyntö
    elif method == "ECHO":
        return parameter
    else:
        return "ERROR: Unknown method"


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server is running on {HOST}:{PORT}...")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                response = handle_request(data)
                client_socket.sendall(response.encode('utf-8'))


run_server()
