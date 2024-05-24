import socket

class Host:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.host, self.port))

    def receive_messages(self):
        
        while True:
            try:
                message = self.server.recv(1024).decode('utf-8')
                print(message)
            except:
                print("Error: Unable to receive messages")
                self.server.close()
                break
        
        # IDK if this will work, the self.after will only work if i add UI, but i am not sure if this means it will only check
        # if there is a message exactly when the after is called, or if it will recieve all messages and only show them when after is called
        # may need to implement a queue/backlog system, and then grab the messages from the queue each time after is called
        
        # self.after(2000, self.receive_messages)
        # print("Checking...")
        # try:
        #     message = self.server.recv(1024).decode('utf-8')
        #     print(message)
            
        # except:
        #     print("Error: Unable to receive messages")
        #     self.server.close()
            


host = Host()
host.receive_messages()