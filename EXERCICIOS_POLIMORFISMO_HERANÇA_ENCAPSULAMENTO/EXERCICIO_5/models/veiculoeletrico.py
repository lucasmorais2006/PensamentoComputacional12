from models.veiculo import Veiculo

class VeiculoEletrico(Veiculo):
    def __init__(self, modelo, placa):
        super().__init__(modelo, placa)

    def exibir_informacoes(self):
        super().exibir_informacoes()