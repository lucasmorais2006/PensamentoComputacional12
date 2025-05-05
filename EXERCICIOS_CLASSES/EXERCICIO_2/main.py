from models.conta import ContaBancaria
conta1 = ContaBancaria("Lucas", 2400.0, 1000.0, [])
conta2 = ContaBancaria("Francisco", 15000.0, 5000.0, [])

#depósito
conta1.deposito(780.0)
print(conta1.historico)

#saque
conta1.sacar(300.0)
print(conta1.historico)

#TRANSFERENCIA

conta1.transferir(100.0, conta2)

print(f"Saldo Lucas: {conta1.saldo:.2f}")
print(f"Saldo Francisco: {conta2.saldo:.2f}")
print("Histórico Lucas:", conta1.historico)
print("Histórico Francisco:", conta2.historico)


#EXIBIR HISTORICO
conta1.exibir_historico()

#EXIBIR SALDO
conta1.exibir_saldo()