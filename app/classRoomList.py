from ttkbootstrap import *
from tkinter import ttk, messagebox
from classRoomForm import ClassRoomForm
from infra.entities.ERole import ERole
from infra.repository.BlocksRepository import BlocksRepository
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
from userForm import UserForm
from infra.repository.UsersRepository import UsersRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ClassRoomList:
    
    def __init__(self, root, main_content, user_role):

        self.root = root
        self.main_content = main_content
        self.user_role = user_role
        
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("ID", "name", "capacity", "block", "room_type"), padding=(10, 20, 10, 5))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="name")
        self.treeview.heading("#3", text="capacidade")
        self.treeview.heading("#4", text="Block")
        self.treeview.heading("#5", text="Tipo de sala")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
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

        # Botão para exibir a lista de usuários
        self.btn_list_users = ttk.Button(self.main_content, text="Exibir Lista de Usuários", style="Outline.TButton", command=self.exibir_lista_usuarios)
        self.btn_list_users.pack(pady=10)

    def exibir_lista_usuarios(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Preencher a Treeview com os usuários
        for classRoom, block in ClassRoomsRepository.gets():
            self.treeview.insert("", "end", values=(classRoom.id, classRoom.name, classRoom.capacity, block.name ,classRoom.typeRoom))


    def cadastrar_usuarios(self):
        limpar_tela(self.root)
        self.root.title("Usuários")
        user = UserForm(self.root)
        
    def editar(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            limpar_tela(self.main_content)
            room = ClassRoomForm(self.root ,self.main_content, id)
    
    def delete(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            if ClassRoomsRepository.delete(id):
                self.exibir_lista_usuarios()
    def exibir_lista_usuarios(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Preencher a Treeview com os usuários
        for room in ClassRoomsRepository.gets():
            self.treeview.insert("", "end", values=[room.id, room.name])

