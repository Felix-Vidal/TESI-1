import tkinter as tk
from tkinter import messagebox, ttk
from banco import Banco

class CadastroBanco:

    def __init__(self, frame):
        self.root = frame

        self.label_nome = tk.Label(self.root, text="Nome do Banco:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.button_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.pack()

    def cadastrar(self):
        nome_banco = self.entry_nome.get()
        if nome_banco:
            novo_banco = Banco(nome_banco)
            messagebox.showinfo("Cadastro de Banco", "Banco cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, informe o nome do banco.")


class MostrarBancos:
    colunas_bancos = ('id','nome')
    def __init__(self, frame, banco):
        self.root = frame
        self.banco = banco
    	

        self.listbox_bancos = ttk.Treeview(frame, columns=self.colunas_bancos, show='headings')
        self.listbox_bancos.grid()

        #Cabeçalho
        self.listbox_bancos.heading('id', text='ID')
        self.listbox_bancos.heading('nome', text='Nome')

        #Colunas
        self.listbox_bancos.column('id', minwidth=15, width=30)
        self.listbox_bancos.column('nome', minwidth=300, width=300)

        #Linhas
        bancos = self.banco.listar_bancos()
        for b in bancos:
            self.listbox_bancos.insert('', 'end', values=[b._num, b._nome])

        #Barra de rolagem
        scb = tk.Scrollbar(self.root, orient=tk.VERTICAL,command=self.listbox_bancos.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.listbox_bancos.config(yscrollcommand=scb.set)

        #Botões
        frm_botoes = tk.Frame(self.root)
        frm_botoes.grid(row=1, column=0)

        btn_editar = tk.Button(frm_botoes, text='Editar', command=self.editar)
        btn_editar.grid(row=0, column=0)
        btn_excluir = tk.Button(frm_botoes, text='Excluir')
        btn_excluir.grid(row=0, column=1)

    def editar(self):
        item = self.listbox_bancos.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            valores = self.listbox_bancos.item(item, 'values')
            self.top_editar = tk.Toplevel()
            self.top_editar.grab_set()

            #id do objeto invisivel 
            self.ent_id = tk.Entry(self.top_editar)
            self.ent_id.insert('end', valores[0])

            lbl_nome = tk.Label(self.top_editar, text='Nome:')
            lbl_nome.grid(row=0, column=0)

            self.ent_nome = tk.Entry(self.top_editar)
            self.ent_nome.grid(row=0, column=1)
            self.ent_nome.insert('end', valores[1])

            btn_confirmar = tk.Button(self.top_editar,text='Confirmar',command=self.confirmar_edicao)
            btn_confirmar.grid(row=1, column=0, columnspan=2)

    def confirmar_edicao(self):
        id = int(self.ent_id.get())
        nome = self.ent_nome.get()

        selecionado = self.listbox_bancos.selection()
        if nome == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.')
        else:
            Banco.atualizar_banco(id,nome)
            self.listbox_bancos.item(selecionado, values=(id,nome))
            self.top_editar.destroy()
        




# class AtualizarBanco:
#     def __init__(self, root, lista_bancos):  # Recebe a lista de bancos como argumento
#         self.root = root
#         self.lista_bancos = lista_bancos

#         self.label_selecione = tk.Label(root, text="Selecione um banco:")
#         self.label_selecione.pack()
#         self.combobox_bancos = tk.Combobox(root, values=self.lista_bancos)  # Preenche a combobox com a lista de bancos
#         self.combobox_bancos.pack()

#         self.button_atualizar = tk.Button(root, text="Atualizar", command=self.atualizar)
#         self.button_atualizar.pack()
#     def atualizar(self):
#         indice_selecionado = self.combobox_bancos.current()
#         bancos = self.banco.listar_bancos()
#         if 0 <= indice_selecionado < len(bancos):
#             banco_selecionado = bancos[indice_selecionado]
#             messagebox.showinfo("Atualização de Banco", f"Você selecionou o banco: {banco_selecionado._nome}")
            
#             # Obter os valores dos campos de atualização
#             novo_nome = self.entry_nome.get()
#             banco_selecionado._nome = novo_nome
#             messagebox.showinfo("Atualização de Banco", "Banco atualizado com sucesso!")
#             self.root.destroy()
#         else:
#             messagebox.showerror("Erro", "Selecione um banco válido.")