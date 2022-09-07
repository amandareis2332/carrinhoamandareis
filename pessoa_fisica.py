class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

class PF(Pessoa):

    def __init__(self, CPF, nome, idade):
        self.CPF = CPF
        super().__init__(nome, idade)
    def getCPF(self):
        return self.CPF

    def setCPF(self, CPF):
        self.CPF = CPF
    
a= PF("1111111", "Gabriel", "15")
print(a.getCPF())
print(a.getNome())
print(a.getidade())

class PJ(Pessoa):
    def __init__(self, CNPJ, nome, idade):
        super().__init__(nome, idade)
        self.CNPJ = CNPJ

    def getCNPJ(self):
        return self.CNPJ

    def setCNPJ(self, CNPJ):
        self.CNPJ = CNPJ
    

