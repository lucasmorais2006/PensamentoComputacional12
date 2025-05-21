from models.carro import Carro
from models.moto import Moto
from models.veiculoeletrico import VeiculoEletrico 

lista_veiculos = [Carro(), Moto(), VeiculoEletrico()]
distancia = float(input("Digite a distância percorrida (km): "))

for veiculo in lista_veiculos:
    consumo = veiculo.calcular_consumo(distancia)
    print(f"{veiculo.__class__.__name__}: {consumo:.2f} litros")
