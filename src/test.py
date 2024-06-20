import socket

import tkinter as tk
import customtkinter as ctk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("test")
        self.geometry("500x350")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.initialise_ui()
    
    def initialise_ui(self):
        
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.t = np.arange(0, 3, .01)
        self.fig.add_subplot(111).plot(self.t, 2 * np.sin(2 * np.pi * self.t))

        canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

app = App()
app.mainloop()

#  old host.py stuff #

import socket

# gonna rewrite all of this so that it just accesses all of the data from the server fil

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