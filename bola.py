#Crie uma classe que modele uma bola:
import math
class Bola:

    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio


    def trocaCor(self, cor):
        self.cor = cor


    def mostraCor(self):
        print ("Minha cor e %s" % self.cor)


    def area(self):
        return 4 * math.pi * self.raio * self.raio


    def volume(self):
        return (4 * math.pi * (self.raio ** 3)) / 3

bola = Bola("azul", 2)
bola.mostraCor()
bola.trocaCor("verde")
bola.mostraCor()
print ("Area: %f Volume: %f" % (bola.area(), bola.volume()))
