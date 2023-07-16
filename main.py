import tkinter as tk
from tkinter import messagebox

class Banco:
    def __init__(self, numero, nome):
        self.__num = numero
        self.__nome = nome
        self.__contas = []

    def cadastrar_conta(self, conta):
        self.__contas.append(conta)

    def mostrar_informacoes(self):
        informacoes = f"Número: {self.__num}\nNome: {self.__nome}\n\nContas:"

        for conta in self.__contas:
            informacoes += f"\nNúmero da Conta: {conta.numero}\nTitular: {conta.titular}\nSaldo: {conta.saldo}\n"

        return informacoes

class Conta:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

class BancoGUI:
    def __init__(self, root, banco):
        self.root = root
        self.banco = banco

        # Configuração da janela principal
        self.root.title("Cadastro de Banco")
        self.root.geometry("400x300")

        # Criação dos widgets
        self.label_numero = tk.Label(self.root, text="Número:")
        self.label_numero.pack()

        self.entry_numero = tk.Entry(self.root)
        self.entry_numero.pack()

        self.label_nome = tk.Label(self.root, text="Nome:")
        self.label_nome.pack()

        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.button_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_banco)
        self.button_cadastrar.pack()

        self.button_mostrar = tk.Button(self.root, text="Mostrar Informações", command=self.mostrar_informacoes)
        self.button_mostrar.pack()

    def cadastrar_banco(self):
        numero = self.entry_numero.get()
        nome = self.entry_nome.get()

        if numero and nome:
            self.banco.__init__(numero, nome)
            messagebox.showinfo("Cadastro de Banco", "Banco cadastrado com sucesso!")
        else:
            messagebox.showerror("Cadastro de Banco", "Por favor, preencha todos os campos.")

    def mostrar_informacoes(self):
        informacoes = self.banco.mostrar_informacoes()
        messagebox.showinfo("Informações do Banco", informacoes)

if __name__ == "__main__":
    root = tk.Tk()
    banco = Banco("", "")  # Instância vazia inicial
    banco_gui = BancoGUI(root, banco)
    root.mainloop()
