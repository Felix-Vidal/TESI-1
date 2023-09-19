from ttkbootstrap import *
from tkinter import ttk, messagebox

from infra.repository.BlocksRepository import BlocksRepository



# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class BlockForm:
    
    def __init__(self, root, main_content, id=None):

        self.root = root
        self.main_content = main_content
        self.id = id
        
        # self.btn_voltar = ttk.Button(self.sidebar, text="Voltar", style="Outline.TButton")
        # self.btn_voltar.pack(pady=(5)) #por algum motivo n aparece embaixo dos menubutton
        
        # Create a frame to hold the user form
        self.user_form_frame = ttk.Frame(self.main_content)
        self.user_form_frame.pack()

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
        if self.id:
            success = BlocksRepository.update(self.id, name)
        else:
            success = BlocksRepository.insert(name)
    
        if success:
            messagebox.showinfo("Success", "Block registered successfully.")
        else:
            messagebox.showerror("Error", "Block is already taken.")

    def create_block_form(self):
        width = 50
        font = ("", 16)
        # Create a frame to hold the block form
        self.block_form_frame = ttk.Frame(self.main_content)
        self.block_form_frame.pack(padx=(200,0), pady=40, fill=tk.BOTH, expand=True)
        if self.id:
            block = BlocksRepository.get(self.id)

            ttk.Label(self.block_form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
            self.name_entry = ttk.Entry(self.block_form_frame, width=width, font=font)
            self.name_entry.insert(0, block.name)
            self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        else:
            # Create and place the form widgets
            ttk.Label(self.block_form_frame, text="Name:", width=width, font=font).grid(row=0, column=0, padx=5, pady=5)
            self.name_entry = ttk.Entry(self.block_form_frame, width=width, font=font)
            self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        register_button = ttk.Button(self.block_form_frame, text="Register", style="Outline.TButton", command=self.register_block)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)
        
