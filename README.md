<img width="1440" alt="Screenshot 2024-08-11 at 12 46 54 PM" src="https://github.com/user-attachments/assets/9e237af3-1aa4-4c5f-b96e-57736e2e5dab"># • UDP File Transfer System
This project is a simple UDP-based file transfer system consisting of a server and a client application. The server can broadcast files to multiple clients, and the client can request files or listen for broadcasted files.
<img width="1440" alt="Screenshot 2024-08-11 at 12 15 15 PM" src="https://github.com/user-attachments/assets/fb022a7b-7359-41be-b137-7ca11af87216">

# • Table of Contents
Project Overview
Requirements
Setup Instructions
Usage
File Format
Acknowledgments
License
# • Project Overview
The UDP File Transfer System allows an administrator to broadcast files to multiple clients over a UDP network. The system consists of two main components:

Server: Listens for file transfer requests from clients, broadcasts files to all connected clients, and provides a list of available files.
Client: Requests files from the server, listens for broadcasted files, and downloads files.
# • Requirements
Python 3.x
Standard Python libraries (socket, os, sys)
Setup Instructions
# • Clone the Repository
sh
Copy code
git clone https://github.com/shuklachitransh/file-transfer.git
cd udp-file-transfer
# • Create Server Files and Client Files
 Place the following Python scripts in the project directory:
server.py: The server application.
client.py: The client application.
Prepare Server Files Directory
<img width="1440" alt="Screenshot 2024-08-11 at 12 46 15 PM" src="https://github.com/user-attachments/assets/72c7e94f-302f-4d3c-979c-6d8728878f48">

# • Create a directory named ServerFiles in the project root. This directory will be used by the server to store and broadcast files.

sh
Copy code
mkdir ServerFiles
Usage
Running the Server
Open a terminal and navigate to the project directory.

# • Run the server script:

sh
Copy code
python server.py
The server will start and listen for client connections on port 10000.

# • Running the Client
Open another terminal and navigate to the project directory.
Run the client script:<br>
sh<br>
Copy code<br>
python client.py<br>
Follow the on-screen commands to interact with the server:<br>
listf: Request a list of files available on the server.<br>
get <filename>: Download a file from the server.<br>
listen: Listen for broadcasted files from the server.<br>
close: Close the client application.<br>

<img width="1440" alt="Screenshot 2024-08-11 at 12 46 54 PM" src="https://github.com/user-attachments/assets/78a1ca07-0762-4ca1-b4c4-53ccb1dc5186">

File Format<br>
Server: server.py<br>
Handles file broadcasting and client connections.<br>
Client: client.py<br>
Allows the user to request files, listen for broadcasts, and interact with the server.<br>
<img width="1440" alt="Screenshot 2024-08-11 at 12 47 16 PM" src="https://github.com/user-attachments/assets/d9017c3a-14e5-4f2c-b424-fc0ac54936be">

# • Acknowledgments
Python documentation and libraries.<br>
# • Network protocols resources<br>
we used User Datagram Protocol<br>
<code>https://www.cloudflare.com/en-in/learning/ddos/glossary/user-datagram-protocol-udp/</code>
