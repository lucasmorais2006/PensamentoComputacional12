from models.veiculo import Veiculo

class Moto(Veiculo):
    def calcular_consumo(self, distancia: float) -> float:
        return distancia / 20
