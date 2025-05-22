from models.carro import Carro
from models.moto import Moto
from models.caminhao import Caminhao

lista_veiculos = [Carro(), Moto(), Caminhao()]
try:
    while True:
        distancia = float(input("Digite a distância percorrida (km) ou algum numero negativo para parar: "))
        if distancia < 0:
            print("Programa encerrado.")
            break
        else:
            for veiculo in lista_veiculos:
                consumo = veiculo.calcular_consumo(distancia)
                print(f"{veiculo.__class__.__name__}: {consumo:.2f} litros")
        continue
except ValueError:
    print('Distância inválida. Digite apenas números!')

