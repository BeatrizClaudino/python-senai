from Banco import SENAIBANK

print('Bem-vindo ao banco SenaiBank! ')
nome = input('Digite seu primeiro nome: ')
cpf = input('Digite o CPF: ')
idade = int(input('Digite a idade: '))

conta = SENAIBANK(nome=nome, cpf=cpf, idade=idade)

opcao = int(input('''Opções de transações disponiveis: 
      [1] Saque
      [2] Depositar
      [3] Transferir
      [4] Extrato'''))

if opcao == 1:
     valor = float(input('Digite o valor que deseja sacar: '))
     conta.efetivar_saque(valor_saque=valor)
     if conta.sacar(valor_saque=valor):
          print(f'Transação aceita. '
                f'O seu saldo é de {conta.efetivar_saque(valor_saque=valor)}')
     else:
          print(f'Transação não aceita. '
                f'O seu saldo é de {conta.extrato()} ')

if opcao == 2:
     valor = int(input('Digite o valor que deseja depositar: '))
     print(conta.depositar(valor_deposito=valor))
if opcao == 3:
    valor = int(input('Digite o valor que deseja transferir: '))
    destinatario = int(input('Insira a conta de destino: '))
    print(f'''Transação aceita!
Seu saldo é de {conta.transferir(valor_transferido=valor)}R$''')
if opcao ==4:
    pass