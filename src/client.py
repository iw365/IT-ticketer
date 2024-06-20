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

class Client:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send_message(self, message):
        self.client.send(message.encode('utf-8'))

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class MyRadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CLIENT")
        self.geometry("500x400")
        self.minsize(300, 200)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.client = Client()
        
        self.initialise_ui()

    def initialise_ui(self):
        
        self.checkbox_frame = MyCheckboxFrame(self, "Values", values=["value 1", "value 2", "value 3"])
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options", values=["High Priority", "Low Priority"])
        self.radiobutton_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")
        
        self.message = ctk.CTkEntry(self, placeholder_text="Enter message")
        self.message.grid(row=1, column=0, padx=10, pady=(10,0), sticky="ew", columnspan=2)

        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=(10,10), sticky="ew", columnspan=2)

    def button_callback(self):
        #print("checkbox_frame:", self.checkbox_frame.get())
        #print("radiobutton_frame:", self.radiobutton_frame.get())
        message = self.message.get()
        
        #print("message:", message)
        self.client.send_message(message)

app = App()
app.mainloop()