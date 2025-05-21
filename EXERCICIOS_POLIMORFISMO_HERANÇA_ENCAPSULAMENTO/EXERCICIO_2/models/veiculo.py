class Veiculo:
    def __init__(self, nome, consumo):
        self.nome = nome
        self.consumo = consumo  

    def calcular_consumo(self, distancia):
        return distancia / self.consumo

    def __str__(self):
        return f"{self.nome} (Consumo: {self.consumo} km/l)"

