import tkinter as tk
from tkinter import messagebox
from component_operacoes import SaqueHome, DepositoHome, TransferenciaFrame
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from component_banco import CadastroBanco, MostrarBancos
from banco import Banco
from component_conta import CadastroConta, MostrarContas
from component_cliente import CadastroCliente, MostrarClientes

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class Home:
    
    def __init__(self, root):

        self.root = root
        # Configuração da janela principal
        self.root.title("Sistema Bancário")
        self.root.configure(bg="#edebeb")

        #  barra de menus
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)


        # === Banco ===
        menu_banco = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Banco", menu=menu_banco)
        menu_banco.add_command(label="Cadastrar Banco", command=self.cadastrar_banco)
        menu_banco.add_command(label="Mostrar Bancos", command=self.mostrar_bancos)


        # === Conta ===
        menu_conta = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Conta", menu=menu_conta)
        menu_conta.add_command(label="Criar Conta", command=self.cadastrar_conta)
        menu_conta.add_separator()
        menu_conta.add_command(label="Mostrar Contas Corrente", command=lambda: self.mostrar_contas("Corrente"))
        menu_conta.add_command(label="Mostrar Contas Poupança", command=lambda: self.mostrar_contas("Poupança"))

        # === Cliente ===
        menu_cliente = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Cliente", menu=menu_cliente)
        menu_cliente.add_command(label="Cadastrar Cliente", command=self.cadastrar_cliente)
        menu_cliente.add_command(label="Mostrar Clientes", command=self.mostrar_clientes)

        # === Operações ===
        menu_operacoes = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Operações", menu=menu_operacoes)
        menu_operacoes.add_command(label="Transferência", command=self.operacao_transferencia)
        menu_operacoes.add_separator()
        menu_operacoes.add_command(label="Saque", command=self.operacao_saque)
        menu_operacoes.add_command(label="Depósito", command=self.operacao_deposito)
        

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
        
    def cadastrar_conta(self):
        limpar_tela(self.frame)
        self.root.title("Cadastrar Conta")
        cadastro = CadastroConta(self.frame)
        
    def mostrar_contas(self, tipo_conta):
        limpar_tela(self.frame)
        self.root.title(f"Mostrar Contas {tipo_conta}")
        mostrar = MostrarContas(self.frame, tipo_conta)
        
    def cadastrar_cliente(self):
        limpar_tela(self.frame)
        self.root.title("Cadastrar Cliente")
        cadastro = CadastroCliente(self.frame)

    def mostrar_clientes(self):
        limpar_tela(self.frame)
        self.root.title("Mostrar Clientes")
        mostrar = MostrarClientes(self.frame)
        
    def operacao_saque(self):
        limpar_tela(self.frame)
        self.root.title("Saque")
        saque_home = SaqueHome(self.frame)
        saque_home.pack()

    def operacao_deposito(self):
        limpar_tela(self.frame)
        self.root.title("Depósito")
        deposito_home = DepositoHome(self.frame)
        deposito_home.pack()
        
    def operacao_transferencia(self):
        limpar_tela(self.frame)
        self.root.title("Realizar Transferência")
        transferencia_frame = TransferenciaFrame(self.frame)
        
        
        
    