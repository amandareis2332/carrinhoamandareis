class RH:
    def __init__(self, funcao):
        self.funcao = funcao

    def _salario(self):
        return "Somente os adm podem ver"
    
    def holerite(self):
        return "Todo mundo podem ver"
    
    def ver_salario(self, responsavel):
        if responsavel == "taci" and self.funcao == "ADM":
            return self._salario()
        return "nao ver"
        
taci = RH("ADM")
print(taci.funcao)

fulano = RH("DEV")
salario_fulano = fulano.ver_salario("taci")
print(salario_taci)

    