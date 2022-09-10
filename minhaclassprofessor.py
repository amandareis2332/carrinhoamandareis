class Funcionario:

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def get_bonificacao(self):
        return self.salario * 0.15

class Cordenador(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qtd_funcionarios = qtd_gerenciados


    def autentica(self, senha):
        if self.senha == senha:
            print("acesso permitido")
            return True
        else:
           print("acesso negado")
           return False
    
    

funcionario = Funcionario('João', '111111111-11', 2000.0)
print(vars(funcionario))
        
cordenador = Cordenador("Kelly", "5555555", 5000.0, "1234",7)
print(cordenador.get_bonificacao())
