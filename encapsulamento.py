#Encapsulamento é o principio de agrupar dados e metodos que os manipulam 
# Restringindo o acesso aos dados e obrigando qualquer alteracao a passar por metodos
# Cotrolados 

# Dado Publico: self.saldo 
# Protegido(Convencao): self._saldo (enfase no _) 
# Name mangling 

class contaBancaria:
    def __init__(self, titular, saldo_iniciaal=0,): 
        self.titular = titular
        self._saldo = saldo_iniciaal #convencao: uso interno 
        

@property
def saldo(self): 
    return self._saldo  #getter e setters sao utilizados para acessar atributos privados 


def depositar(self, valor): 
    if valor <= 0: 
        raise  ValueError("O deposito deve ser positivo")
    self._saldo += valor  

def sacar(self, valor): 
    if valor > self._saldo: 
        raise ValueError("Saldo insuficiente")
    self._saldo -= valor