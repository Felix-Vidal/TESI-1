import tkinter as tk
from tkinter import ttk, messagebox
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from banco import Banco

class SaqueFrame(tk.Frame):
    def __init__(self, parent, tipo_conta):
        super().__init__(parent)

        self.tipo_conta = tipo_conta

        self.label_conta = tk.Label(self, text="Selecione a conta:")
        self.label_conta.pack()
        self.combobox_conta = ttk.Combobox(self, values=self.obter_contas(), state="readonly")
        self.combobox_conta.pack()

        self.label_valor = tk.Label(self, text="Valor:")
        self.label_valor.pack()
        self.entry_valor = tk.Entry(self)
        self.entry_valor.pack()

        self.button_sacar = tk.Button(self, text="Sacar", command=self.sacar)
        self.button_sacar.pack()

    def obter_contas(self):
        if self.tipo_conta == "Corrente":
            return [f"ID: {conta.id} - Titular: {conta.titular}" for conta in ContaCorrente.obter_contas_corrente()]
        elif self.tipo_conta == "Poupança":
            return [f"ID: {conta.id} - Titular: {conta.titular}" for conta in ContaPoupanca.obter_contas_poupanca()]

    def sacar(self):
        id_conta = int(self.combobox_conta.get().split()[1])
        valor = float(self.entry_valor.get())

        if self.tipo_conta == "Corrente":
            contas = ContaCorrente.obter_contas_corrente()
        else:
            contas = ContaPoupanca.obter_contas_poupanca()

        for conta in contas:
            if conta.id == id_conta:
                if conta.status == "Encerrada":
                    messagebox.showerror("Erro", "Conta encerrada. Não é possível realizar saques.")
                    return

                if conta.sacar(valor):
                    messagebox.showinfo("Saque", "Saque realizado com sucesso!")
                    self.entry_valor.delete(0, tk.END)
                    self.combobox_conta.set("")
                else:
                    messagebox.showerror("Erro", "Saldo insuficiente para o saque.")
                return

        messagebox.showerror("Erro", "Conta não encontrada.")

class SaqueHome(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label_tipo_conta = tk.Label(self, text="Selecione o tipo de conta:")
        self.label_tipo_conta.pack()
        self.combobox_tipo_conta = ttk.Combobox(self, values=["Corrente", "Poupança"], state="readonly")
        self.combobox_tipo_conta.pack()

        self.button_selecionar = tk.Button(self, text="Selecionar", command=self.selecionar_conta)
        self.button_selecionar.pack()

    def selecionar_conta(self):
        tipo_conta = self.combobox_tipo_conta.get()
        if tipo_conta:
            self.destroy()
            saque_frame = SaqueFrame(self.master, tipo_conta)
            saque_frame.pack()


class DepositoFrame(tk.Frame):
    def __init__(self, parent, tipo_conta):
        super().__init__(parent)

        self.tipo_conta = tipo_conta

        self.label_conta = tk.Label(self, text="Selecione a conta:")
        self.label_conta.pack()
        self.combobox_conta = ttk.Combobox(self, values=self.obter_contas(), state="readonly")
        self.combobox_conta.pack()

        self.label_valor = tk.Label(self, text="Valor:")
        self.label_valor.pack()
        self.entry_valor = tk.Entry(self)
        self.entry_valor.pack()

        self.button_depositar = tk.Button(self, text="Depositar", command=self.depositar)
        self.button_depositar.pack()

    def obter_contas(self):
        if self.tipo_conta == "Corrente":
            return [f"ID: {conta.id} - Titular: {conta.titular}" for conta in ContaCorrente.obter_contas_corrente()]
        elif self.tipo_conta == "Poupança":
            return [f"ID: {conta.id} - Titular: {conta.titular}" for conta in ContaPoupanca.obter_contas_poupanca()]

    def depositar(self):
        id_conta = int(self.combobox_conta.get().split()[1])
        valor = float(self.entry_valor.get())

        if self.tipo_conta == "Corrente":
            contas = ContaCorrente.obter_contas_corrente()
        else:
            contas = ContaPoupanca.obter_contas_poupanca()

        for conta in contas:
            if conta.id == id_conta:
                if conta.status == "Encerrada":
                    messagebox.showerror("Erro", "Conta encerrada. Não é possível realizar depósitos.")
                    return

                conta.depositar(valor)
                messagebox.showinfo("Depósito", "Depósito realizado com sucesso!")
                self.entry_valor.delete(0, tk.END)
                self.combobox_conta.set("")
                return

        messagebox.showerror("Erro", "Conta não encontrada.")

class DepositoHome(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label_tipo_conta = tk.Label(self, text="Selecione o tipo de conta:")
        self.label_tipo_conta.pack()
        self.combobox_tipo_conta = ttk.Combobox(self, values=["Corrente", "Poupança"], state="readonly")
        self.combobox_tipo_conta.pack()

        self.button_selecionar = tk.Button(self, text="Selecionar", command=self.selecionar_conta)
        self.button_selecionar.pack()

    def selecionar_conta(self):
        tipo_conta = self.combobox_tipo_conta.get()
        if tipo_conta:
            self.destroy()
            deposito_frame = DepositoFrame(self.master, tipo_conta)
            deposito_frame.pack()

class TransferenciaFrame:
    def __init__(self, root):
        self.root = root

        self.label_conta_origem = tk.Label(self.root, text="Conta de Origem:")
        self.label_conta_origem.pack()
        lista_contas = self.obter_lista_contas()
        self.combobox_conta_origem = ttk.Combobox(self.root, values=lista_contas, state="readonly")
        self.combobox_conta_origem.pack()

        self.label_conta_destino = tk.Label(self.root, text="Conta de Destino:")
        self.label_conta_destino.pack()
        self.combobox_conta_destino = ttk.Combobox(self.root, values=lista_contas, state="readonly")
        self.combobox_conta_destino.pack()

        self.label_valor = tk.Label(self.root, text="Valor:")
        self.label_valor.pack()
        self.entry_valor = tk.Entry(self.root)
        self.entry_valor.pack()

        self.button_transferir = tk.Button(self.root, text="Transferir", command=self.transferir)
        self.button_transferir.pack()

    def obter_lista_contas(self):
        contas = []
        bancos = Banco.listar_bancos()
        for banco in bancos:
            for conta in banco._contas:
                contas.append(f"ID: {conta._num} - Titular: {conta._titular._nome} - Banco: {banco._nome}")
        return contas

    def transferir(self):
        id_conta_origem = int(self.combobox_conta_origem.get().split()[1])
        id_conta_destino = int(self.combobox_conta_destino.get().split()[1])
        valor = float(self.entry_valor.get())

        conta_origem = self.obter_conta_por_id(id_conta_origem)
        conta_destino = self.obter_conta_por_id(id_conta_destino)

        if conta_origem is None or conta_destino is None:
            messagebox.showerror("Erro", "Conta de origem ou conta de destino não encontrada.")
        elif conta_origem.status == "Encerrada":
            messagebox.showwarning("Atenção", "Não é possível transferir de uma conta Encerrada.")
        elif conta_destino.status == "Encerrada":
            messagebox.showwarning("Atenção", "Não é possível transferir de uma conta Encerrada.")
        else:
            if conta_origem.transfere(conta_destino, valor):
                messagebox.showinfo("Transferência", "Transferência realizada com sucesso!")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente para realizar a transferência.")

    def obter_conta_por_id(self, id_conta):
        bancos = Banco.listar_bancos()
        for banco in bancos:
            for conta in banco._contas:
                if conta._num == id_conta:
                    return conta
        return None