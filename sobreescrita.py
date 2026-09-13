# a Sobreescrita acontece quando uma classe filha
#redefine um metodo que ja existe na classe pai (ela fica por cima do metodo principal)

class Animal: 
    def emitir_som(self): 
        return "Som generico"

class Cachorro(Animal): 
    def emitir_som(self): 
        return "au au"


print(Cachorro().emitir_som())