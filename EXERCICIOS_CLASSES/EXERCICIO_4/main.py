from models.pessoas import Pessoa

nomes = Pessoa("Lucas", 18, 1.75)

nomes.aniversario()

nomes.crescer(0.05)

nomes.exibir_informacoes()