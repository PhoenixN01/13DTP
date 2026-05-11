import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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
        self.root.title("Big Bank")
        self.root.minsize(500, 800)
        self.root.geometry("500x800+500+0")

        self.create_frames()

        self.input_frame.pack()
        self.bankDetails_frame.pack()
        self.bankActions_frame.pack()
        self.bankLog_frame.pack()

        self.create_widgets()

    def create_frames(self):
        self.input_frame = ttk.Frame(self.root, padding=10)
        self.bankDetails_frame = ttk.Frame(self.root, padding=10)
        self.bankActions_frame = ttk.Frame(self.root, padding=10)
        self.bankLog_frame = ttk.Frame(self.root, padding=10)
    
    def create_widgets(self):
        ttk.Label(self.input_frame, text="Account Name: ").grid(row=0, column=0)
        self.name_entry = ttk.Entry(self.input_frame)
        self.name_entry.grid(row=1, column=0)

        ttk.Button(self.input_frame, text="Create Account", command=self.create_account).grid(row=1, column=1)


        self.name_label = ttk.Label(self.bankDetails_frame, text="Account: -")
        self.name_label.pack()

        self.balance_label = ttk.Label(self.bankDetails_frame, text="Balance: -")
        self.balance_label.pack()

        ttk.Button(self.bankActions_frame, text="Deposit", command=lambda: self.funds_window("deposit")).grid(row=0, column=0)
        ttk.Button(self.bankActions_frame, text="Withdraw", command=lambda: self.funds_window("withdraw")).grid(row=0, column=1)

    def create_account(self):
        name = self.name_entry.get().strip()

        if name == "":
            messagebox.showerror("Account Error", "You must provide an account name to create an account")
            return
        
        if messagebox.askokcancel("Confirm Account", f"Are you sure you would like to create the bank account: {name}"):
            self.account = bankAccount(name)
        
        return
    
    def validate_funds(self, input):
        try:
            return int(input)
        except ValueError or TypeError:
            messagebox.showerror("Incorrect Input", f"{input} is invalid. \n \n Input must be an integer to continue")
            return False
        
    def process_funds(self, request):
        if request is None or self.account is None:
            return
        value = self.change_amount.get().strip()

        valid_change = self.validate_funds(value)

        if valid_change is False:
            return

        if request == "withdraw":
            if valid_change > self.account.balance:
                messagebox.showerror(
                    "Insufficient Funds",
                    f"Maximum withdrawal is ${self.account.balance}"
                )
                return

            self.account.withdraw(valid_change)

        else:
            self.account.deposit(valid_change)

        self.fundsWind.destroy()

    def funds_window(self, request):
        if request is None or self.account is None:
            return
        
        self.fundsWind = tk.Toplevel(self.root)
        self.fundsWind.title(f"{request} Funds")
        funds_infoFrame = ttk.Frame(self.fundsWind, padding=10)
        funds_infoFrame.grid(row=0, column=0)
        funds_inputFrame = ttk.Frame(self.fundsWind, padding=10)
        funds_inputFrame.grid(row=1, column=0)
        self.fundsWind.geometry("500x800")

        ttk.Label(funds_infoFrame, text=f"Current Balance: ${self.account.balance}").grid(row=0, column=0)
        ttk.Label(funds_infoFrame, text=f"How much would you like to {request}:").grid(row=2, column=0)
        
        self.change_amount = ttk.Entry(funds_inputFrame)
        self.change_amount.grid(row=0, column=0)
        ttk.Button(
            funds_inputFrame,
            text="Confirm",
            command=lambda: self.process_funds(request)
        ).grid(row=1, column=1)
                
        return
    
    def update_display(self):
        return

root = tk.Tk()
style = ttk.Style()
style.configure("TFrame", background="blanchedalmond")
style.configure("TLabel", background="blanchedalmond")
gui = bankGUI(root)
root.mainloop()