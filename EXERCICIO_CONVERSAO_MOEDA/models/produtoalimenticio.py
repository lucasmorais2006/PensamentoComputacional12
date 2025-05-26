from models.produto import Produto

class ProdutoAlimenticio(Produto):
    def __str__(self):
        return f"Produto Alimentício: {self.get_nome()} - Preço: {self.get_preco():.2f} {self.get_moeda()}"
