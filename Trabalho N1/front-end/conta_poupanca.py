from conta import Conta

class ContaPoupanca(Conta):
    _lista_contas_poupanca = []
    
    def __init__(self, cli, sal, banco):
        super().__init__(cli, sal, banco)
        ContaPoupanca._lista_contas_poupanca.append(self)

    def atualiza(self, taxa):
        valor = self._saldo * taxa * 3
        self.depositar(valor)
        return valor
    
    @classmethod
    def obter_contas_poupanca(cls):
        return cls._lista_contas_poupanca