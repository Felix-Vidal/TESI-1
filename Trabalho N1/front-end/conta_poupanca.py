from conta import Conta

class ContaPoupanca(Conta):
    _lista_contas_poupanca = []
    
    def __init__(self, cli, sal):
        super().__init__(cli, sal)
        ContaPoupanca._lista_contas_poupanca.append(self)

    def atualiza(self, taxa):
        valor = self._saldo * taxa
        self._saldo += valor
        return valor
    
    @classmethod
    def obter_contas_poupanca(cls):
        return cls._lista_contas_poupanca