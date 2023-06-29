class Banco:
    _total_banco = 0
    def __init__(self, nome):
        self._num = Banco._total_banco + 1
        self._nome = nome
        self._contas = []
        self._caixa_geral = 0
        Banco._total_banco += 1

    def listar_contas(self):
        for i in self._lista_contas:
            print(i)
            i.extrato()

    def incluir_conta(self, conta):
        self._lista_contas.append(conta)

    def remover_conta(self, conta):
        self._lista_contas.remove(conta)