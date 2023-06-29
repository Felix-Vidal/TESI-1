from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, cli, sal, lim=0):
        super().__init__(cli, sal, lim)

    def atualiza(self):
        self._saldo -= self._saldo * Conta._taxa_base*3