from models.veiculo import Veiculo
from models.moto import Moto
from models.veiculoeletrico import VeiculoEletrico

if __name__ == "__main__":
    veiculos = [
        Veiculo("Onix 1", "ABC1234"),
        Moto("XRE 1", "DEF5678"),
        VeiculoEletrico("BYD 1", "GHI9012"),
        Veiculo("Cruze 1", "ABC1234"),  
        Moto("XRE 2", "JKL3456"),
        VeiculoEletrico("BYD 2", "DEF5678"), 
        Veiculo("Onix 2", "MNO7890"),
        Veiculo("Cruze 2", "PQR1234"), 
    ]

    placas_vistas = set()
    placas_duplicadas = set()
    veiculos_por_placa = {}

    for veiculo in veiculos:
        placa = veiculo.get_placa()
        if placa in placas_vistas:
            placas_duplicadas.add(placa)
        else:
            placas_vistas.add(placa)
        if placa not in veiculos_por_placa:
            veiculos_por_placa[placa] = []
        veiculos_por_placa[placa].append(veiculo)

    print("--- Placas Duplicadas Encontradas ---")
    if placas_duplicadas:
        for placa_duplicada in placas_duplicadas:
            print(f"Placa: {placa_duplicada}")
            for veiculo in veiculos_por_placa[placa_duplicada]:
                veiculo.exibir_informacoes()
                print("---")
    else:
        print("Nenhuma placa duplicada encontrada.")