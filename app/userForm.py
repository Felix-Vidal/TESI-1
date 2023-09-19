from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.entities.ERole import ERole

from infra.repository.UsersRepository import UsersRepository

# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class UserForm:
    
    def __init__(self, root, main_content, id=None):

        self.root = root
        self.main_content = main_content
        self.id = id
        # Create a frame to hold the user form
        self.user_form_frame = ttk.Frame(self.main_content)
        self.user_form_frame.pack()

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
        if self.id:
            success = UsersRepository.update(self.id, username, full_name, password, role)
        else:
            success = UsersRepository.insert(username, full_name, password, role)
        if success:
            messagebox.showinfo("Success", "User registered successfully.")
        else:
            messagebox.showerror("Error", "Username is already taken.")

    def create_user_form(self):
        """
        Create the user registration form.
        """
        width = 50
        font = ("", 16)

        # Create a frame to hold the user form
        self.user_form_frame = ttk.Frame(self.main_content)
        self.user_form_frame.pack(padx=(200,0), pady=40, fill=tk.BOTH, expand=True)
        if self.id:
            user = UsersRepository.get(self.id)

        
            

            # Create and place the form widgets
            ttk.Label(self.user_form_frame, text="Username:").pack(anchor="w")
            self.username_entry = ttk.Entry(self.user_form_frame, width=width, font=font)
            self.username_entry.insert(0, user.userName)
            self.username_entry.pack(anchor="w")

            ttk.Label(self.user_form_frame, text="Full Name:").pack(anchor="w")
            self.full_name_entry = ttk.Entry(self.user_form_frame, width=width, font=font)
            self.full_name_entry.insert(0, user.fullName)
            self.full_name_entry.pack(anchor="w")

            ttk.Label(self.user_form_frame, text="Password:").pack(anchor="w")
            self.password_entry = ttk.Entry(self.user_form_frame, show="*", width=width, font=font)
            self.password_entry.insert(0, user.password)
            self.password_entry.pack(anchor="w")
            
            ttk.Label(self.user_form_frame, text="Role:").pack(anchor="w")
            self.role_combobox = ttk.Combobox(self.user_form_frame, values=[role.name for role in ERole], width=width, font=font)
            self.role_combobox.pack(anchor="w")
        else:

            # Create and place the form widgets
            ttk.Label(self.user_form_frame, text="Username:").pack(anchor="w")
            self.username_entry = ttk.Entry(self.user_form_frame, width=width, font=font)
            self.username_entry.pack(anchor="w")

            ttk.Label(self.user_form_frame, text="Full Name:").pack(anchor="w")
            self.full_name_entry = ttk.Entry(self.user_form_frame, width=width, font=font)
            self.full_name_entry.pack(anchor="w")

            ttk.Label(self.user_form_frame, text="Password:").pack(anchor="w")
            self.password_entry = ttk.Entry(self.user_form_frame, show="*", width=width, font=font)
            self.password_entry.pack(anchor="w")
            
            ttk.Label(self.user_form_frame, text="Role:").pack(anchor="w")
            self.role_combobox = ttk.Combobox(self.user_form_frame, values=[role.name for role in ERole], width=width, font=font)
            self.role_combobox.pack(anchor="w")
            
        self.role_combobox.config(state='readonly')

        self.register_button = ttk.Button(self.user_form_frame, text="Register", style="Outline.TButton", command=self.register_user)
        self.register_button.pack(anchor="w")
        
        
        