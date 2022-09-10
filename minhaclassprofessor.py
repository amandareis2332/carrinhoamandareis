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
            print("OK")
            return True
        else:
           print("Não é permitido")
           return False


class Professor(Funcionario):
    materia: str
    def __init__(self, nome, idade,  materia):
        super().__init__(self, nome, idade, salario)
        self.materia = materia
        return 

       
funcionario = Funcionario('João', '111111111-11', 2000.0)
print(vars(funcionario))
        
cordenador = Cordenador("Kelly", "5555555", 5000.0, "1234",7)
print(vars(cordenador))
print(cordenador.get_bonificacao())

professor = Funcionario("Amanda", 32,"matematica")
print(vars(professor))