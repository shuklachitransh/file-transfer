import socket
import os
import threading

# Configuration
HOST = ''  # Server IP (empty means bind to all interfaces)
PORT = 10000  # Server port
BUFFER_SIZE = 1024  # Buffer size for sending data
SERVER_FILES_DIR = 'ServerFiles/'  # Directory where files are stored

# List to store connected clients
clients = []

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

def send_file_to_client(file_path, client_addr):
    """Send a file to a specific client."""
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            server_socket.sendto(data, client_addr)

def handle_client_request(data, client_addr):
    """Handle different client requests."""
    global clients
    request = data.decode('utf-8').strip()

    if client_addr not in clients:
        clients.append(client_addr)

    if request == 'LIST':
        files = os.listdir(SERVER_FILES_DIR)
        response = '\n'.join(files) if files else 'No files available.'
        server_socket.sendto(response.encode('utf-8'), client_addr)

    elif request.startswith('FILE '):
        file_name = request[5:].strip()
        file_path = os.path.join(SERVER_FILES_DIR, file_name)
        if os.path.exists(file_path):
            send_file_to_client(file_path, client_addr)
        else:
            server_socket.sendto("File not found.".encode('utf-8'), client_addr)

    elif request.startswith('BROADCAST '):
        file_name = request[10:].strip()
        file_path = os.path.join(SERVER_FILES_DIR, file_name)
        if os.path.exists(file_path):
            for client in clients:
                send_file_to_client(file_path, client)
        else:
            server_socket.sendto("File not found.".encode('utf-8'), client_addr)

def server_listen():
    """Main server loop to listen for incoming requests."""
    print(f"Server listening on port {PORT}...")
    while True:
        data, client_addr = server_socket.recvfrom(BUFFER_SIZE)
        handle_client_request(data, client_addr)

if __name__ == "__main__":
    if not os.path.exists(SERVER_FILES_DIR):
        os.makedirs(SERVER_FILES_DIR)
    server_listen()