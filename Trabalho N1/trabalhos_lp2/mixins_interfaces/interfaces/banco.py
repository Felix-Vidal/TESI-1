from tributavel import TributavelInterface


class Banco:
    _total_banco = 0
    def __init__(self, nome):
        self._num = Banco._total_banco + 1
        self._nome = nome
        self._contas = []
        self._caixa_geral = 0
        Banco._total_banco += 1
        self._total_impostos = 0

    def listar_contas(self):
        for i in self._lista_contas:
            print(i)
            i.extrato()

    def incluir_conta(self, conta):
        self._contas.append(conta)

    def remover_conta(self, conta):
        self._contas.remove(conta)
    
    def total_impostos(self,manipulador):
        lista_tributaves = []
        for i in self._contas:
            lista_tributaves.append(i)
    
        valor = manipulador.calcular_imposto(lista_tributaves)
        self._total_impostos += valor
        return  f"total de imposto ate agora: {self._total_impostos}"
        
