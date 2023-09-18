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
        
        # Botão para exibir a lista de usuários
        self.btn_list_users = ttk.Button(self.main_content, text="Exibir Lista de Usuários", style="Outline.TButton", command=self.exibir_lista_usuarios)
        self.btn_list_users.pack(pady=10)
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("id", "userName", "fullName", "role"), padding=(10, 20, 10, 5))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.treeview.heading("id", text="ID", anchor='center')
        self.treeview.heading("userName", text="UserName", anchor='center')
        self.treeview.heading("fullName", text="FullName", anchor='center')
        self.treeview.heading("role", text="Role", anchor='center')

        self.treeview.column('id', minwidth=15, width=30, anchor='center')
        self.treeview.column('userName', minwidth=200, width=200, anchor='center')
        self.treeview.column('fullName', minwidth=200, width=200, anchor='center')
        self.treeview.column('role', minwidth=200, width=200, anchor='center')

        

    def exibir_lista_usuarios(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Buscar usuários do banco de dados
        users = UsersRepository.gets()
        
        print("Exibindo lista de usuários")

        # Preencher a Treeview com os usuários
        for user in users:
            self.treeview.insert("", "end", values=[user.id, user.userName, user.fullName, user.role.name])
            print(f"ID: {user.id}, UserName: {user.userName}, FullName: {user.fullName}, Role: {user.role.name}")


    def cadastrar_usuarios(self):
        limpar_tela(self.root)
        self.root.title("Usuários")
        user = UserForm(self.root)

