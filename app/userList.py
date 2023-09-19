from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.entities.ERole import ERole
from userForm import UserForm
from infra.repository.UsersRepository import UsersRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class UserList:
    
    def __init__(self, root, main_content, user_role):

        self.root = root
        self.user_role = user_role
        self.main_content = main_content
        
        
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("id", "userName", "fullName", "role"), height=25)
        self.treeview.pack(fill=tk.X, padx=10)

        self.treeview.heading("id", text="ID", anchor='center')
        self.treeview.heading("userName", text="UserName", anchor='center')
        self.treeview.heading("fullName", text="FullName", anchor='center')
        self.treeview.heading("role", text="Role", anchor='center')

        self.treeview.column('id', minwidth=15, width=30, anchor='center')
        self.treeview.column('userName', minwidth=200, width=200, anchor='center')
        self.treeview.column('fullName', minwidth=200, width=200, anchor='center')
        self.treeview.column('role', minwidth=200, width=200, anchor='center')


        #         #Barra de rolagem
        # scb = tk.Scrollbar(self.main_content, orient=tk.VERTICAL, command=self.treeview.yview)
        # scb.grid(row=0, column=1, sticky='ns')
        # self.treeview.config(yscrollcommand=scb.set)

        self.btn_Delete = ttk.Button(self.main_content, text="Delete", style="Outline.TButton")
        self.btn_Delete.pack(side=tk.RIGHT, padx=5)

        self.btn_editar = ttk.Button(self.main_content, text="Editar", style="Outline.TButton")
        self.btn_editar.pack(side=tk.RIGHT, padx=5 )

        self.btn_registrar = ttk.Button(self.main_content, text="Registrar", style="Outline.TButton", command=self.cadastrar_usuarios)
        self.btn_registrar.pack(side=tk.RIGHT, padx=5)
        
        if self.user_role == ERole.ROLE_USER:
            self.btn_registrar.pack_forget()
            self.btn_editar.pack_forget()
            self.btn_Delete.pack_forget()
            
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

