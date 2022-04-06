from pessoa import Pessoa


class Colaborador(Pessoa):
    _total = 0

    def __init__(self, nome, funcao, setor, matricula):
        super().__init__(nome, funcao)
        self.__setor = setor
        self.__matricula = matricula
        Colaborador._total += 1

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    @property
    def matricula(self):
        return self.__matricula

    @staticmethod
    def total():
        return Colaborador._total

    def __str__(self):
        return f'Nome:{self.nome} Função:{self.funcao} Matricula:{self.setor} Setor:{self.matricula}'
