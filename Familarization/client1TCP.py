import socket

HOST = '127.0.0.1'  # Server IP (localhost)
PORT = 12345        # Server port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname(socket.gethostname()),socket.gethostname())
client_socket.connect((HOST, PORT))

message = "Hello, server!"
client_socket.sendall(message.encode())   # Send data to the server

data = client_socket.recv(1024).decode()  # Receive data from the server
print("Received:", data)

client_socket.close()
