import tkinter as tk
from tkinter import messagebox
from banco import Banco

class CadastroBanco:

    def __init__(self, frame):
        self.root = frame

        self.label_nome = tk.Label(self.root, text="Nome do Banco:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.button_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.pack()

    def cadastrar(self):
        nome_banco = self.entry_nome.get()
        if nome_banco:
            novo_banco = Banco(nome_banco)
            messagebox.showinfo("Cadastro de Banco", "Banco cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, informe o nome do banco.")


class MostrarBancos:
    def __init__(self, frame, banco):
        self.root = frame
        self.banco = banco

        self.listbox_bancos = tk.Listbox(frame)
        self.listbox_bancos.pack()

        bancos = self.banco.listar_bancos()
        for b in bancos:
            self.listbox_bancos.insert(tk.END, b)



# class AtualizarBanco:
#     def __init__(self, root, lista_bancos):  # Recebe a lista de bancos como argumento
#         self.root = root
#         self.lista_bancos = lista_bancos

#         self.label_selecione = tk.Label(root, text="Selecione um banco:")
#         self.label_selecione.pack()
#         self.combobox_bancos = tk.Combobox(root, values=self.lista_bancos)  # Preenche a combobox com a lista de bancos
#         self.combobox_bancos.pack()

#         self.button_atualizar = tk.Button(root, text="Atualizar", command=self.atualizar)
#         self.button_atualizar.pack()
#     def atualizar(self):
#         indice_selecionado = self.combobox_bancos.current()
#         bancos = self.banco.listar_bancos()
#         if 0 <= indice_selecionado < len(bancos):
#             banco_selecionado = bancos[indice_selecionado]
#             messagebox.showinfo("Atualização de Banco", f"Você selecionou o banco: {banco_selecionado._nome}")
            
#             # Obter os valores dos campos de atualização
#             novo_nome = self.entry_nome.get()
#             banco_selecionado._nome = novo_nome
#             messagebox.showinfo("Atualização de Banco", "Banco atualizado com sucesso!")
#             self.root.destroy()
#         else:
#             messagebox.showerror("Erro", "Selecione um banco válido.")
