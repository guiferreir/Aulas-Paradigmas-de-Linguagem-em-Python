from datetime import datetime

class Emprestimo:
    def __init__(self, id_emprestimo: str, usuario, equipamento, data_devolucao_prevista: str):
        if not usuario.pode_emprestar():
            raise ValueError("Usuário não pode realizar novo empréstimo.")

        equipamento.emprestar()
        usuario.registrar_emprestimo()

        self.__id_emprestimo = id_emprestimo
        self.__usuario = usuario
        self.__equipamento = equipamento
        self.__data_inicio = datetime.now()
        self.__data_devolucao_prevista = datetime.strptime(data_devolucao_prevista, "%Y-%m-%d")
        self.__ativo = True

        equipamento.registrar_emprestimo(id_emprestimo)

    def encerrar(self):
        if not self.__ativo:
            raise ValueError("Empréstimo já encerrado.")
        self.__ativo = False
        self.__equipamento.devolver()
        self.__usuario.encerrar_emprestimo()

    @property
    def ativo(self):
        return self.__ativo

    @property
    def usuario(self):
        return self.__usuario

    @property
    def equipamento(self):
        return self.__equipamento
