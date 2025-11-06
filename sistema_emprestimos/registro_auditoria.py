from datetime import datetime

class RegistroAuditoria:
    def __init__(self):
        self.__entradas = []

    def registrar(self, acao: str, usuario):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__entradas.append(f"[{timestamp}] {usuario.nome} - {acao}")

    @property
    def entradas(self):
        return self.__entradas.copy()
