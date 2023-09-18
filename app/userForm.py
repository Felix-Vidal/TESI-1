from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.entities.ERole import ERole


from infra.repository.UsersRepository import UsersRepository

# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class UserForm:
    
    def __init__(self, root, main_content):

        self.root = root
        self.main_content = main_content
        
        # Create a frame to hold the user form
        self.user_form_frame = ttk.Frame(self.main_content)
        self.user_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.treeview = ttk.Treeview(self.main_content, padding=(10, 20, 10, 5))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the user form
        self.create_user_form()

    def register_user(self):
        """
        Callback function to register a new user.
        """
        # Retrieve user input from the form
        username = self.username_entry.get()
        full_name = self.full_name_entry.get()
        password = self.password_entry.get()
        role = ERole.ROLE_USER  # Assuming a new user is a regular user
        
        # Validate input (you can add more validation if needed)
        if not username or not full_name or not password or not role:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Insert the user into the database
        success = UsersRepository.insert(username, full_name, password, role)
        if success:
            messagebox.showinfo("Success", "User registered successfully.")
        else:
            messagebox.showerror("Error", "Username is already taken.")

    def create_user_form(self):
        """
        Create the user registration form.
        """
        # Create a frame to hold the user form
        self.user_form_frame = ttk.Frame(self.main_content)
        self.user_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create and place the form widgets
        ttk.Label(self.user_form_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(self.user_form_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.user_form_frame, text="Full Name:").grid(row=1, column=0, padx=5, pady=5)
        self.full_name_entry = ttk.Entry(self.user_form_frame)
        self.full_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.user_form_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(self.user_form_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.user_form_frame, text="Role:").grid(row=3, column=0, padx=5, pady=5)
        self.role_combobox = ttk.Combobox(self.user_form_frame, values=[role.name for role in ERole])
        self.role_combobox.grid(row=3, column=1, padx=5, pady=5)

        register_button = ttk.Button(self.user_form_frame, text="Register", style="Outline.TButton", command=self.register_user)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)
        
    # def listar_usuarios(self):
    #     limpar_tela(self.root)
    #     self.root.title("Usuários")
    #     user = UserList(self.root)
        