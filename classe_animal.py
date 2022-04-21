############################# Super Classe #############################33

class Animal():
    def __init__(self,especie):
        self.especie= especie
        
    def tipo(self):
        print(f'É da espécie {self.especie}')
    
    def som(self):
        print(f'A {self.especie} não faz som')