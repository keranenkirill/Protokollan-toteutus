import socket

# Client configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The same port as used by the server


def send_request(recuest_file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(recuest_file)
        server_response = client_socket.recv(1024).decode('utf-8')
        return server_response


# GET-metodi, joka ottaa parametrina tiedoston nimen ja
# palvelin palauttaa asiakkaalle tiedoston sisällön
RECUEST_GET_FILE = b"GET testfile.txt"
response = send_request(RECUEST_GET_FILE)
print(f"Server response: {response}")
