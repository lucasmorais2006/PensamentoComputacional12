class MoedaInvalidaError(Exception):
    def __init__(self, mensagem="Moeda inválida. Conversão não realizada."):
        super().__init__(mensagem)