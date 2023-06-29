from conta_corrente import ContaCorrente
from seguro_de_vida import SeguroDeVida
from manipulador import ManipuladorDeTributaveis

#1) class Tributavel feita

#2) class ContaCorrrente herdou da class TributavelMixIn e seu metodo implementado

#3)
cc1 = ContaCorrente("João Félix", 1000)
cc2 = ContaCorrente("Amanda", 10000)
sdv = SeguroDeVida(1000, "josé")
print("imposto da conta corrente 1")
print(cc1.valor_imposto())
print("imposto da conta corrente 2")
print(cc2.valor_imposto())
print("imposto do seguro de vida 1")
print(sdv.valor_imposto(),end="\n\n")


#4)
print("Total de impostos cobrados")
lista = []
lista.append(cc1)
lista.append(cc2)
lista.append(sdv)

manipulador = ManipuladorDeTributaveis()
print(manipulador.calcular_imposto(lista))


