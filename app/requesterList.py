from ttkbootstrap import *
from tkinter import ttk, messagebox
from requesterForm import RequesterForm
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
        self.treeview = ttk.Treeview(self.main_content, columns=("id", "name", "email", "telephone", "requesterType"), height=25)
        self.treeview.pack(fill=tk.X, padx=10, pady=10)

        self.treeview.heading("id", text="ID",anchor='w')
        self.treeview.heading("name", text="Name", anchor='w')
        self.treeview.heading("email", text="Email", anchor='w')
        self.treeview.heading("telephone", text="Telephone", anchor='w')
        self.treeview.heading("requesterType", text="Requester Type", anchor='w')

        self.treeview.column("id",  minwidth=15, width=30, anchor='w')
        self.treeview.column("name", minwidth=200, width=200, anchor='w')
        self.treeview.column("email", minwidth=200, width=200, anchor='w')
        self.treeview.column("telephone", minwidth=200, width=200, anchor='w')
        self.treeview.column("requesterType", minwidth=200, width=200, anchor='w')
        
        self.btn_Delete = ttk.Button(self.main_content, text="Delete", style="TButton", command=self.delete)
        self.btn_Delete.pack(side=tk.RIGHT, padx=5)

        self.btn_editar = ttk.Button(self.main_content, text="Editar", style="TButton", command=self.editar)
        self.btn_editar.pack(side=tk.RIGHT, padx=5 )

        self.btn_registrar = ttk.Button(self.main_content, text="Registrar", style="TButton", command=self.cadastrar_requester)
        self.btn_registrar.pack(side=tk.RIGHT, padx=5)
        
        self.exibir_lista_requesters()

    def editar(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            limpar_tela(self.main_content)
            user = RequesterForm(self.root ,self.main_content, id)

    def delete(self):
        item = self.treeview.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            id = int(self.treeview.item(item[0], "values")[0])
            if RequesterRepository.delete(id):
                self.exibir_lista_requesters()

    def cadastrar_requester(self):
        limpar_tela(self.main_content)
        user = RequesterForm(self.root ,self.main_content)
        
    def exibir_lista_requesters(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Preencher a Treeview com os usuários
        for requester in RequesterRepository.gets():
            self.treeview.insert("", "end", values=(requester.id, requester.name, requester.email, requester.telephone ,requester.typeRequester.name))


