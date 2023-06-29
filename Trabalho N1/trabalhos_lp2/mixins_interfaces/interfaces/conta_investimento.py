from conta import Conta

class ContaInvestimento(Conta):
    
    def __init__(self, cli, sal):
        super().__init__(cli, sal)

    def valor_imposto(self):
        return self._saldo * 0.03