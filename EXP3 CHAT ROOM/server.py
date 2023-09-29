import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def accept_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"Connection from {addr}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.broadcast_message(message, client_socket)
            except OSError:
                break

    def broadcast_message(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(bytes(message, 'utf-8'))
                except socket.error:
                    self.remove_client(client)

    def remove_client(self, client_socket):
        if client_socket in self.clients:
            self.clients.remove(client_socket)
            client_socket.close()

    def run(self):
        print(f"Server listening on {self.host}:{self.port}")
        accept_thread = threading.Thread(target=self.accept_clients)
        accept_thread.start()
        accept_thread.join()


if __name__ == "__main__":
    HOST = "172.18.120.128"  # Change this to the server's IP address or domain name
    PORT = 1234         # Change this to the server's port

    server = ChatServer(HOST, PORT)
    server.run()
