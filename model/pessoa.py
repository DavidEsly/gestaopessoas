class Pessoa:
    def __init__(self, nome, funcao):
        self.__nome = nome
        self.__funcao = funcao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao
