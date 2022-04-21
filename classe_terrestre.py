########## 2 Classe Filha ############

from classe_animal import Animal


class Terrestre(Animal):
    def __init__(self,especie):
        super().__init__(especie)
        
    def tipo(self):
        print(f'É da espécie {self.especie} que anda na terra')