class Inventario:
    def __init__(self):
        self.__equipamentos = {}

    def adicionar_equipamento(self, equipamento):
        if equipamento.id_equipamento in self.__equipamentos:
            raise ValueError("Equipamento já cadastrado.")
        self.__equipamentos[equipamento.id_equipamento] = equipamento

    def listar_disponiveis(self):
        return [e for e in self.__equipamentos.values() if e.estado == "disponível"]

    def obter_equipamento(self, id_equipamento):
        return self.__equipamentos.get(id_equipamento)
