from ttkbootstrap import *
from tkinter import ttk, messagebox
from userList import UserList
from infra.repository.BlocksRepository import BlocksRepository
from userForm import UserForm


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class BlockList:
    
    def __init__(self, root, main_content):

        self.root = root
        self.main_content = main_content
        
        # Botão para exibir a lista de usuários
        self.btn_list_blocks = ttk.Button(self.main_content, text="Exibir Lista de Blocos", style="Outline.TButton", command=self.exibir_lista_blocos)
        self.btn_list_blocks.pack(pady=10)
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("ID", "name"), padding=(10, 20, 10, 5))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="name")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def exibir_lista_blocos(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Buscar usuários do banco de dados
        blocks = BlocksRepository.gets()
        
        print("Exibindo lista de blocos")

        # Preencher a Treeview com os usuários
        for block in blocks:
            self.treeview.insert("", "end", values=(block.id, block.name))
            print(f"ID: {block.id}, name: {block.name}")


    def cadastrar_usuarios(self):
        limpar_tela(self.root)
        self.root.title("Usuários")
        user = UserForm(self.root)
    
    def listar_usuarios(self):
        limpar_tela(self.root)
        self.root.title("Usuários")
        user = UserList(self.root)

