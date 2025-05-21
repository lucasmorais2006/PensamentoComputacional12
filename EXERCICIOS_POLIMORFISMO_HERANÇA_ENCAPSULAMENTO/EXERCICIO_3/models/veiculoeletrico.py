from models.veiculo import Veiculo

class VeiculoEletrico(Veiculo):
    def calcular_consumo(self, distancia: float) -> float:
        return distancia * 0.15

    def recarregar(self):
        print("Veículo elétrico recarregado!")

    def unidade_consumo(self) -> str:
        return "kWh"
