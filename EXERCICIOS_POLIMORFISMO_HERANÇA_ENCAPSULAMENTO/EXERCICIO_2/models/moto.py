from models.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, nome, consumo):
        super().__init__(nome, consumo)
