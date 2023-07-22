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
            conta

    @classmethod
    def incluir_conta(cls, id, conta):
        bancos = Banco.listar_bancos()
        for banco in bancos:
            if(id == banco._num):
                banco._contas.append(conta)

    @classmethod
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

    @classmethod
    def remover_banco(cls, id):
        bancos = cls.listar_bancos()
        for banco in bancos:
            if banco._num == id:
                if len(banco._contas) == 0:
                    print(len(banco._contas))
                    Banco._lista_bancos.remove(banco)
                    return True
                else:
                    return False

    def __str__(self):
       return self._nome
