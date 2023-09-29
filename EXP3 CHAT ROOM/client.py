import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class ChatClient:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        self.username = simpledialog.askstring("Username", "Enter your username:")
        self.gui_init()

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def gui_init(self):
        self.root = tk.Tk()
        self.root.title("Chat Client")

        self.chat_history = scrolledtext.ScrolledText(self.root, state='disabled')
        self.chat_history.pack(expand=True, fill='both')

        self.message_entry = tk.Entry(self.root)
        self.message_entry.pack(expand=True, fill='both')
        self.message_entry.bind("<Return>", self.send_message)

    def receive_messages(self):
        while True:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                self.display_message(message)
            except OSError:
                break

    def send_message(self, event):
        message = self.message_entry.get()
        if message:
            self.sock.send(bytes(f"{self.username}: {message}", 'utf-8'))
            self.message_entry.delete(0, 'end')

    def display_message(self, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert('end', message + '\n')
        self.chat_history.configure(state='disabled')
        self.chat_history.yview(tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Change this to the server's IP address or domain name
    PORT = 12345         # Change this to the server's port

    client = ChatClient(HOST, PORT)
    client.run()
