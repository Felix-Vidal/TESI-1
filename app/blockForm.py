from ttkbootstrap import *
from tkinter import ttk, messagebox
from blockList import BlockList

from infra.repository.BlocksRepository import BlocksRepository



# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class BlockForm:
    
    def __init__(self, root, main_content):

        self.root = root
        self.main_content = main_content
        
        # self.btn_voltar = ttk.Button(self.sidebar, text="Voltar", style="Outline.TButton")
        # self.btn_voltar.pack(pady=(5)) #por algum motivo n aparece embaixo dos menubutton
        
        # Create a frame to hold the user form
        self.block_form_frame = ttk.Frame(self.main_content)
        self.block_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.treeview = ttk.Treeview(self.main_content, padding=(10, 20, 10, 5))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the user form
        self.create_block_form()

    def register_block(self):
        
        # Retrieve user input from the form
        name = self.name_entry.get()
        
        # Validate input (you can add more validation if needed)
        if not name:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Insert the user into the database
        success = BlocksRepository.insert(name)
        if success:
            messagebox.showinfo("Success", "Block registered successfully.")
        else:
            messagebox.showerror("Error", "Block is already taken.")

    def create_block_form(self):
       
        # Create a frame to hold the block form
        self.block_form_frame = ttk.Frame(self.main_content)
        self.block_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create and place the form widgets
        ttk.Label(self.block_form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.block_form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        register_button = ttk.Button(self.block_form_frame, text="Register", style="Outline.TButton", command=self.register_block)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)
        
