# Polimorfismo é a capacidade do mesmo metodo ter comportamentos diferentes
# Dependendo de qual objeto esta sendo executado 

class Animal: 
    def emitir_som(self): 
        return "..."

class Cachorro(Animal): 
    def emitir_som(self): 
        return "au au" 

class Cat(Animal): 
    def emitir_som(self): 
        return "miau miau"

animals = [Cachorro(), Cat(), Cachorro()]

for Animal in animals: 
    print(animals.emitir_som)
    