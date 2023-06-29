from historico import Historico
class Conta:

    _total_contas = 0
    _total_contas_ativas = 0
    _taxa_base = 0.03

    __slots__ = ['_ativo','_numero', '_titular', '_saldo', '_limite', '_historico',"_taxa"]

    def __init__(self,cli,sal,lim=0):
            self._ativo = True
            self._numero = Conta._total_contas + 1
            self._titular = cli
            self._saldo = sal
            self._limite = lim
            self._taxa = Conta._taxa_base
            self._historico = Historico()
            Conta._total_contas += 1
            Conta._total_contas_ativas += 1


    #Métodos de acesso
    @classmethod 
    def get_total_contas(cls):   #total de contas ja criadas
        return Conta._total_contas

    @classmethod 
    def get_total_contas_ativas(cls):  #total de contas ativas 
        return Conta._total_contas_ativas

    @property 
    def limite(self): #visualizar limite
        return self._limite

    @limite.setter
    def limite(self, valor): #modificar limite 
        self._limite = valor

    def get_numero(self):    #visualizar Numero
        return self._numero

    def get_saldo(self):     #visualizar saldo
        return self._saldo

    #Comportamentos

    def atualiza(self):
        self._saldo -= self._saldo - Conta._taxa_base

    def encerrarConta(self):
        if (self._ativo): 
            if self._saldo == 0:
                self._ativo = False                         
                Conta._total_contas_ativas -= 1
                print("Conta encerrada com sucesso")
            else:
                print("tire seu dinheiro antes de encerrar sua conta")
        else:
            print("Essa conta ja foi encerrada")

    def ativaConta(self):
        if (self._ativo == False):
            self._ativo = False    
            Conta._total_contas_ativas += 1
            print("Conta ativada")
        else:
            print("Essa conta ja ta Ativa")



    def sacar(self, valor, transf=False, empres = False):
        if (self._ativo): #verifica se a conta não foi encerrada
            if self._saldo < valor:
                return False
            else:
                if transf: #verifica se o pedido vem de um transferência
                    self._saldo = self._saldo - valor
                    return True
                else:
                    if empres: #verifica se o pedido vem de um emprestimo
                        self._saldo = self._saldo - valor
                        self._historico.transacoes.append(f'Pacela paga no valor de {valor:.2f}')
                        return True
                    else:
                        self._saldo = self._saldo - valor
                        self._historico.transacoes.append(f'Saque de {valor:.2f}')
                        return True
        else:
            print("Você não pode sacar porque esse conta esta encerrada!")



    def depositar(self, valor, empres=False):
        if (self._ativo): #verifica se a conta não foi encerrada
            if (empres):  #verifica se o pedido vem de um emprestimo
                self._saldo += valor
                self._historico.transacoes.append(f'Realizado um emprestimo de {valor:.2f}')
            else:
                self._saldo += valor
                self._historico.transacoes.append(f'Depósito de {valor:.2f}')
        else:
            print ("Você não pode depositar porque essa conta esta encerrada!")



    def transfere(self, c_destino, valor):
        if(self._ativo and c_destino._ativo): #verifica se as contas não foi encerrada
            if self.sacar(valor,True):
                c_destino.depositar(valor)
                self._historico.transacoes.append(f'Enviou uma Tranferência de {valor:.2f}')
                c_destino._historico.transacoes.append(f'Recebeu uma Tranferência de {valor:.2f}')
        else:
            print("Você não pode transferir porque essa conta esta encerrada!")



    def extrato(self, banco = False): 
        if (self._ativo): #verifica se a conta não foi encerrada
            print(f"Extrato da Conta {self._numero}")
            self._historico.imprime()
        else:
            if (banco): #vefica se o pedido vem do banco
                print(f"Extrato da Conta {self._numero}")
                self._historico.imprime()
            else:
                print("Você não pode ver o extrato dessa conta porque esta encerrada!")

    
    
    def __str__(self):
        return f'{self.__class__.__name__}  {self._numero}: {self._titular.get_nome()} Saldo:{self._saldo}'