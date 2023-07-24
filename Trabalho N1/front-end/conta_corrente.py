from conta import Conta

class ContaCorrente(Conta):
    _lista_contas_corrente = []
    _taxa_desconto = 0.1
    
    def __init__(self, cli, sal):
        super().__init__(cli, sal)
        ContaCorrente._lista_contas_corrente.append(self)

    def valor_imposto(self):
        return self._saldo *0.02
    
    def atualiza(self, taxa):
        valor_juros = self._saldo * taxa
        self._saldo += valor_juros
        return valor_juros
    
    def sacar(self, valor):
        if self.status:
            valor_desconto = valor * self._taxa_desconto
            valor_liquido = valor + valor_desconto
            print(valor_desconto)
            if self._saldo < valor_liquido:
                return False
            else:
                super().sacar(valor_liquido)
                return True
        else:
            print('Conta inativa não pode realizar saques')

    def depositar(self, valor):
        if self.status:
            valor_desconto = valor * self._taxa_desconto
            valor_liquido = valor - valor_desconto
            super().depositar(valor_liquido) 
        else:
            print('Conta inativa não pode realizar depósitos')
    
    @classmethod
    def obter_contas_corrente(cls):
        return cls._lista_contas_corrente