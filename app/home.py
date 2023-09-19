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
    
    def __init__(self, root, user_role):

        self.root = root
        # Configuração da janela principal
        self.root.title("SGAS")
        self.user_role = user_role
        
        # Criação do estilo usando ttkbootstrap
        self.style = Style()
        self.style.configure("TButton", padding=(10, 5), width=15)
        self.style.configure("Outline.TMenubutton", padding=(10, 5), width=15)
        
        # Criação da barra lateral
        self.sidebar = ttk.Frame(root, style="TFrame")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Título na barra lateral
        self.title_label = ttk.Label(self.sidebar, text="SGAS",font="-size 24 -weight bold",  style="TLabel", padding=(10, 20, 10, 5))
        self.title_label.pack(fill=tk.X)
        
        # Menubuttons na barra lateral com estilo "OUTLINE"

        self.btn_schedule = ttk.Button(self.sidebar, text="Agendados", style="TButton", command=self.listar_schedules)
        self.btn_schedule.pack(pady=5)

        self.btn_request = ttk.Button(self.sidebar, text="Solicitantes", style="TButton", command=self.listar_requesters)
        self.btn_request.pack(pady=5)

        self.btn_room = ttk.Button(self.sidebar, text="Salas", style="TButton", command=self.listar_classrooms)
        self.btn_room.pack(pady=5)

        self.btn_block = ttk.Button(self.sidebar, text="Blocos", style="TButton", command=self.listar_blocos)
        self.btn_block.pack(pady=5)

        self.btn_user = ttk.Button(self.sidebar, text="Usuarios", style="TButton", command=self.listar_usuarios)
        self.btn_user.pack(pady=(10, 5))

        # Conteúdo principal
        self.main_content = ttk.Frame(root)
        self.main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, padding=(10, 20, 10, 5))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    
    def cadastrar_usuarios(self):
        limpar_tela(self.main_content)
        self.root.title("Usuários")
        user = UserForm(self.root, self.main_content)
        
    def listar_usuarios(self):
        limpar_tela(self.main_content)
        self.root.title("Usuários")
        user = UserList(self.root, self.main_content, self.user_role)
        
    def cadastrar_blocos(self):
        limpar_tela(self.main_content)
        self.root.title("Blocos")
        block = BlockForm(self.root, self.main_content)
        
    def listar_blocos(self):
        limpar_tela(self.main_content)
        self.root.title("Blocos")
        block = BlockList(self.root, self.main_content,self.user_role)

    
    def cadastrar_classrooms(self):
        limpar_tela(self.main_content)
        self.root.title("Salas")
        block = ClassRoomForm(self.root, self.main_content)
        
    def listar_classrooms(self):
        limpar_tela(self.main_content)
        self.root.title("Salas")
        classroom = ClassRoomList(self.root, self.main_content, self.user_role)
        
    def cadastrar_requesters(self):
        limpar_tela(self.main_content)
        self.root.title("Requesters")
        requester = RequesterForm(self.root, self.main_content)
        
    def listar_requesters(self):
        limpar_tela(self.main_content)
        self.root.title("Requester")
        requester = RequesterList(self.root, self.main_content,self.user_role)
        
    def cadastrar_schedules(self):
        limpar_tela(self.main_content)
        self.root.title("Schedule")
        schedule = ScheduleForm(self.root, self.main_content)
        
    def listar_schedules(self):
        limpar_tela(self.main_content)
        self.root.title("Schedule")
        schedule = ScheduleList(self.root, self.main_content, self.user_role)

