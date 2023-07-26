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
        self.root.configure(bg="#edebeb")
        self.root.geometry("700x350")
        
        # Calculate screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 700
        window_height = 350

        # Calculate x and y coordinates to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"700x350+{x}+{y}")

        

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
        self.button_login.pack(pady=5)

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