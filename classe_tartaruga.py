######## Classe que vai Instanciar os Objetos ######
# E vai receber as heranças múltiplas #

from classe_aquatico import Aquatico

from classe_terrestre import Terrestre


class Tartaruga(Aquatico,Terrestre):
    def __init__(self,especie):
        super().__init__(especie)