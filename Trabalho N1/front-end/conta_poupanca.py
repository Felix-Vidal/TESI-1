from conta import Conta
from banco import Banco

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
    
    @classmethod
    def verificar_conta_unica(cls, cpf):
        for banco in Banco.listar_bancos():
            for contas in banco._contas:
                if isinstance(contas, ContaPoupanca):
                    if contas._titular._CPF == cpf:
                        return False
        return True