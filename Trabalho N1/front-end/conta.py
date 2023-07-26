import abc
import datetime
from historico import Historico


class Conta(abc.ABC):
    _lista_contas = []
    _taxa_base = 0.3
    _total_contas = 0
    def __init__(self, cli, sal):
        self._num = Conta._total_contas + 1
        self._id = Conta._total_contas + 1 
        self._titular = cli
        self._saldo = sal
        self._extrato = Historico()
        Conta._total_contas += 1
        self._status = "Ativa"
        Conta._lista_contas.append(self)


    @classmethod
    def atualiza_taxa(cls, taxa):
        Conta._taxa_base = taxa


    def atualiza(self, taxa):
        pass

    # def encerrar_conta(self):

    #     if self._saldo == 0:
    #         self._status = False
    #     elif self._saldo > 0:
    #         print(f'Vc pode sacar {self._saldo}')
    #     else:
    #         print(f'Vc precisa depositar {self._saldo}')

    #Método get para o status das contas
    @property
    def status(self):
        return self._status

    #Métodos de acesso
    #Acesso para o atributo de classe
    #@staticmethod #Primeira forma
    @classmethod #Segunda forma
    def get_total_contas(cls):
        return Conta._total_contas

    @property #Método getter
    def saldo(self):
        return self._saldo

    @property #Método getter
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    def get_numero(self): #Método getter
        return self._numero

    #Não faz sentido um set para o saldo, pois já temos sacar e depositar

    #Comportamentos
    def sacar(self, valor):
        if self.status:
            if self._saldo < valor:
                return False
            else:
                self._saldo -= valor
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._extrato.adicionar_transacao(data, "Saque", valor, self._saldo)
                return True
        else:
            print('Conta inativa não pode realizar saques')


    def depositar(self, valor):
        if self.status:
            self._saldo += valor
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._extrato.adicionar_transacao(data, "Depósito", valor, self._saldo)
        else:
            print('Conta inativa não pode realizar depósitos')
            
    def transfere_saida(self, valor):
        if self.status:
            if self._saldo < valor:
                return False
            else:
                self._saldo -= valor
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._extrato.adicionar_transacao(data, "Transferência - Saída", valor, self._saldo)
                return True
        else:
            print('Conta inativa não pode realizar saques')
            
    def transfere_entrada(self, valor):
        if self.status:
            self._saldo += valor
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._extrato.adicionar_transacao(data, "Transferência - Entrada", valor, self._saldo)
        else:
            print('Conta inativa não pode realizar depósitos')

    def transfere(self, c_destino, valor):
            if self.status and c_destino.status:
                if self.transfere_saida(valor):
                    c_destino.transfere_entrada(valor)
                    return True
                else:
                    print('Saldo insuficiente para realizar a transferência')
                    return False
            else:
                print('Conta inativa não pode realizar transferências')
                return False

    def extrato(self):
        self._extrato.imprime()

    def __str__(self):
        return f'{self.__class__.__name__} {self._num}: {self._titular} Saldo:{self._saldo}'
    
    # Encerrar uma conta
    @classmethod
    def encerrar_conta(cls, id):
        for conta in cls._lista_contas:
            if conta._num == id:
                if conta._status == "Ativa":
                    if conta._saldo == 0.0:
                        conta._status = "Encerrada"
                        return True
                    else:
                        print("Não é possível encerrar a conta. O saldo não está zerado.")
                        return False
                else:
                    return "Encerrada"
    @classmethod
    def ativar_conta(cls, id):
        for conta in cls._lista_contas:
            if conta._num == id:
                if conta._status == "Encerrada":
                    conta._status = "Ativa"
                    return True
                else:
                    return False
    
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, value):
        self._titular = value
        
    @property
    def banco(self):
        return self._banco
    
    @banco.setter
    def banco(self, value):
        self._banco = value
        
    @property
    def id(self):
        return self._id
    
    @classmethod
    def verificar_conta_vinculada(cls, cli):
        for conta in cls._lista_contas:
            if conta.titular == cli:
                return True
        return False
    
    @classmethod
    def remover_conta(cls, conta):
        if conta in cls._lista_contas:
            cls._lista_contas.remove(conta)