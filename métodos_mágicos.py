
## Método __repr__

class Pessoa():
    def __init__(self,nome,sobrenome,rg):
        self.nome= nome
        self.sobrenone= sobrenome
        self.rg= rg
        
    def __repr__(self):
        return self.nome
    
    
#Instanciar

p1= Pessoa('João','Silva',444)

print(p1)
        