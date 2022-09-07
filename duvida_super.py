class Animal:
    def __init__(self,nome):
        pass

class Cachorro(Animal):
    def __init__(self, nome, raca):
        self.raca = raca
        super().__init__(nome)

print(Animal.Cachorro("Symon", "xitsu"))