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
    
    def __init__(self, root):

        self.root = root
        # Configuração da janela principal
        self.root.title("SGAS")
        
        # Criação do estilo usando ttkbootstrap
        self.style = Style()
        self.style.configure("Outline.TButton", padding=(10, 5), width=15)
        self.style.configure("Outline.TMenubutton", padding=(10, 5), width=15)
        
        # Criação da barra lateral
        self.sidebar = ttk.Frame(root, style="TFrame")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Título na barra lateral
        self.title_label = ttk.Label(self.sidebar, text="SGAS",font="-size 24 -weight bold",  style="TLabel", padding=(10, 20, 10, 5))
        self.title_label.pack(fill=tk.X)
        
        # Menubuttons na barra lateral com estilo "OUTLINE"
        self.btn_user = ttk.Menubutton(self.sidebar, text="Usuarios", style="Outline.TMenubutton")
        self.btn_user.pack(pady=(10, 5))
        self.user_menu = tk.Menu(self.btn_user, tearoff=0)
        self.user_menu.add_command(label="Cadastrar", command=self.cadastrar_usuarios)
        self.user_menu.add_command(label="Listar", command=self.exibir_lista_usuarios)
        self.btn_user["menu"] = self.user_menu
        
        self.btn_room = ttk.Menubutton(self.sidebar, text="Salas", style="Outline.TMenubutton")
        self.btn_room.pack(pady=5)
        self.room_menu = tk.Menu(self.btn_room, tearoff=0)
        self.room_menu.add_command(label="Cadastrar")
        self.room_menu.add_command(label="Listar")
        self.btn_room["menu"] = self.room_menu
        
        self.btn_block = ttk.Menubutton(self.sidebar, text="Blocos", style="Outline.TMenubutton")
        self.btn_block.pack(pady=5)
        self.block_menu = tk.Menu(self.btn_block, tearoff=0)
        self.block_menu.add_command(label="Cadastrar")
        self.block_menu.add_command(label="Listar")
        self.btn_block["menu"] = self.block_menu
        
        self.btn_request = ttk.Menubutton(self.sidebar, text="Requisições", style="Outline.TMenubutton")
        self.btn_request.pack(pady=5)
        self.request_menu = tk.Menu(self.btn_request, tearoff=0)
        self.request_menu.add_command(label="Cadastrar")
        self.request_menu.add_command(label="Listar")
        self.btn_request["menu"] = self.request_menu
        
        # Conteúdo principal
        self.main_content = ttk.Frame(root)
        self.main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Botão para exibir a lista de usuários
        self.btn_list_users = ttk.Button(self.main_content, text="Exibir Lista de Usuários", style="Outline.TButton", command=self.exibir_lista_usuarios)
        self.btn_list_users.pack(pady=10)
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.root, columns=("ID", "name", "capacity", "block", "room_type"), padding=(10, 20, 10, 5))
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

