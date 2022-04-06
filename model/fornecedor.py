from model.pessoa import Pessoa


class Fornecedor(Pessoa):
    def __init__(self, nome, funcao, empresa, cpf):
        super().__init__(nome, funcao)
        self.__empresa = empresa
        self.__cpf = cpf

    @property
    def empresa(self):
        return self.__empresa

    @property
    def cpf(self):
        return self.__cpf
