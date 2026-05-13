import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class book:
    def __init__(self, title):
        self.title = title
        self.borrower = None
        self.info = []

class borrower:
    def __init__(self, username, password, admin):
        self.username = username
        self.password = password
        self.books = {}
        self.admin = admin

    def returnBook(self, book):
        removedBook = self.books.pop(book)
        return removedBook[0]
    
    def borrowBook(self, newBook=book):
        currentTime = datetime.now()
        currentTime = currentTime.replace(microsecond=0)
        self.books[newBook.title] = [newBook, currentTime]


class libraryApp:
    def __init__(self, root=tk):
        self.root = root
        self.accounts = {}
        self.root.title("www.onlinelibrary.co.nz")
        self.root.minsize(500, 800)
        self.root.geometry("500x800+500+0")

        self.accounts["admin"] = borrower("admin", "I<3Books", True)
    
    def create_frames(self):
        self.login_frame = ttk.Frame(self.root, padding=10)
        self.main_frame = ttk.Frame(self.root)
        self.nav_frame = ttk.Frame(self.main_frame, padding=10)
    