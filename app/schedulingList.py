from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.repository.SchedulingRepository import SchedulingRepository
from infra.repository.BlocksRepository import BlocksRepository
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
from userForm import UserForm
from infra.repository.UsersRepository import UsersRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ScheduleList:
    
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
        self.user_menu.add_command(label="Cadastrar")
        self.user_menu.add_command(label="Listar")
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
        
        # Create a Treeview to display the scheduling list
        self.treeview = ttk.Treeview(self.main_content, columns=("ID", "Requester", "Classroom", "Date and Time"), padding=(10, 20, 10, 5))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Requester")
        self.treeview.heading("#3", text="Classroom")
        self.treeview.heading("#4", text="Date and Time")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button to refresh and display the scheduling list
        self.refresh_button = ttk.Button(self.main_content, text="Refresh Scheduling List", style="Outline.TButton", command=self.display_scheduling_list)
        self.refresh_button.pack(pady=10)

    def display_scheduling_list(self):
        # Clear the current entries in the Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Retrieve the list of schedulings from the repository
        schedulings = SchedulingRepository.gets()

        print("Displaying scheduling list")

        # Populate the Treeview with the scheduling data
        for scheduling in schedulings:
            requester_name = scheduling[1].name if scheduling[1] else "N/A"
            classroom_name = scheduling[2].name if scheduling[2] else "N/A"
            datetime_str = str(scheduling[0].dateTime)
            self.treeview.insert("", "end", values=(scheduling[0].id, requester_name, classroom_name, datetime_str))
            print(f"ID: {scheduling[0].id}, Requester: {requester_name}, Classroom: {classroom_name}, Date and Time: {datetime_str}")