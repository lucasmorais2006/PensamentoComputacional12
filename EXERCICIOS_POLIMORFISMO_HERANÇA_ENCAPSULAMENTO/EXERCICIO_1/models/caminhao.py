from models.veiculo import Veiculo

class Caminhao(Veiculo):
    def calcular_consumo(self, distancia: float) -> float:
        return distancia / 5
