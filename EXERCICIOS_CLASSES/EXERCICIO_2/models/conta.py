class ContaBancaria:
    def __init__(self, titular, saldo, limite, historico, senha):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = []
        self.senha = senha
        self.conta_ativa = True


    def deposito(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Valor do depósito: {valor:.2f}")
            print(f"Valor do depósito: {valor:.2f}")
        else:
            print("Valor de depósito inválido!")
        
    def sacar(self, valor: float):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.historico.append(f"Valor do saque: {valor:.2f}")
            print(f"Valor do saque: {valor:.2f}")
        else:
            print("Saldo Insuficiente!")

    def transferir(self, valor: float, conta_destino):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.append(f"Transferência de {valor:.2f} para {conta_destino.titular}")
            conta_destino.historico.append(f"Transferência de {valor:.2f} recebida de {self.titular}")
            print(f"Transferência de {valor:.2f} para {conta_destino.titular} realizada com sucesso.")
        else:
            print("Saldo Insuficiente!")

    def exibir_historico(self):
        if not self.historico:
            print("Nenhuma transação realizada")
        else:
            for transacao in self.historico:
                print(transacao)

    def exibir_saldo(self):
        limite_disponivel = self.saldo + self.limite
        print(f"Titular da conta: {self.titular}, Saldo Atual: {self.saldo:.2f}, Limite Disponivel: {self.limite:.2f}, Total Disponivel: {limite_disponivel:.2f} ")

    def excluir_conta(self, senha_digitada):
        if senha_digitada == self.senha:
            if self.saldo > 0:
                pergunta_destinatario = input("Deseja transferir o saldo restante para outro destinatário? [s/n] ")
                if pergunta_destinatario == 's' or pergunta_destinatario == 'S':
                    nome_destinatario = input("Digite o nome do destinatário: ")
                    conta_destino = ContaBancaria(nome_destinatario, 0, 0, [], '')
                    valor = self.saldo
                    self.transferir(valor, conta_destino)
                else:
                    print(f"Saldo de {self.saldo:.2f} foi perdido.")
            print(f"Conta de {self.titular} excluída com sucesso.")        
            self.conta_ativa = False
        else:
            print("Senha incorreta. Conta não excluída.")    