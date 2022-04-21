##################### 1 Classe Filha ####################

from classe_animal import Animal


class Aquatico(Animal):
    def __init__(self,especie):
        super().__init__(especie)
        
    def tipo2(self):
        print(f'É da Espécie {self.especie} que nada no mar')