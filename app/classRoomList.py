from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.repository.BlocksRepository import BlocksRepository
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
from userForm import UserForm
from infra.repository.UsersRepository import UsersRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ClassRoomList:
    
    def __init__(self, root, main_content):

        self.root = root
        self.main_content = main_content
        
        # Botão para exibir a lista de usuários
        self.btn_list_users = ttk.Button(self.main_content, text="Exibir Lista de Usuários", style="Outline.TButton", command=self.exibir_lista_usuarios)
        self.btn_list_users.pack(pady=10)
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("ID", "name", "capacity", "block", "room_type"), padding=(10, 20, 10, 5))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="name")
        self.treeview.heading("#3", text="capacidade")
        self.treeview.heading("#4", text="Block")
        self.treeview.heading("#5", text="Tipo de sala")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def exibir_lista_usuarios(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Buscar usuários do banco de dados
        classrooms = ClassRoomsRepository.gets()
        
        print("Exibindo lista de usuários")

        # Preencher a Treeview com os usuários
        for classroom in classrooms:
            block = BlocksRepository.get_by_id(classroom.block)
            if block:
                self.treeview.insert("", "end", values=(classroom.id, classroom.name, classroom.capacity, block.name ,classroom.TypeRoom.name))
                print(f"ID: {classroom.id}, name: {classroom.name}, capacity: {classroom.capacity}, block: {block.name} ,TypeRoom: {classroom.TypeRoom.name}")
            else:
                print(f"ID: {classroom.id}, name: {classroom.name}, capacity: {classroom.capacity}, block not found, typeRoom: {classroom.typeRoom.name}")


    def cadastrar_usuarios(self):
        limpar_tela(self.root)
        self.root.title("Usuários")
        user = UserForm(self.root)

