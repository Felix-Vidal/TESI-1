from ttkbootstrap import *
from tkinter import ttk, messagebox
from infra.entities.ERole import ERole

from infra.repository.RequesterRepository import RequesterRepository


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()

class RequesterList:
    
    def __init__(self, root, main_content, user_role):

        self.root = root
        self.main_content = main_content
        self.user_role = user_role
        
        
      # Treeview no conteúdo principal
        self.treeview = ttk.Treeview(self.main_content, columns=("ID", "Name", "Email", "Telephone", "Requester Type"), padding=(10, 20, 10, 5))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Name")
        self.treeview.heading("#3", text="Email")
        self.treeview.heading("#4", text="Telephone")
        self.treeview.heading("#4", text="Requester Type")
        self.treeview.pack(fill=tk.BOTH, expand=True)
        
        self.btn_Delete = ttk.Button(self.main_content, text="Delete", style="Outline.TButton")
        self.btn_Delete.pack(side=tk.RIGHT, padx=5)

        self.btn_editar = ttk.Button(self.main_content, text="Editar", style="Outline.TButton")
        self.btn_editar.pack(side=tk.RIGHT, padx=5 )

        self.btn_registrar = ttk.Button(self.main_content, text="Registrar", style="Outline.TButton", command=self.cadastrar_usuarios)
        self.btn_registrar.pack(side=tk.RIGHT, padx=5)
        

        # Botão para exibir a lista de usuários
        self.btn_list_requesters = ttk.Button(self.main_content, text="Exibir Lista de Requesters", style="Outline.TButton", command=self.exibir_lista_requesters)
        self.btn_list_requesters.pack(pady=10)

    def exibir_lista_requesters(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        print("Exibindo lista de requesters")

        # Preencher a Treeview com os usuários
        for requester in RequesterRepository.gets():
            self.treeview.insert("", "end", values=(requester.id, requester.name, requester.email, requester.telephone ,requester.typeRequester.name))
            print(f"ID: {requester.id}, Name: {requester.name}, email: {requester.eamil}, telephone: {requester.telephone} ,Role: {requester.typeRequester.name}")


