from datetime import datetime

class Equipamento:
    def __init__(self, id_equipamento: str, tipo: str, data_aquisicao: str):
        self.__id_equipamento = id_equipamento
        self.__tipo = tipo
        self.__estado = "disponível"
        self.__data_aquisicao = datetime.strptime(data_aquisicao, "%Y-%m-%d")
        self.__historico_emprestimos = []

    @property
    def id_equipamento(self):
        return self.__id_equipamento

    @property
    def tipo(self):
        return self.__tipo

    @property
    def estado(self):
        return self.__estado

    def emprestar(self):
        if self.__estado != "disponível":
            raise ValueError("Equipamento não disponível")
        self.__estado = "emprestado"

    def devolver(self):
        if self.__estado != "emprestado":
            raise ValueError("Equipamento não está emprestado")
        self.__estado = "disponível"

    def registrar_emprestimo(self, emprestimo_id):
        self.__historico_emprestimos.append(emprestimo_id)
