def extrato(extrato, saldo):
    print(f'\n {10 * '='} EXTRATO {10*'='}')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:2f}')


def question(frase, escolhas):
    while True:
        try:
            escolha = int(input(frase).strip())
            if escolha in escolhas:
                return escolha
            else:
                print('Por favor, escolha um valor válido')
        except ValueError:
            print('Por favor, insira um número válido')


def saque(saques_diario, saldo, valor_de_saque, extrato, valor_errado=0):
    while True:
        if saques_diario >= 3:
            print('Saques diários excedidos, por favor, volte amanhã')
            break

        if valor_de_saque > saldo:
            print('Saldo não disponível na conta')
            valor_errado = int(input('O saldo na conta é de R${saldo}, deseja fazer o saque com um valor menor tentado?\n[1] - Sim\n[2] - não').strip()[0])
            while valor_errado != 1 and valor_errado != 2:
                valor_errado = int(input('Digite um valor válido\nO saldo na conta é de R${saldo}, deseja fazer o saque com um valor menor tentado?\n[1] - Sim\n[2] - não').strip()[0])
            if valor_errado == 2:
                break
            else:
                valor_de_saque = float(input('Digite o valor que deseja sacar: R$'))

        if valor_de_saque > 500:
            print('Não pode ser sacado mais de R$500 por saque')
            valor_errado = int(input('Deseja fazer o saque com um valor menor tentado?\n[1] - Sim\n[2] - não').strip()[0])
            while valor_errado != 1 and valor_errado != 2:
                valor_errado = int(input('Digite um valor válido\nDeseja fazer o saque com um valor menor tentado?\n[1] - Sim\n[2] - não').strip()[0])
            if valor_errado == 2:
                break
            else:
                valor_de_saque = float(input('Digite o valor que deseja sacar: R$'))

        saldo -= valor_de_saque
        saques_diario += 1
        extrato += f'Saque: \t\tR${valor_de_saque:.2f}\n'

        return saques_diario, saldo, extrato


def deposito(saldo, valor_de_deposito, extrato, /):
    while valor_de_deposito <= 0:
        valor_de_deposito = float(input('Não é possível depositar um valor igual ou inferior a 0, por favor, digite um valor válido'))
    saldo += valor_de_deposito
    extrato += f'Deposito: \tR${valor_de_deposito:.2f}\n'
    return saldo, extrato


def filtrar_usuario(cpf, cadastro2):
    usuarios_filtrados = [usuario for usuario in cadastro2 if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def new_user(cadastro2):
    cpf = input('Digite seu CPF: ')
    usuario = filtrar_usuario(cpf, cadastro2)

    if usuario:
        print("\n Já existe usúario com esse CPF: ")
        return

    nome = input('Digite seu nome: ')
    data_de_nascimento = input('Digite sua data de nascimento: ')
    endereco = input('Digite seu endereço (lofradouro, numero, bairro, cidade - sigla estado)')

    cadastro2.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})
    
    return cadastro2


def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Úsuario não encontrado, fluxo de criação de conta encerrado!")
    return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print('='*100)
        print(linha)