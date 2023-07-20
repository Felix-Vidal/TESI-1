class Banco:
    _total_banco = 0
    _lista_bancos = []

    def __init__(self, nome):
        self._num = Banco._total_banco + 1
        self._nome = nome
        self._contas = []
        self._caixa_geral = 0
        Banco._total_banco += 1
        Banco._lista_bancos.append(self)

    def listar_contas(self):
        for conta in self._contas:
            print(conta)
            conta.extrato()

    def incluir_conta(self, conta):
        self._contas.append(conta)

    def remover_conta(self, conta):
        self._contas.remove(conta)

    @classmethod
    def listar_bancos(cls):
        bancos = [banco for banco in cls._lista_bancos]
        return bancos
    
    @classmethod
    def atualizar_banco(cls, id, nome):
        bancos = cls.listar_bancos()
        for banco in bancos:
            if(banco._num == id):
                banco._nome = nome

    def __str__(self):
       return self._nome
