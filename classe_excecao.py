## Utilizar uma classe para criar uma exceção (raise)

# A classe da exceção herda da classe padrão exception


class ErroProg(Exception):
    pass


def teste():
    raise ErroProg('Mensagem de Erro')


def prog1():
    try:
        teste()
    except ErroProg as msg:
        print(msg)
        

prog1()