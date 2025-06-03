import re

class Proprietario:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__placas = []  # Lista de placas dos veículos adquiridos
    
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_placas(self):
        return self.__placas
    
    def validar_cpf(self):
        # Validação simples do CPF: deve ter 11 dígitos numéricos
        cpf = re.sub(r'[^0-9]', '', self.__cpf)
        return len(cpf) == 11 and cpf.isdigit()
    
    @staticmethod
    def validar_placa(placa):
        # Validação básica placa (mesma usada no sistema)
        regex_placa = r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$'
        return re.match(regex_placa, placa.upper()) is not None
    
    def adicionar_veiculo(self, placa):
        if not self.validar_placa(placa):
            raise ValueError("Placa inválida.")
        if placa not in self.__placas:
            self.__placas.append(placa)
    
    def __str__(self):
        return f"{self.__nome} (CPF: {self.__cpf}) - Veículos: {', '.join(self.__placas) if self.__placas else 'Nenhum'}"
