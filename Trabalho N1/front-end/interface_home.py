import tkinter as tk
from tkinter import messagebox
from interface_login import login
from interface_banco import CadastroBanco, MostrarBancos
from banco import Banco



def sair():
    if messagebox.askokcancel("Sair", "Deseja sair do programa?"):
        home.destroy()

def janela_login():
    login.root.mainloop()
    
def cadastrar_banco():
    cadastro = tk.Tk()
    cadastro.title("Cadastro de Banco")
    cadastro = CadastroBanco(cadastro, Banco)
    cadastro.mainloop()


def mostrar_bancos():
    mostrar = tk.Tk()
    mostrar.title("Lista de Bancos")
    mostrar = MostrarBancos(mostrar, Banco)
    mostrar.mainloop()


# def atualizar_banco():
#     root_atualizar = tk.Tk()
#     root_atualizar.title("Atualizar Banco")
#     atualizar = AtualizarBanco(root_atualizar, Banco.listar_bancos())  # Passa a lista de bancos
#     root_atualizar.mainloop()




#  janela principal
home = tk.Tk()
home.title("Sistema Bancário")

#  barra de menus
menu_bar = tk.Menu(home)
home.config(menu=menu_bar)


# === Banco ===
menu_banco = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Banco", menu=menu_banco)
menu_banco.add_command(label="Novo Banco", command=cadastrar_banco)
menu_banco.add_command(label="Mostrar Banco", command=mostrar_bancos )
# menu_banco.add_command(label="Atualizar Banco",command= atualizar_banco )


# === Conta ===
menu_conta = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Conta", menu=menu_conta)
menu_conta.add_command(label="Nova Conta Poupança")
menu_conta.add_command(label="Encerrar Conta Poupança")
menu_conta.add_separator()
menu_conta.add_command(label="Nova Conta Corrente")
menu_conta.add_command(label="Encerrar Conta Corrente")

# === Operações ===
menu_operacoes = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Operações", menu=menu_operacoes)
menu_operacoes.add_command(label="Depósito")
menu_operacoes.add_command(label="Saque")
menu_operacoes.add_separator()
menu_operacoes.add_command(label="Transferência")

# === Sair ===
menu_sair = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Sair", menu=menu_sair)
menu_sair.add_command(label="Sair", command=sair)

# primeiro chama a janela de login
home.after(0, janela_login)
home.mainloop()