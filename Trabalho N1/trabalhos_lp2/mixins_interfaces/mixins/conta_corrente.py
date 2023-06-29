from conta import Conta
from tributavel import TributavelMixIn


class ContaCorrente(Conta,TributavelMixIn):
    
    def __init__(self, cli, sal):
        super().__init__(cli, sal)

    def valor_imposto(self):
        return self._saldo *0.02
    
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor
    