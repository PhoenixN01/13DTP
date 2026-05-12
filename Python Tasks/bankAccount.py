import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class bankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transacLog = []
    
    def deposit(self, amount):
        self.balance += amount
        self.updateLog(f"+ ${amount}", "deposit")

    def withdraw(self, amount):
        self.balance -= amount
        self.updateLog(f"- ${amount}", "withdraw")

    def updateLog(self, transacAmount, transacType):
        logTime = datetime.now()
        logTime = logTime.replace(microsecond=0)
        self.transacLog.insert(0, [logTime, self.name, transacAmount, transacType])

class bankGUI:
    def __init__(self, root):
        self.root = root
        self.account = None
        self.root.title("Big Bank")
        self.root.minsize(500, 800)
        self.root.geometry("500x800+500+0")
        self.root.configure(bg="blanchedalmond")

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

        ttk.Label(self.bankLog_frame, text="Transaction History:").pack()

        log_container = ttk.Frame(self.bankLog_frame)
        log_container.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(log_container, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.recentLog = ttk.Treeview(
            log_container,
            columns=("Date and Time", "Account Name", "Amount", "Type"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=15
        )

        self.recentLog.tag_configure("deposit", foreground="green")
        self.recentLog.tag_configure("withdraw", foreground="red")

        scrollbar.config(command=self.recentLog.yview)

        self.recentLog.heading("Date and Time", text="Date and Time")
        self.recentLog.heading("Account Name", text="Account Name")
        self.recentLog.heading("Amount", text="Amount")
        self.recentLog.heading("Type", text="Type")

        # Column sizes
        self.recentLog.column("Date and Time", width=170)
        self.recentLog.column("Account Name", width=100)
        self.recentLog.column("Amount", width=80)
        self.recentLog.column("Type", width=80)

        self.recentLog.pack(side="left", fill="both", expand=True)

    def create_account(self):
        name = self.name_entry.get().strip()

        if name == "":
            messagebox.showerror("Account Error", "You must provide an account name to create an account")
            return
        
        if messagebox.askokcancel("Confirm Account", f"Are you sure you would like to create the bank account: {name}"):
            messagebox.showinfo("Welcome!", f"Welcome to Big Bank {name}!")
            self.account = bankAccount(name)
            self.name_label.config(text=f"Account: {name}")
            self.balance_label.config(text=f"Balance: ${self.account.balance}")
        
        return
    
    def validate_funds(self, input):
        try:
            return int(input)
        except ValueError or TypeError:
            messagebox.showerror("Incorrect Input", f"{input} is invalid. \n \nInput must be a positive integer to continue")
            return False
        
    def process_funds(self, request=""):
        if request == "" or self.account is None:
            return
        value = self.change_amount.get().strip()

        valid_change = self.validate_funds(value)

        if valid_change is False:
            return

        if valid_change < 0:
            messagebox.showerror("Invalid Input", f"{value} is invalid. \n \nInput must be a positive integer")
            return
        elif valid_change > 5000:
            messagebox.showerror(f"Maximum {request.capitalize()}", f"{request.capitalize()}s can only be a maximum of $5000 per transaction")
            return
        
        if request == "withdraw":
            if valid_change > self.account.balance:
                messagebox.showerror(
                    "Insufficient Funds",
                    f"Please input a valid withdrawal amount. \n \nMaximum withdrawal is ${self.account.balance}"
                )
                return

            self.account.withdraw(valid_change)

        else:
            self.account.deposit(valid_change)

        self.update_display()
        self.update_recentLog()
        self.fundsWind.destroy()

    def funds_window(self, request=""):
        if request == "" or self.account is None:
            messagebox.showerror("No Account Found", "Please create an account to continue")
            return
        
        self.fundsWind = tk.Toplevel(self.root)
        self.fundsWind.title(f"{request.capitalize()} Funds")
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
        ).grid(row=1, column=0)
                
        return
    
    def update_display(self):
        if self.account is None:
            self.name_label.config(text="Account: -")
            self.balance_label.config(text="Balance: -")
        else:
            self.balance_label.config(text=f"Balance: ${self.account.balance}")
        return

    def update_recentLog(self):
        if self.account is None or self.account.transacLog == []:
            return

        for item in self.recentLog.get_children():
            self.recentLog.delete(item)

        for log in self.account.transacLog[:10]:

            trans_type = str(log[3])

            self.recentLog.insert(
                "",
                "end",
                values=(
                    log[0],
                    log[1],
                    log[2],
                    trans_type.capitalize()
                ),
                tags=(trans_type,)
            )
        
root = tk.Tk()
root.option_add('*background', 'blanchedalmond')
style = ttk.Style()
style.theme_use('clam')
style.configure('.', background="antiquewhite1")
style.configure("TFrame", background="blanchedalmond")
gui = bankGUI(root)
root.mainloop()