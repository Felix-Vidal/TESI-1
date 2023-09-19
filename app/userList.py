from ttkbootstrap import *
from tkinter import ttk, messagebox
from userForm import UserForm
from infra.repository.UsersRepository import UsersRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class UserList:
    
    def __init__(self, root, main_content):

        self.root = root
        self.main_content = main_content
        
        
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("id", "userName", "fullName", "role"), height=25)
        self.treeview.pack(fill=tk.X, padx=10)

        self.treeview.heading("id", text="ID", anchor='w')
        self.treeview.heading("userName", text="UserName", anchor='w')
        self.treeview.heading("fullName", text="FullName", anchor='w')
        self.treeview.heading("role", text="Role", anchor='w')

        self.treeview.column('id', minwidth=15, width=30, anchor='w')
        self.treeview.column('userName', minwidth=200, width=200, anchor='w')
        self.treeview.column('fullName', minwidth=200, width=200, anchor='w')
        self.treeview.column('role', minwidth=200, width=200, anchor='w')


        #         #Barra de rolagem
        # scb = ttk.Scrollbar(self.main_content, orient="vertical", command=self.treeview.yview)
        # scb.grid(row=0, column=1, sticky='ns')
        # self.treeview.config(yscrollcommand=scb.set)

        self.btn_Delete = ttk.Button(self.main_content, text="Delete", style="Outline.TButton", command=self.delete)
        self.btn_Delete.pack(side=tk.RIGHT, padx=5)

        self.btn_editar = ttk.Button(self.main_content, text="Editar", style="Outline.TButton", command=self.editar)
        self.btn_editar.pack(side=tk.RIGHT, padx=5 )

        self.btn_registrar = ttk.Button(self.main_content, text="Registrar", style="Outline.TButton", command=self.cadastrar_usuarios)
        self.btn_registrar.pack(side=tk.RIGHT, padx=5)
        
        self.exibir_lista_usuarios()
        

    def editar(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            limpar_tela(self.main_content)
            self.root.title("Usuários")
            user = UserForm(self.root ,self.main_content, id)

    def delete(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            if UsersRepository.delete(id):
                self.exibir_lista_usuarios()
    
    def exibir_lista_usuarios(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Preencher a Treeview com os usuários
        for user in UsersRepository.gets():
            self.treeview.insert("", "end", values=[user.id, user.userName, user.fullName, user.role.name])


    def cadastrar_usuarios(self):
        limpar_tela(self.main_content)
        self.root.title("Usuários")
        user = UserForm(self.root ,self.main_content)

