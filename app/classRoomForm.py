from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.entities.ERoom import ERoom
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
from infra.repository.BlocksRepository import BlocksRepository



# from app.home import Home

def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ClassRoomForm:
    
    def __init__(self, root, main_content, id=None):

        self.root = root
        self.main_content = main_content
        self.id = id
        # Create a frame to hold the user form
        self.classroom_form_frame = ttk.Frame(self.main_content)
        self.classroom_form_frame.pack()
        
        self.create_classroom_form()

    def register_classroom(self):
        name = self.name_entry.get()
        capacity = int(self.capacity_entry.get())
        block_name = self.block_combobox.get()
        room = self.room_combobox.get()
        block = BlocksRepository.getName(block_name)
        if block:
            block_id = block.id
        else:
            messagebox.showerror("Error", "Invalid block selected.")
            return

        if not name or not capacity or not block_name or not room:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if self.id:
            success = ClassRoomsRepository.update(self.id, name, capacity, block_id, room)
        else:
            success = ClassRoomsRepository.insert(name, capacity, block_id, room)
        if success:
            messagebox.showinfo("Success", "Classroom registered successfully.")
        else: 
            messagebox.showerror("Error", "Class is already taken.")

    def create_classroom_form(self):
        
        width = 50
        font = ("", 16)

        self.classroom_form_frame = ttk.Frame(self.main_content)
        self.classroom_form_frame.pack(padx=(200,0), pady=40, fill=tk.BOTH, expand=True)
        if self.id:
            classroom, block = ClassRoomsRepository.get(self.id)
            print(classroom)
            
            # Create and place the form widgets
            ttk.Label(self.classroom_form_frame, text="Name:").pack(anchor="w")
            self.name_entry = ttk.Entry(self.classroom_form_frame, width=width, font=font)
            self.name_entry.insert(0, classroom.name)
            self.name_entry.pack(anchor="w")

            ttk.Label(self.classroom_form_frame, text="Capacity:").pack(anchor="w")
            self.capacity_entry = ttk.Entry(self.classroom_form_frame, width=width, font=font)
            self.capacity_entry.insert(0, classroom.capacity)
            self.capacity_entry.pack(anchor="w")

            ttk.Label(self.classroom_form_frame, text="Block:").pack(anchor="w")
            self.block_combobox = ttk.Combobox(self.classroom_form_frame, values=[block.name for block in BlocksRepository.gets()], width=width, font=font)
            self.block_combobox.insert(0, block.name)
            self.block_combobox.pack(anchor="w")
            
            ttk.Label(self.classroom_form_frame, text="Room Type:").pack(anchor="w")
            self.room_combobox = ttk.Combobox(self.classroom_form_frame, values=[room.name for room in ERoom], width=width, font=font)
            self.room_combobox.pack("w")
        else:
            ttk.Label(self.classroom_form_frame, text="Name:").pack(anchor="w")
            self.name_entry = ttk.Entry(self.classroom_form_frame, width=width, font=font)
            self.name_entry.pack(anchor="w")

            ttk.Label(self.classroom_form_frame, text="Capacity:").pack(anchor="w")
            self.capacity_entry = ttk.Entry(self.classroom_form_frame, width=width, font=font)
            self.capacity_entry.pack(anchor="w")

            ttk.Label(self.classroom_form_frame, text="Block:").pack(anchor="w")
            self.block_combobox = ttk.Combobox(self.classroom_form_frame, values=[block.name for block in BlocksRepository.gets()], width=width, font=font)
            self.block_combobox.pack(anchor="w")
            
            ttk.Label(self.classroom_form_frame, text="Room Type:").pack(anchor="w")
            self.room_combobox = ttk.Combobox(self.classroom_form_frame, values=[room.name for room in ERoom], width=width, font=font)
            self.room_combobox.pack(anchor="w")
            
        self.room_combobox.config(state='readonly')
        self.block_combobox.config(state='readonly')

        register_button = ttk.Button(self.classroom_form_frame, text="Register", style="TButton", command=self.register_classroom)
        register_button.pack(anchor="w")
        
