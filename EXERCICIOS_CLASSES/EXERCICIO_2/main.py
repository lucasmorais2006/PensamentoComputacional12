from models.conta import ContaBancaria
conta1 = ContaBancaria(input('Digite seu nome completo para criar a sua conta: '), 0, 1000.0, [])
#conta2 = ContaBancaria(input('Digite o nome completo do destinatário da sua transfêrencia: '), 0, 1000.0, [])

#depósito
conta1.saldo = float(input(f'Quantos R$ gostaria de depositar como saldo inicial de sua conta? '))
pergunta_deposito = input(f'Desea realizar um depósito? [s/n] ')
if pergunta_deposito == 's' or pergunta_deposito == 'S':
    pergunta_deposito_valor = (float(input((f'Quantos R$ deseja depositar? '))))
    conta1.deposito = (pergunta_deposito_valor)
else:
    pass
#saque
pergunta_saque = input(f'Deseja realizar um saque? [s/n] ')
if pergunta_saque == 's' or pergunta_saque == 'S':
    pergunta_saque_valor = float(input(f'Quantos R$ deseja sacar? '))
    conta1.sacar = (pergunta_saque_valor)
else:
    pass
#TRANSFERENCIA
pergunta_transferencia = input(f'Deseja realizar uma transferência? [s/n] ')
if pergunta_transferencia == 's' or pergunta_transferencia == 'S':
    conta2 = ContaBancaria(input(f'Digite o nome completo do remetente para realizar sua tranferência: '),1000.0, 5000.0, [])
    pergunta_transferencia_2 = float(input(f'Qual o valor em R$ da transferência? '))
    conta1.transferir(pergunta_transferencia_2, conta2)
else:
    pass
pergunta_historico = input(f'Deseja exibir o histórico da conta? [s/n] ')
if pergunta_historico == 's' or pergunta_historico == 'S':
    #EXIBIR HISTORICO
    conta1.exibir_historico()
else:
    pass
pergunta_saldo = input(f'Deseja exibir o saldo da conta? [s/n]' )
if pergunta_saldo == 's' or pergunta_saldo =='S':
    #EXIBIR SALDO
    conta1.exibir_saldo()
else:
    pass