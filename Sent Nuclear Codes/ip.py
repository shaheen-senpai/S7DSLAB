import socket

HOST = '172.18.120.128'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server listening on", HOST, "port", PORT)

client_socket, client_address = server_socket.accept()
print("Connection from:", client_address)

message = "Hello, NIGGA!"
client_socket.sendall(message.encode())

while True:
    
    received_message = client_socket.recv(1024).decode()
    print("Received:", received_message)

    if received_message.lower() == "bye":
        response = "Goodbye!"
        client_socket.sendall(response.encode())
        break

    user_input = input("Enter your response: ")
    client_socket.sendall(user_input.encode())

client_socket.close()
server_socket.close()
