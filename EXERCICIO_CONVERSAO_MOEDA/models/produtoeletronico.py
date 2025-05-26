from models.produto import Produto

class ProdutoEletronico(Produto):
    def __str__(self):
        return f"Produto Eletrônico: {self.get_nome()} - Preço: {self.get_preco():.2f} {self.get_moeda()}"
