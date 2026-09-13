# metodo super() da acesso a classe pai a partir de dentro da classe filho 
 
class Funcionario: 
    def __init__(self, salario, nome):
        self._salario = salario
        self.nome = nome 


class DesenvolvedordeSoft(Funcionario): 
    def __init__(self, salario, nome, linguagemprincipal):
        super().__init__(salario, nome) # O super me da acesso aos atributos da classe Funcionario
        self.linguagemprincipal = linguagemprincipal

dev = DesenvolvedordeSoft("Ana", 2000, "Java") 
print(dev.nome, dev._salario, dev.linguagemprincipal)
