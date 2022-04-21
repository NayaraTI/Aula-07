## Associar e vincular uma classe com a outra

class Livro():
    def __init__(self,nome):
        self.nome= nome
        self.__editora= None
        self.__autor= None
        
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self,editora):
        self.__editora= editora
        
    @property
    def autor(self):
        return self.__autor
        
    @autor.setter
    def autor(self,autor):
        self.__autor= autor
        
        

class Editora():
    
    def insereeditora(self,insereeditora):
        print(f'Essa é a Editora: {insereeditora}')
        



class Autor():
    
    def insereautor(self,insereautor):
        print(f'Esse é o Autor: {insereautor}')
        
        
# Instanciar os objetos

l1= Livro('O Pequeno Príncipe')
aut1= Autor()
ed1= Editora()
l1.editora= ed1
l1.autor= aut1

l1.editora.insereeditora('Editora das Contas')
l1.autor.insereautor('O autor que não lembro')
print(l1.nome)




########### Agregação trabalha com a junção de partes de classe
#chamadas objet-parte onde juntas forma o objeto-todo


## Compra frutas e Frutas


class CompraFrutas():
    def __init__(self):
        self.frutas= []
        
    def inserir_frutas(self,frutas):
        self.frutas.append(frutas)
        
    def lista_frutas(self):
        for frutas in self.frutas:
            print(frutas.nome)
            
    def soma_frutas(self):
        total_valor= 0
        for frutas in self.frutas:
            total_valor +=frutas.valor
        return total_valor
    
    
class Frutas():
    def __init__(self,nome,valor):
        self.nome= nome
        self.valor = valor
        
        
## Instanciar os Objetos

cestafrutas = CompraFrutas()

fruta1= Frutas('Maçã',10)
fruta2= Frutas('Morango',30)

cestafrutas.inserir_frutas(fruta1)
cestafrutas.inserir_frutas(fruta2)

cestafrutas.lista_frutas()

print(cestafrutas.soma_frutas())



####### A Composição é uma variação da agregação,
#Porém a classe pai(principal) se encarrega
#da tratativa dos objetos
# Caso o objeto for removido, ele remove todos os vínculos desse objeto(GARBAGE COLLETOR)

class RegistroSetor():
    def __init__(self,setor,funcao):
        self.setor= setor
        self.funcao= funcao
        self.funcionarios = []
        
    def insere_funcionarios(self,nome,sobrenome):
        self.funcionarios.append(Funcionarios(nome,sobrenome))
        
    def lista_funcionario(self):
        for funcionarios in self.funcionarios:
            print(funcionarios.nome,funcionarios.sobrenome,self.funcionarios)
            
    def __del__(self):
        print('Apagou da Classe Setor')
        
    
            
class Funcionarios():
    def __init__(self,nome,sobrenome):
        self.nome= nome
        self.sobrenome= sobrenome
        
    def __del__(self):
        print('Apagou da Classe Funcionarios')
        
        
## Instanciar os objetos

func1= RegistroSetor('Faturamento','Analista')
func1.insere_funcionarios('João','Cavichiolli')
print(func1.setor)
func1.lista_funcionario()


    