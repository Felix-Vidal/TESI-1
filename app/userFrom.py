from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.entities.ERole import ERole

from infra.repository.UsersRepository import UsersRepository

# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class UserForm:
    
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
        
        self.btn_request = ttk.Menubutton(self.sidebar, text="Requisições", style="Outline.TMenubutton")
        self.btn_request.pack(pady=5)
        self.request_menu = tk.Menu(self.btn_request, tearoff=0)
        self.request_menu.add_command(label="Cadastrar")
        self.request_menu.add_command(label="Listar")
        self.btn_request["menu"] = self.request_menu
        
        self.main_content = ttk.Frame(root)
        self.main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create a frame to hold the user form
        self.user_form_frame = ttk.Frame(self.main_content)
        self.user_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.treeview = ttk.Treeview(self.main_content, padding=(10, 20, 10, 5))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the user form
        self.create_user_form()

    def create_user_form(self):
        # Labels
        ttk.Label(self.user_form_frame, text="User Name:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.user_form_frame, text="Full Name:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self.user_form_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self.user_form_frame, text="Role:").grid(row=3, column=0, padx=5, pady=5)

        # Entry fields
        self.user_name_entry = ttk.Entry(self.user_form_frame)
        self.user_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.full_name_entry = ttk.Entry(self.user_form_frame)
        self.full_name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.password_entry = ttk.Entry(self.user_form_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        self.role_combobox = ttk.Combobox(self.user_form_frame, values=[role.name for role in ERole])
        self.role_combobox.grid(row=3, column=1, padx=5, pady=5)

        # Button to submit the form
        ttk.Button(self.user_form_frame, text="Submit", style="Outline.TButton", command=self.submit_user).grid(row=4, column=0, columnspan=2, pady=10)

    def submit_user(self):
        user_name = self.user_name_entry.get()
        full_name = self.full_name_entry.get()
        password = self.password_entry.get()
        role = ERole[self.role_combobox.get()]

        # Ensure user_name, full_name, and password are not empty
        if not user_name or not full_name or not password:
            messagebox.showerror("Error", "Please provide all user details.")
            return

        # Insert the user into the database
        result = UsersRepository.insert(user_name, full_name, password, role)

        if result:
            messagebox.showinfo("Success", "User successfully added.")
        else:
            messagebox.showerror("Error", "User with this username already exists.")

        # Update the Treeview with the new data
        self.update_treeview()

    def update_treeview(self):
        # Function to update the Treeview with user data
        # Retrieve user data from the database using UsersRepository
        users_data = UsersRepository.gets()

        # Clear existing Treeview data
        self.treeview.delete(*self.treeview.get_children())

        # Insert user data into the Treeview
        for user in users_data:
            self.treeview.insert("", "end", values=(user.userName, user.fullName, user.password, user.role))

        