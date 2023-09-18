from ttkbootstrap import *
from tkinter import ttk, messagebox
from schedulingList import ScheduleList
from schedulingForm import ScheduleForm
from requesterList import RequesterList
from requesterForm import RequesterForm
from classRoomList import ClassRoomList
from classRoomForm import ClassRoomForm
from blockForm import BlockForm
from blockList import BlockList
from userForm import UserForm

from userList import UserList

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class Home:
    
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
        self.user_menu.add_command(label="Listar", command=self.listar_usuarios)
        self.btn_user["menu"] = self.user_menu
        
        self.btn_room = ttk.Menubutton(self.sidebar, text="Salas", style="Outline.TMenubutton")
        self.btn_room.pack(pady=5)
        self.room_menu = tk.Menu(self.btn_room, tearoff=0)
        self.room_menu.add_command(label="Cadastrar", command=self.cadastrar_classrooms)
        self.room_menu.add_command(label="Listar", command=self.listar_classrooms)
        self.btn_room["menu"] = self.room_menu
        
        self.btn_block = ttk.Menubutton(self.sidebar, text="Blocos", style="Outline.TMenubutton")
        self.btn_block.pack(pady=5)
        self.block_menu = tk.Menu(self.btn_block, tearoff=0)
        self.block_menu.add_command(label="Cadastrar", command=self.cadastrar_blocos)
        self.block_menu.add_command(label="Listar", command=self.listar_blocos)
        self.btn_block["menu"] = self.block_menu
        
        self.btn_request = ttk.Menubutton(self.sidebar, text="Solicitantes", style="Outline.TMenubutton")
        self.btn_request.pack(pady=5)
        self.request_menu = tk.Menu(self.btn_request, tearoff=0)
        self.request_menu.add_command(label="Cadastrar", command=self.cadastrar_requesters)
        self.request_menu.add_command(label="Listar", command=self.listar_requesters)
        self.btn_request["menu"] = self.request_menu
        
        self.btn_request = ttk.Menubutton(self.sidebar, text="Agendados", style="Outline.TMenubutton")
        self.btn_request.pack(pady=5)
        self.request_menu = tk.Menu(self.btn_request, tearoff=0)
        self.request_menu.add_command(label="Cadastrar", command=self.cadastrar_schedules)
        self.request_menu.add_command(label="Listar", command=self.listar_schedules)
        self.btn_request["menu"] = self.request_menu
        
        # Conteúdo principal
        self.main_content = ttk.Frame(root)
        self.main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, padding=(10, 20, 10, 5))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    
    def cadastrar_usuarios(self):
        limpar_tela(self.root)
        self.root.title("Usuários")
        user = UserForm(self.root)
        
    def listar_usuarios(self):
        limpar_tela(self.root)
        self.root.title("Usuários")
        user = UserList(self.root)
        
    def cadastrar_blocos(self):
        limpar_tela(self.root)
        self.root.title("Blocos")
        block = BlockForm(self.root)
        
    def listar_blocos(self):
        limpar_tela(self.root)
        self.root.title("Blocos")
        block = BlockList(self.root)

    
    def cadastrar_classrooms(self):
        limpar_tela(self.root)
        self.root.title("Salas")
        block = ClassRoomForm(self.root)
        
    def listar_classrooms(self):
        limpar_tela(self.root)
        self.root.title("Salas")
        classroom = ClassRoomList(self.root)
        
    def cadastrar_requesters(self):
        limpar_tela(self.root)
        self.root.title("Requesters")
        requester = RequesterForm(self.root)
        
    def listar_requesters(self):
        limpar_tela(self.root)
        self.root.title("Requester")
        requester = RequesterList(self.root)
        
    def cadastrar_schedules(self):
        limpar_tela(self.root)
        self.root.title("Schedule")
        schedule = ScheduleForm(self.root)
        
    def listar_schedules(self):
        limpar_tela(self.root)
        self.root.title("Schedule")
        schedule = ScheduleList(self.root)

