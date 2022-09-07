class Heroi:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def set_nome():
        self.nome = novo_nome

    def get_nome(self):
        return self.nome
    
    def skill (self):
        return "nao tem poder"

class HomemAranha(Heroi):
    def __init__(self,nome,idade, cidade):
        self.cidade = cidade
        super().__init__(nome, idade)

class Flash (Heroi):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

class Batman (Heroi):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

heroi1 = HomemAranha("Peter Park", "18", "NY")
heroi1.set_nome()
print("poder homem aranha", heroi1.skill)


heroi2 = Flash(("Realen"),"30anos")
print("o poder do flash é:", heroi2.skill)


