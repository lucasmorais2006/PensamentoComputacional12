class Frota:
    def __init__(self):
        self.__veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.__veiculos.append(veiculo)

    def listar_veiculos(self):
        for veiculo in self.__veiculos:
            print(veiculo)

    def calcular_consumo_total(self, distancia):
        total = 0
        for veiculo in self.__veiculos:
            total += veiculo.calcular_consumo(distancia)
        return total
