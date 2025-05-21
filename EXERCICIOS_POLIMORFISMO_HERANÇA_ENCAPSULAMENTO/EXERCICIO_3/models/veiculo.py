class Veiculo:
    def calcular_consumo(self, distancia: float) -> float:
        raise NotImplementedError("Subclasse")

    def recarregar(self):
        pass

    def unidade_consumo(self) -> str:
        return "litros"
