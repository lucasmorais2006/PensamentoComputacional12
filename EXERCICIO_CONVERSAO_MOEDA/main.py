from models.produtoalimenticio import ProdutoAlimenticio
from models.produtoeletronico import ProdutoEletronico
from models.conversormoeda import ConversorMoeda
from models.moedainvalidaerror import MoedaInvalidaError


nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço em BRL: "))
tipo = input("Digite o tipo do produto (alimenticio ou eletronico): ").lower() #lower auxilia para que reconheça mesmo com diferença de escrita


if tipo == "alimenticio":
    produto = ProdutoAlimenticio(nome, preco)
elif tipo == "eletronico":
    produto = ProdutoEletronico(nome, preco)
else:
    print("Tipo inválido. Criando produto genérico.")
    from models.produto import Produto
    produto = Produto(nome, preco)


conversor = ConversorMoeda()


try:
    convertido = conversor.converte_preco_para_usd(produto)
    if convertido:
        print("Conversão para USD realizada com sucesso.")
    else:
        print("O produto já estava em USD.")
except MoedaInvalidaError as e:
    print(f"Erro na conversão: {e}")


print(produto)
