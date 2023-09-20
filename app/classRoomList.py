from ttkbootstrap import *
from tkinter import ttk, messagebox
from classRoomForm import ClassRoomForm
from infra.entities.ERole import ERole
from infra.repository.ClassRoomsRepository import ClassRoomsRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class ClassRoomList:
    
    def __init__(self, root, main_content, user_role):

        self.root = root
        self.main_content = main_content
        self.user_role = user_role
        
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("id", "name", "capacity", "block", "room_type"), height=25)
        self.treeview.pack(fill=tk.X, padx=10, pady=10)
        
        self.treeview.heading("id", text="ID", anchor='w')
        self.treeview.heading("name", text="Nome", anchor='w')
        self.treeview.heading("capacity", text="Capacidade", anchor='w')
        self.treeview.heading("block", text="Bloco", anchor='w')
        self.treeview.heading("room_type", text="Tipo de Sala", anchor='w')
        
        self.treeview.column('id', minwidth=15, width=30, anchor='w')
        self.treeview.column("name", minwidth=200, width=200, anchor='w')
        self.treeview.column("capacity",minwidth=200, width=200, anchor='w')
        self.treeview.column("block", minwidth=200, width=200, anchor='w')
        self.treeview.column("room_type", minwidth=200, width=200, anchor='w')
        
        self.btn_Delete = ttk.Button(self.main_content, text="Delete", style="TButton", command=self.delete)
        self.btn_Delete.pack(side=tk.RIGHT, padx=5)

        self.btn_editar = ttk.Button(self.main_content, text="Editar", style="TButton", command=self.editar)
        self.btn_editar.pack(side=tk.RIGHT, padx=5 )

        self.btn_registrar = ttk.Button(self.main_content, text="Registrar", style="TButton", command=self.cadastrar_salas)
        self.btn_registrar.pack(side=tk.RIGHT, padx=5)
        
        if self.user_role == ERole.ROLE_USER:
            self.btn_registrar.pack_forget()
            self.btn_editar.pack_forget()
            self.btn_Delete.pack_forget()
            
        self.exibir_lista_salas()



    def editar(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            limpar_tela(self.main_content)
            self.root.title("Salas")
            room = ClassRoomForm(self.root ,self.main_content, id)

    def delete(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            if ClassRoomsRepository.delete(id):
                self.exibir_lista_salas()
                
    def exibir_lista_salas(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Preencher a Treeview com os usuários
        for classRoom, block in ClassRoomsRepository.gets():
            
            self.treeview.insert("", "end", values=(classRoom.id, classRoom.name, classRoom.capacity, block.name ,classRoom.typeRoom.name))

    def cadastrar_salas(self):
        limpar_tela(self.main_content)
        self.root.title("Salas")
        sala = ClassRoomForm(self.root, self.main_content)

