from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.repository.RequesterRepository import RequesterRepository
from infra.entities.ERequester import ERequester


from infra.repository.UsersRepository import UsersRepository

# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class RequesterForm:
    
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
        
        # self.btn_voltar = ttk.Button(self.sidebar, text="Voltar", style="Outline.TButton")
        # self.btn_voltar.pack(pady=(5)) #por algum motivo n aparece embaixo dos menubutton
        
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
        
        self.btn_request = ttk.Menubutton(self.sidebar, text="Solicitantes", style="Outline.TMenubutton")
        self.btn_request.pack(pady=5)
        self.request_menu = tk.Menu(self.btn_request, tearoff=0)
        self.request_menu.add_command(label="Cadastrar")
        self.request_menu.add_command(label="Listar")
        self.btn_request["menu"] = self.request_menu
        
        self.main_content = ttk.Frame(root)
        self.main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.requester_form_frame = ttk.Frame(self.main_content)
        self.requester_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.treeview = ttk.Treeview(self.main_content, padding=(10, 20, 10, 5))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_requester_form()

    def register_requester(self):
        
        name = self.name_entry.get()
        email = self.email_entry.get()
        telephone = self.telephone_entry.get()
        typeRequester = ERequester.ROLE_PROFESSOR  
        
        # Validate input (you can add more validation if needed)
        if not name or not email or not telephone or not typeRequester:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        
        success = RequesterRepository.insert(name, email, telephone, typeRequester)
        if success:
            messagebox.showinfo("Success", "Requester registered successfully.")
        else:
            messagebox.showerror("Error", "Email is already taken.")

    def create_requester_form(self):
        
        self.requester_form_frame = ttk.Frame(self.main_content)
        self.requester_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create and place the form widgets
        ttk.Label(self.requester_form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.requester_form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.requester_form_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(self.requester_form_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.requester_form_frame, text="Telephone:").grid(row=2, column=0, padx=5, pady=5)
        self.telephone_entry = ttk.Entry(self.requester_form_frame)
        self.telephone_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.requester_form_frame, text="Type Requester:").grid(row=3, column=0, padx=5, pady=5)
        self.type_requester_combobox = ttk.Combobox(self.requester_form_frame, values=[typeRequester.name for typeRequester in ERequester])
        self.type_requester_combobox.grid(row=3, column=1, padx=5, pady=5)

        register_button = ttk.Button(self.requester_form_frame, text="Register", style="Outline.TButton", command=self.register_requester)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)
        
   