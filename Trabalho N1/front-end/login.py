import tkinter as tk
from tkinter import messagebox
from home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class Login:
    def __init__(self, root):
        self.root = root

        self.root.title("Login")
        self.root.geometry("600x300")

        self.label_username = tk.Label(self.root, text="Username:")
        self.label_username.pack()

        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()
        self.entry_username.focus()

        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack()

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self.root, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Simulando um processo de autenticação simples
        if username == "admin" and password == "admin":
            self.open_home()
        else:
            messagebox.showerror("Login", "Credenciais inválidas.")

    def open_home(self):
        limpar_tela(self.root)
        TelaPricipal = Home(self.root)

root = tk.Tk()
TelaPricipal = Login(root)
root.mainloop()