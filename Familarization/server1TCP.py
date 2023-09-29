import socket

HOST = '127.0.0.1'  # Server IP (localhost)
PORT = 12345        # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket()
server_socket.bind((HOST, PORT))
server_socket.listen() # -> Listen()

print("Server listening on", HOST, "port", PORT)

client_socket, client_address = server_socket.accept()  # -> Accept() 
print("Connection from:", client_address)

data = client_socket.recv(1024).decode()  # Receive data from the client -> Read() command
print("Received:", data)

message = "Hello, client!"
client_socket.sendall(message.encode())   # Send data to the client -> Write() command

client_socket.close()
server_socket.close() # Close() command
