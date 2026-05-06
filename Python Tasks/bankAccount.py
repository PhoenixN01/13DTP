import tkinter as tk

class bankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class bankGUI:
    def __init__(self, root):
        self.root = root
        self.account = None
        self.root.title = ("Big Bank")
        self.root.minsize(500, 800)
        self.root.geometry("500x800+500+500")

    def create_frames(self):
        self.input_frame = tk.Frame(self.root, width="")
        