from conta_poupanca import ContaPoupanca
from banco import Banco
from tributavel import TributavelInterface
from conta_corrente import ContaCorrente
from seguro_de_vida import SeguroDeVida
from manipulador import ManipuladorDeTributaveis
from conta_investimento import ContaInvestimento

cc1 = ContaCorrente("João Félix", 1000)
cc2 = ContaCorrente("Amanda", 10000)
cp1 = ContaPoupanca("mandi", 300)
sdv = SeguroDeVida(1000, "josé")


#5) Torne Tributavel uma classe abstrata e o método valor_imposto() um método abstrato, ok.

#6)
#help(TributavelInterface)

#7)
TributavelInterface.register(ContaCorrente)
TributavelInterface.register(SeguroDeVida)

#8)
print("Total de impostos cobrados")
lista = []
lista.append(cc1)
lista.append(cc2)
lista.append(cp1)
lista.append(sdv)

manipulador = ManipuladorDeTributaveis()
print(manipulador.calcular_imposto(lista))

#9)
TributavelInterface.register(ContaInvestimento)
ci = ContaInvestimento("Bruno Perine", 50000)
lista.append(ci)
print(manipulador.calcular_imposto(lista))

#10) 
banco1 = Banco("BB")
banco1.incluir_conta(cc1)
banco1.incluir_conta(cc2)
banco1.incluir_conta(sdv)
banco1.incluir_conta(ci)
print(banco1.total_impostos(manipulador))
