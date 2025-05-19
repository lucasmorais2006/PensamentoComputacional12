from models.conta import ContaBancaria
nome = input('Digite seu nome completo para criar a sua conta: ') 
senha = input('Digite uma senha para sua conta: ')
conta1 = ContaBancaria(nome, 0, 1000.0, [], senha)
#conta2 = ContaBancaria(input('Digite o nome completo do destinatário da sua transfêrencia: '), 0, 1000.0, [])

#depósito
conta1.saldo = float(input(f'Quantos R$ gostaria de depositar como saldo inicial de sua conta? '))
pergunta_deposito = input(f'Desea realizar um depósito? [s/n] ')
if pergunta_deposito == 's' or pergunta_deposito == 'S':
    pergunta_deposito_valor = float(input('Quantos R$ deseja depositar? '))
    conta1.deposito(pergunta_deposito_valor)
else:
    pass
#saque
pergunta_saque = input(f'Deseja realizar um saque? [s/n] ')
if pergunta_saque == 's' or pergunta_saque == 'S':
    pergunta_saque_valor = float(input('Quantos R$ deseja sacar? '))
    conta1.sacar(pergunta_saque_valor)
else:
    pass
#TRANSFERENCIA
pergunta_transferencia = input(f'Deseja realizar uma transferência? [s/n] ')
if pergunta_transferencia == 's' or pergunta_transferencia == 'S':
    nome_destinatario = input('Digite o nome do destinatário da transferência: ')
    conta2 = ContaBancaria(nome_destinatario, 1000.0, 5000.0, [], '')  # destinatário não tem senha
    valor_transferencia = float(input(f'Qual o valor em R$ da transferência? '))
    senha_informada = input(f'Insira a senha da sua conta para confirmar: ')
    if senha_informada == conta1.senha:
        conta1.transferir(valor_transferencia, conta2)
    else:
        print("Senha incorreta! Transferência não realizada.")
        pass
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
# excluir conta
pergunta_excluir = input('Deseja excluir sua conta? [s/n] ')
if pergunta_excluir == 's' or pergunta_excluir == 'S':
    senha_digitada = input('Digite sua senha para confirmar: ')
    conta1.excluir_conta(senha_digitada)
else:
    pass