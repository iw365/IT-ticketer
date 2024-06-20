import tkinter as tk
import customtkinter as ctk
import os
import threading
import subprocess

class main_frame(ctk.CTkFrame):
    def __init__(self, parent, width, height):
        self.width = width
        self.height = height        
        super().__init__(parent)
        
        self.initialise_ui()
        
    def initialise_ui(self):
        
        self.button = ctk.CTkButton(self, text="START SERVER", command=self.button_callback)
        self.button.pack(padx=10, pady=20, expand=False)
        
        self.terminate_button = ctk.CTkButton(self, text="STOP SERVER", command=self.stop_server)
        self.terminate_button.pack(padx=10, pady=(0,20), expand=False)
        
        self.button2 = ctk.CTkButton(self, text="START CLIENT", command=self.button2_callback)
        self.button2.pack(padx=10, pady=(0,20), expand=False)
        
    def button_callback(self):
        
        def run_server():
            self.server_process = subprocess.Popen(["python", "server.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

        server_thread = threading.Thread(target=run_server)
        server_thread.start()
        
    def stop_server(self):
        if self.server_process is not None:
            self.server_process.terminate()
    
    def button2_callback(self):
        
        def run_client():
            os.system("python client.py")
        
        client_thread = threading.Thread(target=run_client)
        client_thread.start()

class sub_frame(ctk.CTkFrame):
    def __init__(self, parent, width, height):
        self.width = width
        self.height = height        
        super().__init__(parent)
        
        self.initialise_ui()
        
    def initialise_ui(self):
        
        self.button = ctk.CTkButton(self, text="START CLIENT", command=self.button_callback)
        self.button.pack(padx=10, pady=10, expand=False)
        
        self.button2 = ctk.CTkButton(self, text="START CLIENT", command=self.button_callback)
        self.button2.pack(padx=10, pady=(0,10), expand=False)
        
    def button_callback(self):
        
        def run_client():
            os.system("python client.py")
        
        client_thread = threading.Thread(target=run_client)
        client_thread.start()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.width = 400
        self.height = 600

        self.title("HOST")
        self.geometry(f"{self.width}x{self.height}")
        self.minsize(300, 200)
        self.grid_propagate(False)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.grid_rowconfigure(1, weight=1)
        
        self.initialise_ui()

    def initialise_ui(self):
        
        # self.message = ctk.CTkEntry(self, placeholder_text="Enter message")
        # self.message.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")
        
        self.main_frame = main_frame(parent=self, width = self.width, height = self.height)
        self.main_frame.grid(row=0, column=0, padx=50, pady=(50, 0), sticky="nesw")
        
        self.sub_frame = sub_frame(parent=self, width = self.width, height = self.height)
        self.sub_frame.grid(row=1, column=0, padx=50, pady=(10, 50), sticky="nesw")

app = App()
app.mainloop()