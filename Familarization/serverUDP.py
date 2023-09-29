import socket

# Define the server's IP address and port
SERVER_HOST = '0.0.0.0'  # Listen on all available interfaces
SERVER_PORT = 12345

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print("Server is listening on", SERVER_HOST, "port", SERVER_PORT)

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)
    print("Received from:", client_address, "Message:", data.decode())

    # Send a response back to the client
    response = "Server received your message: " + data.decode()
    server_socket.sendto(response.encode(), client_address)
