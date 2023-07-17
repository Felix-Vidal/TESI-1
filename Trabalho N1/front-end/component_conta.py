import tkinter as tk
from tkinter import messagebox, ttk
from conta import Conta
from banco import Banco
from cliente import Cliente
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

class CadastroConta:

    def __init__(self, frame):
        self.root = frame
        
        self.label_banco = tk.Label(self.root, text="Banco:")
        self.label_banco.pack()
        lista_bancos = Banco.listar_bancos()
        self.combobox_banco = ttk.Combobox(self.root, values=lista_bancos)
        self.combobox_banco.pack()

        self.label_titular = tk.Label(self.root, text="Titular:")
        self.label_titular.pack()
        lista_clientes = Cliente.listar_clientes()
        self.combobox_titular = ttk.Combobox(self.root, values=lista_clientes)
        self.combobox_titular.pack()

        self.label_saldo = tk.Label(self.root, text="Saldo:")
        self.label_saldo.pack()
        self.entry_saldo = tk.Entry(self.root)
        self.entry_saldo.pack()

        self.label_tipo = tk.Label(self.root, text="Tipo de Conta:")
        self.label_tipo.pack()
        self.combobox_tipo = ttk.Combobox(self.root, values=["Corrente", "Poupança"])
        self.combobox_tipo.pack()

        self.button_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.pack()

    def cadastrar(self):
        titular = self.combobox_titular.get()
        banco = self.combobox_banco.get()
        tipo = self.combobox_tipo.get()
        saldo = float(self.entry_saldo.get())
        

        if titular and banco and tipo:
            cliente = Cliente.obter_cliente_por_nome(titular)
            if tipo == "Corrente":
                nova_conta = ContaCorrente(cliente, saldo, banco)
            else:
                nova_conta = ContaPoupanca(cliente, saldo, banco)
            messagebox.showinfo("Cadastro de Conta", "Conta cadastrada com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


class MostrarContas:
    colunas_contas = ('id', 'titular', 'saldo', 'banco', 'tipo', 'status')

    def __init__(self, frame, tipo_conta):
        self.root = frame
        self.tipo_conta = tipo_conta

        self.listbox_contas = ttk.Treeview(frame, columns=self.colunas_contas, show='headings')
        self.listbox_contas.grid()

        # Cabeçalho
        self.listbox_contas.heading('id', text='ID')
        self.listbox_contas.heading('titular', text='Titular')
        self.listbox_contas.heading('saldo', text='Saldo')
        self.listbox_contas.heading('banco', text='Banco')
        self.listbox_contas.heading('tipo', text='Tipo de Conta')
        self.listbox_contas.heading('status', text='Status')

        # Colunas
        self.listbox_contas.column('id', minwidth=50, width=50)
        self.listbox_contas.column('titular', minwidth=150, width=150)
        self.listbox_contas.column('saldo', minwidth=100, width=100)
        self.listbox_contas.column('banco', minwidth=150, width=150)
        self.listbox_contas.column('tipo', minwidth=100, width=100)
        self.listbox_contas.column('status', minwidth=100, width=100)

        # Linhas
        contas = self.obter_contas_por_tipo(tipo_conta)
        for conta in contas:
            self.listbox_contas.insert('', 'end', values=[conta.id, conta.titular, conta.saldo ,conta.banco, conta.__class__.__name__, conta.status])

        # Barra de rolagem
        scb = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.listbox_contas.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.listbox_contas.config(yscrollcommand=scb.set)

        # Botões
        frm_botoes = tk.Frame(self.root)
        frm_botoes.grid(row=1, column=0)

        btn_encerrar = tk.Button(frm_botoes, text='Encerrar', command=self.encerrar_conta)
        btn_encerrar.grid(row=0, column=0)
        btn_excluir = tk.Button(frm_botoes, text='Excluir')
        btn_excluir.grid(row=0, column=1)

    def obter_contas_por_tipo(self, tipo_conta):
        contas = []
        if tipo_conta == "Corrente":
            contas = ContaCorrente.obter_contas_corrente()
        elif tipo_conta == "Poupança":
            contas = ContaPoupanca.obter_contas_poupanca()
        return contas
    
    
    def encerrar_conta(self):
        item = self.listbox_contas.selection()

        if item:
            id_conta = int(self.listbox_contas.item(item, "values")[0])

            if self.tipo_conta == "Corrente":
                contas = ContaCorrente.obter_contas_corrente()
            elif self.tipo_conta == "Poupança":
                contas = ContaPoupanca.obter_contas_poupanca()

            conta_encerrar = None
            for conta in contas:
                if conta.id == id_conta:
                    conta_encerrar = conta
                    break

            if conta_encerrar:
                if conta_encerrar.saldo == 0:
                    conta_encerrar.encerrar_conta()
                    messagebox.showinfo("Encerrar Conta", "Conta encerrada com sucesso!")
                    self.listbox_contas.set(item, 'status', 'Encerrada')
                else:
                    messagebox.showerror("Erro", "A conta não pode ser encerrada pois possui saldo diferente de zero.")
            else:
                messagebox.showerror("Erro", "Conta não encontrada.")
        else:
            messagebox.showerror("Erro", "Nenhum item selecionado.")



            
            
