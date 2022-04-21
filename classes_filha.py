## Uma classe que vai herdar de uma classe abstrata

from classes_abstratas import Animal

class Cachorro(Animal):
    def __init__(self,tipo,especie,cor):
        super().__init__(tipo,especie)
        self.cor= cor
        
##  Você é obrigado a sobrepor um método abstrato

    def raca(self,raca):
        return self.raca