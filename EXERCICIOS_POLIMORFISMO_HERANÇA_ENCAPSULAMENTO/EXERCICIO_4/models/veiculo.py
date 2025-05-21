class Veiculo:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.__placa = self.__validar_placa(placa)
        if self.__placa is None:
            raise ValueError("Placa inicial inválida")

    def __validar_placa(self, placa):
        if len(placa) == 7 and placa[:3].isalpha() and placa[:3].isupper() and placa[3:].isdigit():
            return placa
        return None

    def get_placa(self):
        return self.__placa

    def set_placa(self, nova_placa):
        placa_validada = self.__validar_placa(nova_placa)
        if placa_validada:
            self.__placa = placa_validada
            print(f"Placa alterada para: {self.__placa}")
        else:
            print(f"Erro: Placa '{nova_placa}' não segue o padrão brasileiro (3 letras e 4 números).")

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.__placa}")