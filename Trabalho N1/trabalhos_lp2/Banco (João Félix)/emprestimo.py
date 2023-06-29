from datetime import date, datetime
from dateutil.relativedelta import relativedelta
class Emprestimo:
    _total_emprestimos = 0 
    __slots__ = ['_valor','_parcelas', '_juros', '_conta','_valor_pacela', '_dia']
    def __init__(self,valor,parcelas,conta,juros=0.05 ): #juros simples padrao 5% ao mes 
        
        self._dia = date.today()
        self._valor = valor
        self._parcelas = parcelas
        self._juros = juros
        self._conta = conta
        self._valor_pacela = ((valor+valor*juros*parcelas)/parcelas)
        self._conta.depositar(self._valor, True)
        
        Emprestimo._total_emprestimos += 1
        #e) Controlar e informar a quantidade de empréstimos realizados.
    @classmethod
    def get_total_emprestimos(cls):
        return Emprestimo._total_emprestimos
    
    @property
    def parcelas(self):
        return self._parcelas

    @parcelas.setter
    def parcelas(self, valor):
        self._parcelas = valor
                                                            #c) Controlar e informar o número e o valor das parcelas;
    @property
    def valor_pacela(self):
        return self._valor_pacela
    
    @valor_pacela.setter
    def valor_pacela(self, valor):
        self._valor_pacela = valor

    def prox_pacela(self): #dia da proxima parcela
        if self._dia < self._dia + relativedelta(months=+1):
            aux = self._dia + relativedelta(months=+1)
            aux = datetime.strftime(aux,"%d/%m/%Y")
            print(f"Proxima parcela da conta {self._conta.get_numero()}: {aux}") 
        else:
            print("pacela atrasada pague logo")


    def total(self):
        print(f"conta {self._conta.get_numero()} devendo: {self.valor_pacela*self.parcelas}")

    def info_parcelas(self):
        if self.parcelas > 1:
            print(f"Falta {self.parcelas} Pacelas no valor de {self.valor_pacela:.2f} cada")
        elif self.parcelas == 1:
            print(f"Falta {self.parcelas} Pacela no valor de {self.valor_pacela:.2f}")


    def pagar(self):
        if self._conta.sacar(self.valor_pacela, False, True):
            self.parcelas -= 1
            self._dia = self._dia + relativedelta(months=+1)
            print("parcela paga")
            print(f'Seu saldo atual é de: {self._conta.get_saldo()}')
            self.info_parcelas()
            self.prox_pacela()
            if self.parcelas == 0: #verifica se tem alguma parcela pedente 
                self.valor_pacela = 0
                Emprestimo._total_emprestimos -= 1 #e) Controlar e informar a quantidade de empréstimos realizados.