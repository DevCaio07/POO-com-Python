# a herança permite que uma classe utilize atributos de outras classes
# sendo uma especie de filha da classe principal 

class Animal: 
    def __init__(self, raca, tamanho, nome):
        self.raca = raca 
        self.tamanho = tamanho 
        self.nome = nome 


def Dormir(self): #Funcao dizendo que faz o cachorro dormiu  
    return f"O {self.nome} esta dormindo "


class Cachorro(Animal): 
    pass

class Gato(Animal): 
    pass 

rex = Cachorro("Rex")
print(rex.dormir())
