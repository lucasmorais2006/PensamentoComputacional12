from models.moedainvalidaerror import MoedaInvalidaError
from models.produto import Produto

class ConversorMoeda:
    def __init__(self):
        self.__usd_brl = 5.05
        self.__eur_brl = 6.14
        self.__eur_usd = 1.22

    def converte_preco_para_usd(self, produto: Produto) -> bool:
        moeda = produto.get_moeda()
        preco = produto.get_preco()

        if moeda == "USD":
            return False
        elif moeda == "BRL":
            produto.set_preco(preco / self.__usd_brl)
            produto.set_moeda("USD")
            return True
        elif moeda == "EUR":
            produto.set_preco(preco / self.__eur_usd)
            produto.set_moeda("USD")
            return True
        else:
            raise MoedaInvalidaError()

    def converte_preco_para_eur(self, produto: Produto) -> bool:
        moeda = produto.get_moeda()
        preco = produto.get_preco()

        if moeda == "EUR":
            return False
        elif moeda == "BRL":
            produto.set_preco(preco / self.__eur_brl)
            produto.set_moeda("EUR")
            return True
        elif moeda == "USD":
            produto.set_preco(preco * self.__eur_usd)
            produto.set_moeda("EUR")
            return True
        else:
            raise MoedaInvalidaError()

    def converte_preco_para_brl(self, produto: Produto) -> bool:
        moeda = produto.get_moeda()
        preco = produto.get_preco()

        if moeda == "BRL":
            return False
        elif moeda == "USD":
            produto.set_preco(preco * self.__usd_brl)
            produto.set_moeda("BRL")
            return True
        elif moeda == "EUR":
            produto.set_preco(preco * self.__eur_brl)
            produto.set_moeda("BRL")
            return True
        else:
            raise MoedaInvalidaError()
