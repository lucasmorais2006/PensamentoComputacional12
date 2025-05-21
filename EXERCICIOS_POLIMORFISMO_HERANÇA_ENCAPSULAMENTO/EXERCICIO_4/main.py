from models.veiculo import Veiculo

if __name__ == "__main__":
    try:
        teste_veiculo = Veiculo("Onix", "ABC1234")
        teste_veiculo.exibir_informacoes()

        print("\nTentando alterar a placa:")
        teste_veiculo.set_placa("DEF5678")
        teste_veiculo.exibir_informacoes()

        teste_veiculo.set_placa("GHIJ901")
        teste_veiculo.exibir_informacoes()

        teste_veiculo.set_placa("JKL90123")
        teste_veiculo.exibir_informacoes()

        teste_veiculo.set_placa("MNO-3456")
        teste_veiculo.exibir_informacoes()

        teste_veiculo.set_placa("PQR7890")
        teste_veiculo.exibir_informacoes()

    except ValueError as e:
        print(f"Erro ao criar veículo: {e}")