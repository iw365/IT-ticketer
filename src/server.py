import socket
import threading

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
            c.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.messages.append((client, message))
                self.broadcast(message, client)
            except:
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