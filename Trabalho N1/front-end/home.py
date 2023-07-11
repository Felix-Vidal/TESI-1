import tkinter as tk
from tkinter import messagebox
import login

# Função para abrir uma nova janela
def abrir_janela(titulo_janela):
    messagebox.showinfo("Nova Janela", f"Abrindo {titulo_janela}")


# Função para exibir uma mensagem quando uma opção do menu é selecionada
# def menu_cb(menu_item):
#     messagebox.showinfo("Menu", f"Selecionado: {menu_item}")



def sair():
    if messagebox.askokcancel("Sair", "Deseja sair do programa?"):
        home.destroy()

def janela_login():
    login.root.mainloop()

#  janela principal
home = tk.Tk()
home.title("Sistema Bancário")

#  barra de menus
menu_bar = tk.Menu(home)
home.config(menu=menu_bar)

# === Arquivo ===
menu_arquivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Nova Conta", command=lambda: abrir_janela("Nova Conta"))
menu_arquivo.add_command(label="Encerrar Conta", command=lambda: abrir_janela("Encerrar Conta"))
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)

# === Operações ===
menu_operacoes = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Operações", menu=menu_operacoes)
menu_operacoes.add_command(label="Depósito", command=lambda: abrir_janela("Depósito"))
menu_operacoes.add_command(label="Saque", command=lambda: abrir_janela("Saque"))
menu_operacoes.add_separator()
menu_operacoes.add_command(label="Transferência", command=lambda: abrir_janela("Transferência"))

# === Ajuda ===
# help_menu = tk.Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Ajuda", menu=help_menu)
# help_menu.add_command(label="Sobre", command=lambda: menu_cb("Sobre"))

# primeiro chama a janela de login
home.after(0, janela_login)
home.mainloop()