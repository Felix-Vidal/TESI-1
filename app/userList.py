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
        self.treeview = ttk.Treeview(self.main_content, columns=("id", "userName", "fullName", "role", "active"), height=25)
        self.treeview.pack(fill=tk.X, padx=10, pady=10)

        self.treeview.heading("id", text="ID", anchor='w')
        self.treeview.heading("userName", text="UserName", anchor='w')
        self.treeview.heading("fullName", text="FullName", anchor='w')
        self.treeview.heading("role", text="Role", anchor='w')
        self.treeview.heading("active", text="Active", anchor='w')

        self.treeview.column('id', minwidth=15, width=30, anchor='w')
        self.treeview.column('userName', minwidth=200, width=200, anchor='w')
        self.treeview.column('fullName', minwidth=200, width=200, anchor='w')
        self.treeview.column('role', minwidth=200, width=200, anchor='w')
        self.treeview.column('active', minwidth=200, width=200, anchor='w')
        
        self.btn_Delete = ttk.Button(self.main_content, text="Habilitar/Desabilitar", style="TButton", command=self.toggling)
        self.btn_Delete.pack(side=tk.RIGHT, padx=5)

        self.btn_editar = ttk.Button(self.main_content, text="Editar", style="TButton", command=self.editar)
        self.btn_editar.pack(side=tk.RIGHT, padx=5 )

        self.btn_registrar = ttk.Button(self.main_content, text="Registrar", style="TButton", command=self.cadastrar_usuarios)
        self.btn_registrar.pack(side=tk.RIGHT, padx=5)
        
        # self.search_entry = ttk.Entry(self.main_content)
        # self.search_entry.pack(side=tk.LEFT, padx=5)
        # self.search_button = ttk.Button(self.main_content, text="Search", style="TButton", command=self.search_users)
        # self.search_button.pack(side=tk.LEFT, padx=5)
        
        if self.user_role == ERole.ROLE_USER:
            self.btn_registrar.pack_forget()
            self.btn_editar.pack_forget()
            self.btn_Delete.pack_forget()
            
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

    def toggling(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            active = self.treeview.item(item[0], "values")[4]
            if active == "True":
                if UsersRepository.desabilita(id):
                    self.exibir_lista_usuarios()
            elif active == "False":
                if UsersRepository.habilitar(id):
                    self.exibir_lista_usuarios()
    
    def exibir_lista_usuarios(self, search_term=None):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # for index, user in enumerate(UsersRepository.gets(search_term)):
        for index, user in enumerate(UsersRepository.gets()):
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'
            bg_color = '#28394a' if index % 2 == 0 else '#32465a' 
            self.treeview.insert("", "end", values=[user.id, user.userName, user.fullName, user.role.name, user.active], tags=(tag,), iid=user.id)
            self.treeview.tag_configure(tag, background=bg_color)


    def cadastrar_usuarios(self):
        limpar_tela(self.main_content)
        self.root.title("Usuários")
        user = UserForm(self.root ,self.main_content)

    # def search_users(self):
    #     search_term = self.search_entry.get()
    #     self.exibir_lista_usuarios(search_term)