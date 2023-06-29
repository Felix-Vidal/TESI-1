from contacorrente import ContaCorrente

class ContaEspecial(ContaCorrente):
    def __init__(self, cli, sal, lim=500):
        super().__init__(cli, sal, lim)


    def sacar(self, valor, transf=False, empres = False):
        if (self._ativo):
            if (self._saldo - valor)+ self.limite <= 0:
                return False
            else:
                self._saldo = self._saldo - valor
                self._historico.transacoes.append(f'Saque de {valor:.2f}')
                return True
        else:
            print("Você não pode sacar porque esse conta esta encerrada!")
        

            