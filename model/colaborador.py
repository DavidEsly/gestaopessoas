from model.pessoa import Pessoa


class Colaborador(Pessoa):
    def __init__(self, nome, funcao, setor, matricula):
        super().__init__(nome, funcao)
        self.__setor = setor
        self.__matricula = matricula

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    @property
    def matricula(self):
        return self.__matricula
