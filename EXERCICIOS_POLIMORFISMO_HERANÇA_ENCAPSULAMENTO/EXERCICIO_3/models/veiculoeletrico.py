from models.veiculo import Veiculo

class VeiculoEletrico(Veiculo):
    def calcular_consumo(self, distancia: float) -> float:
        return distancia / 5
