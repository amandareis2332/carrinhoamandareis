import math

#Crie uma classe que modele um quadrado

class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def trocaLado(self, lado):
        self.lado = lado

    def mostraLado(self):
        print("Meu lado e %s" % self.lado)

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado * self.lado

quad = Quadrado(2)
quad.mostraLado()
quad.trocaLado(3)
quad.mostraLado()
print ("Perimetro: %i Area: %i" % (quad.perimetro(), quad.area()))

