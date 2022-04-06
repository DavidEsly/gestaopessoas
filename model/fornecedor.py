from pessoa import Pessoa


class Fornecedor(Pessoa):
    _total = 0

    def __init__(self, nome, funcao, empresa, cpf):
        super().__init__(nome, funcao)
        self.__empresa = empresa
        self.__cpf = cpf
        Fornecedor._total += 1

    @property
    def empresa(self):
        return self.__empresa

    @property
    def cpf(self):
        return self.__cpf

    @staticmethod
    def total():
        return Fornecedor._total

    def __str__(self):
        return f'Nome: {self.nome:<15} Função: {self.funcao:<10} CPF: {self.empresa:<10} Empresa: {self.cpf:<11}'
