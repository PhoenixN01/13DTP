import tkinter as tk
from tkinter import messagebox

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

        tk.Button(self.input_frame, text="Create Account", command=self.create_account())

        self.name_label = tk.Label(self.bankDetails_frame, text="Account: -")
        self.name_label.pack()

        self.balance_label = tk.Label(self.bankDetails_frame, text="Balance: -")
        self.balance_label.pack()

        tk.Button(self.bankActions_frame, text="Deposit", command=self.account_deposit).grid(row=0, column=0)
        tk.Button(self.bankActions_frame, text="Withdraw").grid(row=0, column=1)
    
    def create_account(self):
        name = self.name_entry.get().strip()

        if name == "":
            messagebox.showerror("Account Error", "You must provide an account name to create an account")
            return
        
        if messagebox.askokcancel("Confirm Account", f"Are you sure you would like to create the bank account: {name}"):
            self.account = bankAccount(name)
        
        return
    
    def funds_window(self, request):
        if request is None:
            return
        
        fundsWind = tk.Toplevel(self.root)
        fundsWind.title(f"{request} Funds")
        funds_infoFrame = tk.Frame(fundsWind, padx=10, pady=10)
        funds_inputFrame = tk.Frame(fundsWind, padx=10, pady=10)
        fundsWind.geometry("500x800")

        tk.Label(funds_infoFrame, text=f"Current Balance: ${self.account.balance}")
        tk.Label(funds_infoFrame, text=f"How much would you like to {request}")
        
        
        return

    def account_deposit(self):
        return