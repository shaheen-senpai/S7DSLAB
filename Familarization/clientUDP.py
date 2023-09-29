import socket

# Define the server's IP address and port
SERVER_IP = '127.0.0.1'  # Replace with the server's IP address
SERVER_PORT = 12345

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
message = "Hello, server!"
client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
print("Sent:", message)

# Receive the response from the server
response, server_address = client_socket.recvfrom(1024)
print("Received from server at", server_address, ":", response.decode())

# Close the socket
client_socket.close()
