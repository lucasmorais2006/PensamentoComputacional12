lista_veiculos = [moto, caminhao, carro]
distancia = float(input("Digite a distância que será percorrida em km's"))
for veiculo in lista_veiculos:
    print(veiculo.calcular_consumo(distancia))
