import socket

class Client:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send_message(self, message):
        self.client.send(message.encode('utf-8'))

client = Client()
while True:
    message = input('Enter message: ')
    client.send_message(message)