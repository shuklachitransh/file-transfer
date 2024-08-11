# UDP File Transfer System
This project is a simple UDP-based file transfer system consisting of a server and a client application. The server can broadcast files to multiple clients, and the client can request files or listen for broadcasted files.

# Table of Contents
Project Overview
Requirements
Setup Instructions
Usage
File Format
Acknowledgments
License
# Project Overview
The UDP File Transfer System allows an administrator to broadcast files to multiple clients over a UDP network. The system consists of two main components:

Server: Listens for file transfer requests from clients, broadcasts files to all connected clients, and provides a list of available files.
Client: Requests files from the server, listens for broadcasted files, and downloads files.
# Requirements
Python 3.x
Standard Python libraries (socket, os, sys)
Setup Instructions
# Clone the Repository
sh
Copy code
git clone https://github.com/shuklachitransh/file-transfer.git
cd udp-file-transfer
# Create Server Files and Client Files

Place the following Python scripts in the project directory:

server.py: The server application.
client.py: The client application.
Prepare Server Files Directory

# Create a directory named ServerFiles in the project root. This directory will be used by the server to store and broadcast files.

sh
Copy code
mkdir ServerFiles
Usage
Running the Server
Open a terminal and navigate to the project directory.

# Run the server script:

sh
Copy code
python server.py
The server will start and listen for client connections on port 10000.

# Running the Client
Open another terminal and navigate to the project directory.

Run the client script:
sh
Copy code
python client.py
Follow the on-screen commands to interact with the server:

listf: Request a list of files available on the server.
get <filename>: Download a file from the server.
listen: Listen for broadcasted files from the server.
close: Close the client application.
File Format
Server: server.py
Handles file broadcasting and client connections.
Client: client.py
Allows the user to request files, listen for broadcasts, and interact with the server.
Acknowledgments
Python documentation and libraries.
Network programming resources and examples.
