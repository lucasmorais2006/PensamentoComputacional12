from models.veiculo import Veiculo

class Carro(Veiculo):
    def calcular_consumo(self, distancia: float) -> float:
        return distancia / 12
