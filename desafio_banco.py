from time import sleep
menu= f"""
{30 * '-'}
Seja bem-vindo ao banco DIO
{30 * '-'}
Selecione a alternativa da operação desejada
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair

->
"""
escolhas = (1, 2, 3, 4)
saldo = 0
deposito = 0
saque = 0
saques_diarios = 0
saque_invalido = 0
while True:
    escolha = int(input(menu).strip())
    while escolha not in escolhas:
        print('Por favor, escolha um valor válido')
        escolha = int(input(menu).strip())
    
    if escolha == 1:
        valor_deposito = float(input('Digite o valor que deseja depositar: '))
        while valor_deposito <= 0:
            print('Por favor, digite um número válido')
            valor_deposito = float(input('Digite o valor que deseja depositar: '))
        saldo += valor_deposito
        deposito += valor_deposito

    
    elif escolha == 2:
        if saques_diarios >= 3:
            print('saques diários excedido, por favor, volte amanhã')
            break
        else:    
            valor_de_saque = float(input('Digite o valor que deseja sacar: '))
            while valor_de_saque > 500 or valor_de_saque < 0:
                if valor_de_saque > 500:
                    print('Saque não pode ser maior que R$500')
                valor_de_saque = float(input('Valor de saque inválido, por favor, digite um valor válido: '))
            while valor_de_saque > saldo:
                print(f'Não será possivel sacar o dinheiro por falta de saldo, seu saldo atual é de R${saldo}')
                saque_invalido = int(input('Digite sua escolha\n[1] - Deseja sair\n[2]- Sacar um valor válido').strip())
                if saque_invalido == 1:
                    break
                elif saque_invalido == 2:
                    valor_de_saque = float(input('Valor de saque inválido, por favor, digite um valor válido: '))
            if saque_invalido == 1:
                break
            saldo -= valor_de_saque
            saque += valor_de_saque
            saques_diarios += 1
    
    elif escolha == 3:
        if saque <= 0 or deposito <= 0:
            print('Não houve movimentação na conta')
        else:
            print(f'Foram depositados R${deposito:.2f} e sacadados R${saque:.2f}')
        sleep(2)
    else:
        break