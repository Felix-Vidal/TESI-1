from ttkbootstrap import *
from tkinter import ttk, messagebox

from infra.repository.RequesterRepository import RequesterRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class RequesterList:
    
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
        
        # Botão para exibir a lista de usuários
        self.btn_list_requesters = ttk.Button(self.main_content, text="Exibir Lista de Requesters", style="Outline.TButton", command=self.exibir_lista_requesters)
        self.btn_list_requesters.pack(pady=10)
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.root, columns=("ID", "Name", "Email", "Telephone", "Requester Type"), padding=(10, 20, 10, 5))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Name")
        self.treeview.heading("#3", text="Email")
        self.treeview.heading("#4", text="Telephone")
        self.treeview.heading("#4", text="Requester Type")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def exibir_lista_requesters(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Buscar usuários do banco de dados
        requesters = RequesterRepository.gets()
        
        print("Exibindo lista de requesters")

        # Preencher a Treeview com os usuários
        for requester in requesters:
            self.treeview.insert("", "end", values=(requester.id, requester.name, requester.email, requester.telephone ,requester.typeRequester.name))
            print(f"ID: {requester.id}, Name: {requester.name}, email: {requester.eamil}, telephone: {requester.telephone} ,Role: {requester.typeRequester.name}")


