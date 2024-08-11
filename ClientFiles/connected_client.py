import socket as sk
from socket import *
import os
import sys
import time

# Variables used for UDP transfer
host = sk.gethostbyname(sk.gethostname())  # Server IP
serverPort = 10000  # Server bind port
buffer = 1024  # Buffer size of client

# Create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

def requestList():
    '''Sends a request to the server for the list of files and displays it'''
    clientSocket.sendto("LIST".encode("utf-8"), (host, serverPort))
    data, _ = clientSocket.recvfrom(buffer)
    print("\nAvailable files:\n", data.decode("utf-8"))

def requestFile(fileName):
    '''Requests a file from the server and downloads it'''
    clientSocket.sendto(f"FILE {fileName}".encode("utf-8"), (host, serverPort))
    receive_file(fileName)

def receive_file(fileName):
    '''Receives a file and writes it to disk'''
    with open(fileName, "wb") as file:
        while True:
            data, _ = clientSocket.recvfrom(buffer)
            if not data:
                break
            file.write(data)
    print("File downloaded:", fileName)

def listen_for_broadcast():
    '''Listens for broadcasted files from the server (admin)'''
    print("Listening for broadcasted files...")
    while True:
        data, addr = clientSocket.recvfrom(buffer)
        print(f"Received data from {addr}: {data[:50]}...")  # Debugging print
        if data.startswith(b'FILE '):
            fileName = data.decode("utf-8").split(" ", 1)[1].strip()
            print(f"Receiving broadcasted file: {fileName}")
            receive_file(fileName)
        else:
            print(f"Unexpected data received: {data.decode('utf-8')}")

def options():
    '''Gives user option to do file transfer.'''
    while True:
        print("\n========================== ENTER COMMAND ==========================")
        print("\t 'listf' to see the list of files available on server\n",
              "\t 'get <filename>' to download a file\n",
              "\t 'listen' to listen for broadcasted files\n",
              "\t 'close' to close the application\n")
        command = input("Udp > ").strip()
        
        if command == "listf":
            requestList()
        elif command.startswith("get "):
            fileName = command.split(" ", 1)[1]
            requestFile(fileName)
        elif command == "listen":
            listen_for_broadcast()
        elif command == "close":
            closeApp()
        else:
            print("Udp > Command Error")
            continue

def closeApp():
    '''Close this application'''
    clientSocket.close()  # Closing socket
    print("Udp is going to close...")
    print("System exiting...")
    sys.exit()  # Exiting from the system

if __name__ == "__main__":
    options()