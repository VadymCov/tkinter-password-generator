import tkinter as tk
from tkinter import ttk
import secrets

class PasswordGeneration:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('password generation')
        self.window_in_the_center()
        self.create_entry()
        self.create_button()
        self.root.mainloop()

        
    def window_in_the_center(self):
        """Centers the windows on the screen with dimensions (n x n)pixels."""
        width = 300
        height = 100
        x = (self.root.winfo_screenwidth() // 2 ) - (width // 2)
        y = (self.root.winfo_screenheight() // 2 ) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_button(self):
        btn = ttk.Button(self.root, text='generate', command=self.entry_get )
        btn.pack(padx=10, pady=(5,5))

    def create_entry(self):
        self.entry_pass =  ttk.Entry(self.root,)
        self.entry_pass.pack(pady=5)

    def entry_get(self):
        self.password = secrets.token_urlsafe(10)
        self.entry_pass.delete(0, tk.END)
        self.entry_pass.insert(0, self.password)

PasswordGeneration()