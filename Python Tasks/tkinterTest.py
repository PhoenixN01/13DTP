import tkinter as tk

root = tk.Tk()

root.title("Test Window")
root.configure(background="white")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("400x420+300+100")

tk.Label(root, text="Tkinter is better than easygui")