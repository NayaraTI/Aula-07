######### Classes Abstratas não permitem que sejam instanciados objetos
# a partir delas. Elas servem para ser como modelo para suas
# classes derivativas(filhas)
# Por regras os métodos dessa classe deverão ser sobrescritos nas clases filhas(polimorfismo)

# para criar uma classe abstrata preciso que ela seja importada da classe ABC

from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,tipo,especie):
        self._tipo= tipo
        self.especie= especie
        
    @abstractmethod
    def raca(self):
        pass
    
    
## Tentando instanciar uma classe abstrata

#an= Animal('Mamífero','Baleia')
#print(an1.especie)