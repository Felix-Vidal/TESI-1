from conta import Conta

class ContaPoupanca(Conta):
    
    def __init__(self, cli, sal):
        super().__init__(cli, sal)

    def atualiza(self, taxa):
        valor = self._saldo * taxa * 3
        self.depositar(valor)
        return valor