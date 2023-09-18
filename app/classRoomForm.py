from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.entities.ERoom import ERoom
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
from blockList import BlockList

from infra.repository.BlocksRepository import BlocksRepository



# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ClassRoomForm:
    
    def __init__(self, root, main_content):

        self.root = root
        self.main_content = main_content
  
        
        # Create a frame to hold the user form
        self.block_form_frame = ttk.Frame(self.main_content)
        self.block_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.treeview = ttk.Treeview(self.main_content, padding=(10, 20, 10, 5))
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        
        self.create_classroom_form()

    def register_classroom(self):
        # Retrieve user input from the form
        name = self.name_entry.get()
        capacity = int(self.capacity_entry.get())
        block_name = self.block_combobox.get()
        room = ERoom.CLASS_ROOM

        
        
        # Get the block ID based on the selected block name
        block = BlocksRepository.getName(block_name)
        if block:
            block_id = block.id
        else:
            messagebox.showerror("Error", "Invalid block selected.")
            return

        # Validate input
        if not name or not capacity or not block_name or not room:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Insert the classroom into the database
        success = ClassRoomsRepository.insert(name, capacity, block_id, room)
        if success:
            messagebox.showinfo("Success", "Classroom registered successfully.")
        else: 
            messagebox.showerror("Error", "Class is already taken.")

    def create_classroom_form(self):
       
        # Create a frame to hold the classroom form
        self.classroom_form_frame = ttk.Frame(self.main_content)
        self.classroom_form_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create and place the form widgets
        ttk.Label(self.classroom_form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.classroom_form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.classroom_form_frame, text="Capacity:").grid(row=1, column=0, padx=5, pady=5)
        self.capacity_entry = ttk.Entry(self.classroom_form_frame)
        self.capacity_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.classroom_form_frame, text="Block:").grid(row=2, column=0, padx=5, pady=5)
        self.block_combobox = ttk.Combobox(self.classroom_form_frame, values=[block.name for block in BlocksRepository.gets()])
        self.block_combobox.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.classroom_form_frame, text="Room Type:").grid(row=3, column=0, padx=5, pady=5)
        self.room_combobox = ttk.Combobox(self.classroom_form_frame, values=[room.name for room in ERoom])
        self.room_combobox.grid(row=3, column=1, padx=5, pady=5)

        register_button = ttk.Button(self.classroom_form_frame, text="Register", style="Outline.TButton", command=self.register_classroom)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)
        
    def listar_blocos(self):
        limpar_tela(self.root)
        self.root.title("Blocos")
        block = BlockList(self.root)
    # def listar_usuarios(self):
    #     limpar_tela(self.root)
    #     self.root.title("Usuários")
    #     user = UserList(self.root)
        