import tkinter as tk
from tkinter import ttk
from conta import Conta

class SelecionarContaFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label_tipo_conta = tk.Label(self, text="Selecione o tipo de conta:")
        self.label_tipo_conta.pack()
        self.combobox_tipo_conta = ttk.Combobox(self, values=["Corrente", "Poupança"], state="readonly")
        self.combobox_tipo_conta.pack()

        self.label_conta = tk.Label(self, text="Selecione a conta:")
        self.label_conta.pack()
        self.combobox_conta = ttk.Combobox(self, state="readonly")
        self.combobox_conta.pack()

        self.button_selecionar = tk.Button(self, text="Selecionar", command=self.listar_contas)
        self.button_selecionar.pack()

        self.button_gerar_relatorio = tk.Button(self, text="Gerar Relatório", command=self.gerar_relatorio)
        self.button_gerar_relatorio.pack()

    def listar_contas(self):
        tipo_conta = self.combobox_tipo_conta.get()
        if tipo_conta:
            self.combobox_conta['values'] = self.obter_contas(tipo_conta)

    def obter_contas(self, tipo_conta):
        if tipo_conta == "Corrente":
            return [f"ID: {conta.id} - Titular: {conta.titular}" for conta in Conta.obter_contas_corrente()]
        elif tipo_conta == "Poupança":
            return [f"ID: {conta.id} - Titular: {conta.titular}" for conta in Conta.obter_contas_poupanca()]

    def gerar_relatorio(self):
        conta_str = self.combobox_conta.get()
        if conta_str:
            id_conta = int(conta_str.split()[1])
            tipo_conta = self.combobox_tipo_conta.get()

            if tipo_conta == "Corrente":
                contas = Conta.obter_contas_corrente()
            else:
                contas = Conta.obter_contas_poupanca()

            for conta in contas:
                if conta.id == id_conta:
                    conta.salvar_relatorio()
                    return

            tk.messagebox.showerror("Erro", "Conta não encontrada.")

