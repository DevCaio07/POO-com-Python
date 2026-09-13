# Abstracao é o pilar de esconder detalhes de implementacao e expor apenas 
# o nescessario para quem vai usar aquele objeto 

from abc import ABC, abstractmethod # ABC = Abstract Base Class 

class Animal(ABC): 
    @abstractmethod
    def emitir_som(self): 
        pass


class cachorro(Animal): 
    def emitir_som(self): 
        return "au au"

class cat(Animal): 
    def emitir_som(self): 
        return "miau miau"

    Cachorro = cachorro()
    print(cachorro.emitir_som)          