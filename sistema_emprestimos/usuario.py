class Usuario:
    def __init__(self, id_usuario: str, nome: str, tipo: str):
        if tipo not in ("aluno", "professor", "tecnico"):
            raise ValueError("Tipo de usuário inválido.")
        self.__id_usuario = id_usuario
        self.__nome = nome
        self.__tipo = tipo
        self.__emprestimos_ativos = 0

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    def pode_emprestar(self):
        if self.__tipo == "aluno":
            return self.__emprestimos_ativos < 1
        return self.__emprestimos_ativos < 3

    def registrar_emprestimo(self):
        if not self.pode_emprestar():
            raise ValueError(f"Usuário {self.__nome} não pode pegar mais equipamentos.")
        self.__emprestimos_ativos += 1

    def encerrar_emprestimo(self):
        if self.__emprestimos_ativos > 0:
            self.__emprestimos_ativos -= 1
