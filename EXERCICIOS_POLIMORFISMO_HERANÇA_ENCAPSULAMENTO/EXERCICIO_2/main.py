from models.carro import Carro
from models.moto import Moto
from models.frota import Frota
from models.veiculo import Veiculo

frota = Frota()

carro1 = Carro("Chevrolet Onix", 10)
carro2 = Carro("Hyundai I30", 8)
moto1 = Moto("Honda CG", 20)


frota.adicionar_veiculo(carro1)
frota.adicionar_veiculo(carro2)
frota.adicionar_veiculo(moto1)

print("Veículos na frota:")
frota.listar_veiculos()

try:
    distancia = float(input('Qual a distância que será percorrida (em km)? '))  
    if distancia < 0:
        print("Distância inválida!")
    else:
        consumo_total = frota.calcular_consumo_total(distancia)
        print(f"\nConsumo total da frota para {distancia} km: {consumo_total:.2f} litros")  
except ValueError:
    print('Distância inválida. Digite apenas números!')