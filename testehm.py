class A1():
    def __init__(self,nome):
        self.nome = nome
    
    def metodo1():
        print("Estou executando da classe A1")

    def metodo3():
        print("Estou executando da Classe A1")

class A2(A1):
    def __init__(self,nome):
        self.nome = nome 
    
    def metodo2 ():
        print("Estou executando da Classe A2")


class A3(A1):
    def __init__(self,nome):
        self.nome = nome 
    
    def metodo3 ():
        print("Estou executando da Classe A3")

class A4(A2,A3):
    def __init__(self,nome):
        self.nome = nome 
    
  

teste = A4.metodo1()


## Uma classe que possui herança multipla irá sempre buscar utilizar
# Atributos das classes com herança direta. Senão achar irá procurar nas 
# classe de herança indireta.