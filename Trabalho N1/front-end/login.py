import tkinter as tk
from tkinter import messagebox

def login():
    user = ent_user.get()
    senha = ent_senha.get()

    if user == "admin" and senha == "123":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        root.destroy()  # Fecha a janela de login
    else:
        messagebox.showerror("Login", "Credenciais inválidas!")

root = tk.Tk()
root.title("Login")


lbl_user = tk.Label(root, text="Usuário:")
lbl_user.pack()
ent_user = tk.Entry(root)
ent_user.pack()

lbl_senha = tk.Label(root, text="Senha:")
lbl_senha.pack()
ent_senha = tk.Entry(root, show="*")
ent_senha.pack()

# Botão de login
btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack()

root.mainloop()
