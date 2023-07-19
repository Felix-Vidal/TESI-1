from conta import Conta

class ContaCorrente(Conta):
    _lista_contas_corrente = []
    
    def __init__(self, cli, sal, banco):
        super().__init__(cli, sal, banco)
        ContaCorrente._lista_contas_corrente.append(self)

    def valor_imposto(self):
        return self._saldo *0.02
    
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor
    
    @classmethod
    def obter_contas_corrente(cls):
        return cls._lista_contas_corrente