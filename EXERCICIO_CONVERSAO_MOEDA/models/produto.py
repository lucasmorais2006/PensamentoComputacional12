class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = "BRL"

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco: float):
        self.__preco = preco

    def get_moeda(self) -> str:
        return self.__moeda

    def set_moeda(self, moeda: str):
        self.__moeda = moeda

    def __str__(self):
        return f"Produto: {self.__nome} - Preço: {self.__preco:.2f} {self.__moeda}"
