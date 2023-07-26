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
        self.root.configure(bg="#edebeb")
        
        self.label_banco = tk.Label(self.root, text="Banco:")
        self.label_banco.pack()
        lista_bancos = Banco.listar_bancos()
        bancos = [f"ID: {banco._num} Banco: {banco._nome}" for banco in lista_bancos]
        self.combobox_banco = ttk.Combobox(self.root, values=bancos,state="readonly")
        self.combobox_banco.pack()

        self.label_titular = tk.Label(self.root, text="Titular:")
        self.label_titular.pack()
        lista_clientes = Cliente.listar_clientes()
        titular = [f"ID: {titular._num} Titular: {titular._nome}" for titular in lista_clientes]
        self.combobox_titular = ttk.Combobox(self.root, values=titular,state="readonly")
        self.combobox_titular.pack()

        self.label_saldo = tk.Label(self.root, text="Saldo:")
        self.label_saldo.pack()
        self.entry_saldo = tk.Entry(self.root)
        self.entry_saldo.pack()

        self.label_tipo = tk.Label(self.root, text="Tipo de Conta:")
        self.label_tipo.pack()
        self.combobox_tipo = ttk.Combobox(self.root, values=["Corrente", "Poupança"],state="readonly")
        self.combobox_tipo.pack()

        self.button_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.pack(pady=5)

    def cadastrar(self):
        id_titular = int(self.combobox_titular.get()[4])
        id_banco = int(self.combobox_banco.get()[4])
        tipo = self.combobox_tipo.get()
        saldo = float(self.entry_saldo.get())
        

        if id_titular and id_banco and tipo:
            cliente = Cliente.get_id(id_titular)
            if(cliente):
                if tipo == "Corrente":
                    if ContaCorrente.verificar_conta_unica(cliente._CPF, id_banco):
                        nova_conta = ContaCorrente(cliente, saldo)
                        Banco.incluir_conta(id_banco, nova_conta)
                        messagebox.showinfo("Cadastro de Conta", "Conta cadastrada com sucesso!")
                    else:
                        messagebox.showerror("Erro", f"Cliente ja tem um conta corrente {self.combobox_banco.get()}.")
                    
                else:
                    if ContaPoupanca.verificar_conta_unica(cliente._CPF):
                        nova_conta = ContaPoupanca(cliente, saldo)
                        Banco.incluir_conta(id_banco, nova_conta)
                        messagebox.showinfo("Cadastro de Conta", "Conta cadastrada com sucesso!")
                    else:
                        messagebox.showerror("Erro", f"Cliente ja tem um conta poupança {self.combobox_banco.get()}.")
                        
            else:
                messagebox.showerror("Erro", "Cliente não encontrado.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


class MostrarContas:
    colunas_contas = ('id', 'titular', 'saldo', 'banco', 'tipo', 'status')

    def __init__(self, frame, tipo_conta):
        self.root = frame
        self.root.configure(bg="#edebeb")
        self.tipo_conta = tipo_conta

        self.listbox_contas = ttk.Treeview(frame, columns=self.colunas_contas, show='headings')
        self.listbox_contas.grid()

        # Cabeçalho
        self.listbox_contas.heading('id', text='ID',anchor='center')
        self.listbox_contas.heading('titular', text='Titular', anchor='center')
        self.listbox_contas.heading('saldo', text='Saldo',anchor='center')
        self.listbox_contas.heading('banco', text='Banco',anchor='center')
        self.listbox_contas.heading('tipo', text='Tipo de Conta',anchor='center')
        self.listbox_contas.heading('status', text='Status',anchor='center')

        # Colunas
        self.listbox_contas.column('id', minwidth=50, width=50,anchor='center')
        self.listbox_contas.column('titular', minwidth=150, width=150,anchor='center')
        self.listbox_contas.column('saldo', minwidth=100, width=100,anchor='center')
        self.listbox_contas.column('banco', minwidth=150, width=150,anchor='center')
        self.listbox_contas.column('tipo', minwidth=100, width=100,anchor='center')
        self.listbox_contas.column('status', minwidth=100, width=100,anchor='center')

        # Linhas
        bancos = Banco.listar_bancos()
        contas = self.obter_contas_por_tipo(tipo_conta)
        for conta in contas:
            for banco in bancos:
                if conta in banco._contas:
                    self.listbox_contas.insert('', 'end', values=[conta.id, conta.titular, conta.saldo ,banco._nome, conta.__class__.__name__, conta.status])

        # Barra de rolagem
        scb = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.listbox_contas.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.listbox_contas.config(yscrollcommand=scb.set)

        # Botões
        frm_botoes = tk.Frame(self.root)
        frm_botoes.grid(row=1, column=0)

        btn_ativar = tk.Button(frm_botoes, text='Ativar Conta', command=self.ativar_conta)
        btn_ativar.grid(row=0, column=0, padx=3, pady=5)
        
        btn_encerrar = tk.Button(frm_botoes, text='Encerrar Conta', command=self.encerrar_conta)
        btn_encerrar.grid(row=0, column=1, padx=3, pady=5)
        
        btn_gerar_relatorio = tk.Button(frm_botoes, text='Gerar Relatório', command=self.gerar_relatorio)
        btn_gerar_relatorio.grid(row=0, column=2, padx=3, pady=5)

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

            for conta in contas:
                if conta._num == id_conta:
                    if conta.encerrar_conta(conta._num) == True:
                        messagebox.showinfo("Encerrar Conta", "Conta encerrada com sucesso!")
                        self.listbox_contas.set(item, 'status', 'Encerrada')
                        return None
                    if conta.encerrar_conta(conta._num) == "Encerrada":
                        messagebox.showwarning("Encerrar Conta", "Conta ja está encerrada")
                        return None
                    else:
                        messagebox.showerror("Erro", "A conta não pode ser encerrada pois possui saldo diferente de zero.")
                        return None
                
            messagebox.showerror("Erro", "Conta não encontrada.")

    def ativar_conta(self):
        item = self.listbox_contas.selection()
        if item:
            id_conta = int(self.listbox_contas.item(item, "values")[0])
            if self.tipo_conta == "Corrente":
                contas = ContaCorrente.obter_contas_corrente()
            elif self.tipo_conta == "Poupança":
                contas = ContaPoupanca.obter_contas_poupanca()

            for conta in contas:
                if conta._num == id_conta:
                    if conta.ativar_conta(conta._num) == True:
                        messagebox.showinfo("Ativar Conta", "Conta Ativada com sucesso!")
                        self.listbox_contas.set(item, 'status', 'Ativa')
                        return None
                    else:
                        messagebox.showwarning("Ativar Conta", "Conta ja está Ativada")
                        return None
                
            messagebox.showerror("Erro", "Conta não encontrada.")
            
    def gerar_relatorio(self):
        item = self.listbox_contas.selection()
        if item:
            id_conta = int(self.listbox_contas.item(item, "values")[0])
            if self.tipo_conta == "Corrente":
                contas = ContaCorrente.obter_contas_corrente()
            elif self.tipo_conta == "Poupança":
                contas = ContaPoupanca.obter_contas_poupanca()

            for conta in contas:
                if conta._num == id_conta:
                    self.limpar_frame()
                    self.mostrar_relatorio(conta)

                    return

            messagebox.showerror("Erro", "Conta não encontrada.")

    def limpar_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def mostrar_relatorio(self, conta):
        self.root.configure(bg="#edebeb")
        for widget in self.root.winfo_children():
            widget.destroy()

        report_frame = tk.Frame(self.root)
        report_frame.pack(fill='both', expand=True)

        report_tree = ttk.Treeview(report_frame, columns=('data', 'tipo_operacao', 'valor', 'saldo_final'), show='headings')
        report_tree.heading('data', text='Data', anchor='center')
        report_tree.heading('tipo_operacao', text='Tipo de Operação', anchor='center')
        report_tree.heading('valor', text='Valor', anchor='center')
        report_tree.heading('saldo_final', text='Saldo Final', anchor='center')
        report_tree.grid(row=0, column=0, sticky='nsew')

        h_scrollbar = ttk.Scrollbar(report_frame, orient=tk.HORIZONTAL, command=report_tree.xview)
        v_scrollbar = ttk.Scrollbar(report_frame, orient=tk.VERTICAL, command=report_tree.yview)
        report_tree.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')

        report_frame.grid_rowconfigure(0, weight=1)
        report_frame.grid_columnconfigure(0, weight=1)

        for transacao in conta._extrato._transacoes:
            data, tipo_operacao, valor, saldo_final = transacao.split(", ")
            report_tree.insert('', 'end', values=(data, tipo_operacao, valor, saldo_final))

        saldo_label = tk.Label(report_frame, text=f"Saldo Final: {conta._saldo}")
        saldo_label.grid(row=2, column=0, columnspan=2)

        salvar_button = tk.Button(report_frame, text="Salvar Relatório", command=lambda: self.salvar_relatorio(conta))
        salvar_button.grid(row=3, column=0, columnspan=2, pady=5)

    def salvar_relatorio(self, conta):
        filename = f"relatorio_conta_{conta._num}.txt"
        with open(filename, "w") as file:
            file.write(f"Extrato da Conta {conta._num}:\n")
            for transacao in conta._extrato._transacoes:
                file.write(f"{transacao}\n")
            file.write(f"Saldo Final: {conta._saldo}\n")

        messagebox.showinfo("Relatório Salvo", f"O relatório da conta {conta._num} foi salvo com sucesso!")
                



            
            
