from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.entities.ESituation import ESituation
from schedulingForm import ScheduleForm
from classRoomForm import ClassRoomForm
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
        self.treeview = ttk.Treeview(self.main_content, columns=("id", "requester", "classRoom", "dateTime", "block", 'situation'), height=25)
        self.treeview.pack(fill=tk.X, padx=10, pady=10)
        
        self.treeview.heading("id", text="ID", anchor='w')
        self.treeview.heading("requester", text= "Requisitor", anchor='w')
        self.treeview.heading("classRoom", text = "Sala", anchor='w')
        self.treeview.heading("dateTime", text="Data e Hora", anchor='w')
        self.treeview.heading("block", text="Bloco", anchor='w')
        self.treeview.heading("situation", text="Situation", anchor='w')
        
        self.treeview.column('id',  minwidth=15, width=30, anchor='w')
        self.treeview.column('requester',  minwidth=200, width=200, anchor='w')
        self.treeview.column('classRoom',  minwidth=200, width=200, anchor='w')
        self.treeview.column('dateTime',  minwidth=200, width=200, anchor='w')
        self.treeview.column('block', minwidth=200, width=200, anchor='w')
        self.treeview.column('situation', minwidth=200, width=200, anchor='w')
        
        self.btn_Delete = ttk.Button(self.main_content, text="Cancelar", style="TButton", command=self.canceled)
        self.btn_Delete.pack(side=tk.RIGHT, padx=5)

        self.btn_editar = ttk.Button(self.main_content, text="Editar", style="TButton", command=self.editar)
        self.btn_editar.pack(side=tk.RIGHT, padx=5 )

        self.btn_registrar = ttk.Button(self.main_content, text="Registrar", style="TButton", command=self.cadastrar_agendamento)
        self.btn_registrar.pack(side=tk.RIGHT, padx=5)
        
        self.display_scheduling_list()

    def editar(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            limpar_tela(self.main_content)
            self.root.title("Agendamento")
            classroom = ScheduleForm(self.root ,self.main_content, id)

    def canceled(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            situation = self.treeview.item(item[0], "values")[5]
            if situation == ESituation.MARKED.name:
                SchedulingRepository.canceled(id)
            else:
                messagebox.showwarning('Aviso', 'item ja foi cancelado')
            self.display_scheduling_list()


    def display_scheduling_list(self):
        # Clear the current entries in the Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # ng data
        for scheduling, requester, classRoom, block in SchedulingRepository.gets():
            self.treeview.insert("", "end", values=(scheduling.id, requester.name, classRoom.name, scheduling.dateTime, block.name, scheduling.situation.name))
    def cadastrar_agendamento(self):
        limpar_tela(self.main_content)
        self.root.title("Agendamento")
        agenda = ScheduleForm(self.root, self.main_content)