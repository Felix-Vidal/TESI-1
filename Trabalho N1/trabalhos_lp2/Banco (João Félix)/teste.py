from cliente import Cliente
from conta import Conta
from banco import Banco
from emprestimo import Emprestimo


#Q1
#python não tem atributos privados para privar variáveis mas podemos colocar Underline para informar as pessoas envolvidas no projeto 
#para não manipular as variáveis de qualquer maneira mas sim dentro de da propria class, dentro da propria class manipulamos adicionando o Underline na variável
#ja fora (jeito errado de manipular) de que add A class e o Underline

#Q2.1 tem ValidarCPF(cpf) validarCPF2(cpf) precisa entra na classe cliente para trocar 
cli1 = Cliente("João Félix", 'Rua não sei','111.444.777-35',20)
cli2 = Cliente("João ", 'Rua não sei','111.444.777-35',18)
cli3 = Cliente("Félix", 'Rua não sei','111.444.777-35',21)
print()

#Q2.2 encerrar uma conta específica.
c1 = Conta(cli1,0)
c1.depositar(100)
c1.encerrarConta()
c1.sacar(100)
c1.encerrarConta() #encerrar conta
c1.sacar(100) #com a conta encerrada não tem como usar as fucções
c1.ativaConta() #ativar conta
print()

#Q3
print (f"Total de Contas Ativas: {Conta.get_total_contas_ativas()}")

c2 = Conta(cli2,1000)

print (f"Total de Contas Ativas: {Conta.get_total_contas_ativas()}")

c3 = Conta(cli3,50)

print (f"Total de Contas Ativas: {Conta.get_total_contas_ativas()}")
print (f'Total de contas: {Conta.get_total_contas()}')
print ()

#Q4
banco1 = Banco("Félix")

c2.sacar(500)
c3.depositar(5000)
c3.transfere(c2,3000)
banco1.incluir(c1)
banco1.incluir(c2)
banco1.incluir(c3)
banco1.remover(c1) #conta 1 não vai aparecer na listagem
banco1.listagem()
print()




#Q5
empre1 = Emprestimo(1200,14,c2) #juros é opcional mas se quiser altera coloque na quarta pocição
empre2 = Emprestimo(5000,32,c3)
empre1.prox_pacela()
empre2.prox_pacela()

#A) taxa de juros ta definida no __init__ como 5%

#B)
empre1.total()
empre2.total()
print()

#C)
empre1.info_parcelas()
print()

#D)
empre1.pagar()

empre2.pagar()
empre2.pagar()

print()

#E)
print(f'Total de emprestimos: {Emprestimo.get_total_emprestimos()}')
print()

#Q6 feito o __slot__ em todas as classes


#Q7 teste.py
banco1.listagem()