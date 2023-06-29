class Banco:
    _total_bancos = 0
    __slots__ = ['_num','_nome', '_contas']
    def __init__(self, nome):
        self._num = Banco._total_bancos + 1
        self._nome = nome
        self._contas = []
        self._saldo_total = 0
        Banco._total_bancos += 1

    @property
    def contas(self):
        return self._contas
                                #controlar e informar lista de contas
    @contas.setter
    def contas(self, valor):
        
        self._contas = valor
        



    def incluir(self,conta):
        self.contas.append(conta)
        
    def remover(self, conta):
        self.contas.remove(conta)

    def atualizar_contas(self):
        print("saldo anterior")
        print(self._saldo_total)

        for i in self.contas:
            i.atualiza()

        print("Saldo atual")
        return self._saldo_total
    
    def listagem(self):
        soma = 0
        for i in range(len(self.contas)):
            print(self.contas[i])
            self.contas[i].extrato(True)
            soma += self.contas[i].get_saldo()

        print(f"total de saldo do Banco: {soma:.2f}")
            
     
            

        
            