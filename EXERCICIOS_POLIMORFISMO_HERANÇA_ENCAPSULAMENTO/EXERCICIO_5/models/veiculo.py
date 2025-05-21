class Veiculo:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.__placa = placa

    def get_placa(self):
        return self.__placa

    def set_placa(self, nova_placa):
        self.__placa = nova_placa
        print(f"Placa alterada para: {self.__placa}")

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.__placa}")

    def __eq__(self, outro):
        if isinstance(outro, Veiculo):
            return self.__placa == outro.get_placa()
        return False 