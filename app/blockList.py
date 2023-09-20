from ttkbootstrap import *
from tkinter import ttk, messagebox
from blockForm import BlockForm
from infra.entities.ERole import ERole
from userList import UserList
from infra.repository.BlocksRepository import BlocksRepository
from userForm import UserForm


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class BlockList:
    
    def __init__(self, root, main_content, user_role):

        self.root = root
        self.main_content = main_content
        self.user_role = user_role
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("id", "name") , height=25)
        self.treeview.pack(fill=tk.X, padx=10, pady=10)
        
        self.treeview.heading("id", text="ID" , anchor='w')
        self.treeview.heading("name", text="name", anchor='w')

        self.treeview.column('id', minwidth=15, width=30, anchor='w')
        self.treeview.column('name', minwidth=200, width=200, anchor='w')

        self.treeview.pack(fill=tk.X, padx=10)
        
        self.btn_Delete = ttk.Button(self.main_content, text="Delete", style="TButton", command=self.delete)
        self.btn_Delete.pack(side=tk.RIGHT, padx=5)

        self.btn_editar = ttk.Button(self.main_content, text="Editar", style="TButton", command=self.editar)
        self.btn_editar.pack(side=tk.RIGHT, padx=5 )

        self.btn_registrar = ttk.Button(self.main_content, text="Registrar", style="TButton", command=self.cadastrar_blocos)
        self.btn_registrar.pack(side=tk.RIGHT, padx=5)
        
        if self.user_role == ERole.ROLE_USER:
            self.btn_registrar.pack_forget()
            self.btn_editar.pack_forget()
            self.btn_Delete.pack_forget()

        self.exibir_lista_blocos()

    def editar(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            limpar_tela(self.main_content)
            block = BlockForm(self.root ,self.main_content, id)

    def cadastrar_blocos(self):
        limpar_tela(self.main_content)
        block = BlockForm(self.root ,self.main_content)

    def delete(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            if BlocksRepository.delete(id):
                self.exibir_lista_usuarios()
    
    def exibir_lista_usuarios(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Preencher a Treeview com os usuários
        for block in BlocksRepository.gets():
            self.treeview.insert("", "end", values=[block.id, block.name])

    def exibir_lista_blocos(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Preencher a Treeview com os usuários
        for block in BlocksRepository.gets():
            self.treeview.insert("", "end", values=(block.id, block.name))


