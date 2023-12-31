from conta import Conta
from banco import Banco

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
            valor_liquido2 = self._saldo / (1 + valor_desconto)
            if self._saldo < valor_liquido:
                if self._saldo > valor_liquido2:
                    return super().sacar(self.saldo)
            else:
                return super().sacar(valor_liquido)
        else:
            print('Conta inativa não pode realizar saques')

    @classmethod
    def verificar_conta_unica(cls, cpf, id_banco):
        banco = Banco.id_get(id_banco)
        for contas in banco._contas:
            if isinstance(contas, ContaCorrente):
                if contas._titular._CPF == cpf:
                    return False
        return True
            
                

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