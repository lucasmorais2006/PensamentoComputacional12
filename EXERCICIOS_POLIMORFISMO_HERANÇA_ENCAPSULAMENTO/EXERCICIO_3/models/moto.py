from models.veiculo import Veiculo

class Moto(Veiculo):
    def calcular_consumo(self, distancia: float) -> float:
        return distancia / 20

    def unidade_consumo(self) -> str:
        return "litros"

