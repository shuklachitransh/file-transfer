import socket
import os

# Configuration
SERVER_IP = '127.0.0.1'  # IP of the server (localhost for testing)
PORT = 10000  # Same port as the server
BUFFER_SIZE = 1024  # Buffer size for sending data
SERVER_FILES_DIR = 'ServerFiles/'  # Directory where files are stored

def send_file(file_name):
    """Send the selected file to the server for broadcasting."""
    file_path = os.path.join(SERVER_FILES_DIR, file_name)
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as admin_socket:
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                admin_socket.sendto(data, (SERVER_IP, PORT))

if __name__ == "__main__":
    file_name = input("Enter the name of the file to broadcast: ")
    send_file(file_name)
    print(f"Broadcasting {file_name} to all clients.")