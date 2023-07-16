import tkinter as tk
from tkinter import messagebox
from component_banco import CadastroBanco, MostrarBancos
from banco import Banco

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class Home:
    
    def __init__(self, root):

        self.root = root
        # Configuração da janela principal
        self.root.title("Sistema Bancário")
        self.root.geometry("500x300")

        #  barra de menus
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)


        # === Banco ===
        menu_banco = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Banco", menu=menu_banco)
        menu_banco.add_command(label="Cadastrar Banco", command=self.cadastrar_banco)
        menu_banco.add_command(label="Mostrar Bancos", command=self.mostrar_bancos)
        # menu_banco.add_command(label="Atualizar Banco",command= atualizar_banco )


        # === Conta ===
        menu_conta = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Conta", menu=menu_conta)
        menu_conta.add_command(label="Criar Conta")
        menu_conta.add_separator()
        menu_conta.add_command(label="Mostrar Contas Corrente")
        menu_conta.add_command(label="Mostrar Contas Poupança")

        # === Cliente ===
        menu_cliente = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Cliente", menu=menu_cliente)
        menu_cliente.add_command(label="Cadastrar Cliente")
        menu_cliente.add_command(label="Mostrar Clientes")

        # === Operações ===
        menu_operacoes = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Operações", menu=menu_operacoes)
        menu_operacoes.add_command(label="Transferência")
        menu_operacoes.add_separator()
        menu_operacoes.add_command(label="Depósito")
        menu_operacoes.add_command(label="Saque")
        

        # === Sair ===
        menu_bar.add_command(label="Sair", command=self.sair)

        self.frame = tk.Frame(self.root)
        self.frame.pack()


    def sair(self):
        if messagebox.askokcancel("Sair", "Deseja sair do programa?"):
            self.root.destroy()
        
    def cadastrar_banco(self):
        limpar_tela(self.frame)
        self.root.title("Cadastrar Bancos")
        cadastro = CadastroBanco(self.frame)

    def mostrar_bancos(self):
        limpar_tela(self.frame)
        self.root.title("Mostrar Bancos")
        mostrar = MostrarBancos(self.frame, Banco)
