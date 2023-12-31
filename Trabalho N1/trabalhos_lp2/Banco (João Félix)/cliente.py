from functools import reduce
class Cliente:

    __slots__ = ['_nome','_endereco', '_titular', '_CPF', '_idade']

    def __init__(self, n, e, cpf, i):
        self._nome = n
        self._endereco = e
        self._CPF = Cliente.validarCPF(cpf) #mudar para o segundo metodo troca para validarCPF2
        self._idade = i

        

        
    @property
    def CPF(self):
        return self._CPF
    
    @CPF.setter
    def CPF(self, valor):
        self._CPF = valor
    def get_nome(self):
        return self._nome
        
    def validarCPF(cpf):
        while True:
            
            original = cpf
            cpf = list(cpf)
            cpf = reduce(lambda x,y: x+y, [n for n in cpf if n.isdigit()])
            cpf2 = cpf[:9]

            verificador = reduce(lambda x,y: x+y, [int(cpf[(10-i)])*i for i in range(10,1,-1)])%11
            cpf2 += '0' if verificador < 2 else str(11-verificador)
            
            verificador = reduce(lambda x,y: x+y, [int(cpf2[(11-i)])*i for i in range(11,1,-1)])%11 
            cpf2 += '0' if verificador < 2 else str(11-verificador)

            if (cpf == cpf2):
                print("CPF valido")
                return original
            else:
                print("CPF invalido para criar a conta")
                print("Entre com outro CPF")
                cpf = input()

    def validarCPF2(cpf):
        while True:
            num = ['0',"1",'2','3','4','5','6','7','8','9']
            original = cpf
            cpf = [int(i) for i in cpf if i in num]
            cpf2 = cpf.copy()
            cpf = [cpf[i] for i in range(9)]
            
            verificador = [cpf[i]*(10-i) for i in range(len(cpf))]
            verificador = reduce(lambda x, y: x+y,verificador)

            if verificador%11 < 2:
                cpf.append(0)
            else:
                cpf.append(11-(verificador%11))

            verificador = [cpf[i]*(11-i) for i in range(len(cpf))]
            verificador = reduce(lambda x, y: x+y,verificador)

            if verificador%11 < 2:
                cpf.append(0)
            else:
                cpf.append(11-(verificador%11))

            if (cpf == cpf2):
                print("CPF valido")
                return original
            else:
                print("CPF invalido para criar a conta")
                print("Entre com outro CPF")
                cpf = input()




