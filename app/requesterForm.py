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
    
    def __init__(self, root, main_content):

        self.root = root
        self.main_content = main_content
        
        
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
        
   