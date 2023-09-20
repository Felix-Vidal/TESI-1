from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.repository.RequesterRepository import RequesterRepository
from infra.entities.ERequester import ERequester


# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class RequesterForm:
    
    def __init__(self, root, main_content, id = None):

        self.root = root
        self.main_content = main_content
        self.id = id
        
        
        self.requester_form_frame = ttk.Frame(self.main_content)
        self.requester_form_frame.pack()

        self.create_requester_form()

    def register_requester(self):
        
        name = self.name_entry.get()
        email = self.email_entry.get()
        telephone = int(self.telephone_entry.get())
        typeRequester = ERequester.ROLE_PROFESSOR  
        
        # Validate input (you can add more validation if needed)
        if not name or not email or not telephone or not typeRequester:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if self.id:
            success = RequesterRepository.update(self.id, name, email, telephone, typeRequester)
        else:
            success = RequesterRepository.insert(name, email, telephone, typeRequester)
        if success:
            messagebox.showinfo("Success", "Requester registered successfully.")
        else:
            messagebox.showerror("Error", "Email is already taken.")

    def create_requester_form(self):
        
        width = 50
        font = ("", 16)
        
        self.requester_form_frame = ttk.Frame(self.main_content)
        self.requester_form_frame.pack(padx=(200,0), pady=40, fill=tk.BOTH, expand=True)

        if self.id:
            requester = RequesterRepository.get(self.id)
            
            requester_type = requester.typeRequester.name.split(".")[-1]
            
            ttk.Label(self.requester_form_frame, text="Name:").pack(anchor="w")
            self.name_entry = ttk.Entry(self.requester_form_frame, width=width, font=font)
            self.name_entry.insert(0, requester.name)
            self.name_entry.pack(anchor="w")

            ttk.Label(self.requester_form_frame, text="Email:").pack(anchor="w")
            self.email_entry = ttk.Entry(self.requester_form_frame, width=width, font=font)
            self.email_entry.insert(0, requester.email)
            self.email_entry.pack(anchor="w")

            ttk.Label(self.requester_form_frame, text="Telephone:").pack(anchor="w")
            self.telephone_entry = ttk.Entry(self.requester_form_frame, width=width, font=font)
            self.telephone_entry.insert(0, requester.telephone)
            self.telephone_entry.pack(anchor="w")
            
            ttk.Label(self.requester_form_frame, text="Type Requester:").pack(anchor="w")
            self.type_requester_combobox = ttk.Combobox(self.requester_form_frame, values=[typeRequester.name for typeRequester in ERequester], width=width, font=font)
            self.type_requester_combobox.insert(0, requester_type)
            self.type_requester_combobox.pack(anchor="w")
        else:

            ttk.Label(self.requester_form_frame, text="Name:").pack(anchor="w")
            self.name_entry = ttk.Entry(self.requester_form_frame, width=width, font=font)
            self.name_entry.pack(anchor="w")

            ttk.Label(self.requester_form_frame, text="Email:").pack(anchor="w")
            self.email_entry = ttk.Entry(self.requester_form_frame, width=width, font=font)
            self.email_entry.pack(anchor="w")

            ttk.Label(self.requester_form_frame, text="Telephone:").pack(anchor="w")
            self.telephone_entry = ttk.Entry(self.requester_form_frame, width=width, font=font)
            self.telephone_entry.pack(anchor="w")
            
            ttk.Label(self.requester_form_frame, text="Type Requester:").pack(anchor="w")
            self.type_requester_combobox = ttk.Combobox(self.requester_form_frame, values=[typeRequester.name for typeRequester in ERequester], width=width, font=font)
            self.type_requester_combobox.pack(anchor="w")


        register_button = ttk.Button(self.requester_form_frame, text="Register", style="Outline.TButton", command=self.register_requester)
        register_button.pack(anchor="w")
        
   