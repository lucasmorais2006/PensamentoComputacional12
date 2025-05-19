def calcular_consumo(self, distancia) -> str:
        """
        Método que cálcula o consumo de combustível do carro
        """
        calculo_consumo = distancia / 5
        return f"O consumo do caminhão foi de {round(calculo_consumo, 2)} litros"
        
    
