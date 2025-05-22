from models.carro import Carro
from models.moto import Moto
from models.veiculoeletrico import VeiculoEletrico

lista_veiculos = [Carro(), Moto(), VeiculoEletrico()]
try:
    distancia = float(input("Digite a distância percorrida (km): "))
    if distancia < 0:
        print('Distância inválida')
    else:
        for veiculo in lista_veiculos:
            consumo = veiculo.calcular_consumo(distancia)
            veiculo.recarregar()
            print(f"{veiculo.__class__.__name__}: {consumo:.2f} {veiculo.unidade_consumo()}")
except ValueError:
    print('Distância inválida! Digite apenas números')
