import socket
import threading
from datetime import datetime

class Server:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.messages = []

    def broadcast(self, message, client):
        for c in self.clients:
            if c != client:  # Don't send the message back to the sender
                c.send(message.encode('utf-8'))

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                if not message:
                    break
                message = message.decode('utf-8')
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] Received: {message}")
                self.messages.append((client, message))
                #self.broadcast(message, client)
            except Exception as e:
                print(f"An error occurred with client {client}: {e}")
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                break

    def start(self):
        while True:
            client, address = self.server.accept()
            self.clients.append(client)
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

server = Server()
server.start()