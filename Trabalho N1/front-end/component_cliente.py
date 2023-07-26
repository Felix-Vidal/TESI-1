import tkinter as tk
from tkinter import messagebox, ttk
from conta import Conta
from cliente import Cliente


class CadastroCliente:
    def __init__(self, frame):
        self.root = frame
        self.root.configure(bg="#edebeb")

        self.label_nome = tk.Label(self.root, text="Nome do Cliente:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.label_endereco = tk.Label(self.root, text="Endereço do Cliente:")
        self.label_endereco.pack()
        self.entry_endereco = tk.Entry(self.root)
        self.entry_endereco.pack()

        self.label_cpf = tk.Label(self.root, text="CPF do Cliente:")
        self.label_cpf.pack()
        self.entry_cpf = tk.Entry(self.root)
        self.entry_cpf.pack()

        self.label_idade = tk.Label(self.root, text="Idade do Cliente:")
        self.label_idade.pack()
        self.entry_idade = tk.Entry(self.root)
        self.entry_idade.pack()

        self.button_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.pack(pady=5)

    def cadastrar(self):
        nome_cliente = self.entry_nome.get()
        endereco_cliente = self.entry_endereco.get()
        cpf_cliente = self.entry_cpf.get()
        idade_cliente = self.entry_idade.get()

        if nome_cliente and endereco_cliente and cpf_cliente and idade_cliente:
            if (Cliente.validarCPF(cpf_cliente)):
                if Cliente.verificar_mesmo_cpf(cpf_cliente):
                    if int(idade_cliente) >= 16:
                        novo_cliente = Cliente(nome_cliente, endereco_cliente, cpf_cliente, idade_cliente)
                        messagebox.showinfo("Cadastro de Cliente", "Cliente cadastrado com sucesso!")
                    else:
                        messagebox.showwarning('Aviso', 'Idade invalida, idades menores que 16 anos são invalidas')
                else:
                    messagebox.showerror("Erro", "O CPF ja existe no sistema.")
            else:
                messagebox.showerror("Erro", "Por favor, coloque um cpf valido.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            

class MostrarClientes:
    colunas_clientes = ('id', 'nome', 'endereco', 'cpf', 'idade')

    def __init__(self, frame):
        self.root = frame
        self.root.configure(bg="#edebeb")
        self.clientes = Cliente.listar_clientes()  # Obter a lista de clientes

        self.listbox_clientes = ttk.Treeview(frame, columns=self.colunas_clientes, show='headings')
        self.listbox_clientes.grid()

        # Cabeçalho
        self.listbox_clientes.heading('id', text='ID', anchor='center')
        self.listbox_clientes.heading('nome', text='Nome',anchor='center')
        self.listbox_clientes.heading('endereco', text='Endereço', anchor='center')
        self.listbox_clientes.heading('cpf', text='CPF', anchor='center')
        self.listbox_clientes.heading('idade', text='Idade',anchor='center')

        # Colunas
        self.listbox_clientes.column('id', minwidth=15, width=30, anchor='center')
        self.listbox_clientes.column('nome', minwidth=150, width=150, anchor='center')
        self.listbox_clientes.column('endereco', minwidth=150, width=150, anchor='center')
        self.listbox_clientes.column('cpf', minwidth=100, width=100, anchor='center')
        self.listbox_clientes.column('idade', minwidth=50, width=50, anchor='center')

        # Linhas
        self.carregar_clientes()

        # Barra de rolagem
        scb = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.listbox_clientes.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.listbox_clientes.config(yscrollcommand=scb.set)

        # Botões
        frm_botoes = tk.Frame(self.root)
        frm_botoes.grid(row=1, column=0)

        btn_editar = tk.Button(frm_botoes, text='Editar', command=self.editar)
        btn_editar.grid(row=0, column=0, padx=5, pady=5)
        btn_excluir = tk.Button(frm_botoes, text='Excluir', command=self.excluir)
        btn_excluir.grid(row=0, column=1, padx=5, pady=5)

    def carregar_clientes(self):
        for cliente in self.clientes:
            self.listbox_clientes.insert('', 'end', values=[
                cliente._num, cliente._nome, cliente._endereco, cliente._CPF, cliente._idade])

    def editar(self):
        item = self.listbox_clientes.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            valores = self.listbox_clientes.item(item, 'values')
            self.top_editar = tk.Toplevel()
            self.top_editar.grab_set()

            lbl_id = tk.Label(self.top_editar, text='ID:')
            self.ent_id = tk.Entry(self.top_editar)
            self.ent_id.insert('end', valores[0])

            lbl_nome = tk.Label(self.top_editar, text='Nome:')
            lbl_nome.grid(row=0, column=0)

            self.ent_nome = tk.Entry(self.top_editar)
            self.ent_nome.grid(row=0, column=1)
            self.ent_nome.insert('end', valores[1])
            
            lbl_endereco = tk.Label(self.top_editar, text='Endereço:')
            lbl_endereco.grid(row=1, column=0)
            
            self.ent_endereco = tk.Entry(self.top_editar)
            self.ent_endereco.grid(row=1, column=1)
            self.ent_endereco.insert('end', valores[2])
            
            lbl_CPF = tk.Label(self.top_editar, text='CPF:')
            lbl_CPF.grid(row=2, column=0)
            
            self.ent_CPF = tk.Entry(self.top_editar)
            self.ent_CPF.grid(row=2, column=1)
            self.ent_CPF.insert('end', valores[3])
            self.ent_CPF.config(state='readonly')
            
            lbl_idade = tk.Label(self.top_editar, text='Idade:')
            lbl_idade.grid(row=3, column=0)
            
            self.ent_idade = tk.Entry(self.top_editar)
            self.ent_idade.grid(row=3, column=1)
            self.ent_idade.insert('end', valores[4])
            

            btn_confirmar = tk.Button(self.top_editar,
                                      text='Confirmar',
                                      command=self.confirmar_edicao)
            btn_confirmar.grid(row=4, column=0)

    def confirmar_edicao(self):
        id = int(self.ent_id.get())
        nome = self.ent_nome.get()
        endereco = self.ent_endereco.get()
        CPF = self.ent_CPF.get()
        idade = self.ent_idade.get()
        

        selecionado = self.listbox_clientes.selection()
        if nome == '' or endereco == '' or CPF == '' or idade == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.')
        else:
            Cliente.atualizar_cliente(id, nome, endereco, CPF, idade)
            self.listbox_clientes.item(selecionado, values=(id, nome, endereco, CPF, idade))
            self.top_editar.destroy()

    def excluir(self):
        item = self.listbox_clientes.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            cliente_selecionado = self.clientes[self.listbox_clientes.index(item)]
            if Conta.verificar_conta_vinculada(cliente_selecionado):
                messagebox.showerror('Erro', 'O cliente possui uma conta vinculada e não pode ser excluído.')
            else:
                Cliente.remover_cliente(cliente_selecionado)
                self.listbox_clientes.delete(item)
                messagebox.showinfo('Excluir Cliente', 'Cliente removido com sucesso.')