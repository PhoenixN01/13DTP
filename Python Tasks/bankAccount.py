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
        self.root.configure(bg="blanchedalmond")

    def create_frames(self):
        self.input_frame = tk.Frame(self.root, padx=10, pady=10)
        self.bankDetails_frame = tk.Frame(self.root, padx=10, pady=10)
        self.bankActions_frame = tk.Frame(self.root, padx=10, pady=10)
        self.bankLog_frame = tk.Frame(self.root, padx=10, pady=10)
    
    def create_widgets(self):
        tk.Label(self.input_frame, text="Account Name: ").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=1, column=0)

        tk.Button()
        