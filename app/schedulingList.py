from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.repository.SchedulingRepository import SchedulingRepository
from infra.repository.BlocksRepository import BlocksRepository
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
from infra.repository.UsersRepository import UsersRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ScheduleList:
    
    def __init__(self, root, main_content, user_role):

        self.root = root
        self.main_content = main_content
        self.user_role = user_role
        
        # Create a Treeview to display the scheduling list
        self.treeview = ttk.Treeview(self.main_content, columns=("ID", "Requester", "Classroom", "Date and Time", "Block"), padding=(10, 20, 10, 5))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Requester")
        self.treeview.heading("#3", text="Classroom")
        self.treeview.heading("#4", text="Date and Time")
        self.treeview.heading("#5", text="Block")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button to refresh and display the scheduling list
        self.refresh_button = ttk.Button(self.main_content, text="Refresh Scheduling List", style="Outline.TButton", command=self.display_scheduling_list)
        self.refresh_button.pack(pady=10)

    def display_scheduling_list(self):
        # Clear the current entries in the Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Populate the Treeview with the scheduling data
        for scheduling, requester, classRoom, block in SchedulingRepository.gets():
            self.treeview.insert("", "end", values=(scheduling.id, requester.name, classRoom.name, scheduling.dateTime, block.name))