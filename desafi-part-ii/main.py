import funcoes_banco as fb
# Para ver todos os cadastros, utilizar a função get_cadastros

frase = f"""
{30 * '-'}
Seja bem-vindo ao banco DIO
{30 * '-'}
Selecione a alternativa da operação desejada
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Criar conta de usúario
[5] - Criar conta corrente
[6] - Listar contas
[7] - Sair

->
"""
AGENCIA = '0001'
conta_corragem = []

ext = ""
saldo = 0
sd = 0
usuarios = []
escolhas = (1, 2, 3, 4, 5, 6, 7)
while True:
    escolha = fb.question(frase, escolhas)
    if escolha == 1:
        valor = float(input('Digite o valor que deseja depositar: R$'))
        saldo, ext = fb.deposito(saldo, valor, ext)
        print(saldo)
        print(ext)

    
    if escolha == 2:
        vs = float(input('Digite o valor que você quer sacar: R$'))
        saldo, sd, ext = fb.saque(sd, saldo, vs, ext)
        
    
    if escolha == 3:
        fb.extrato(ext, saldo)
    
    if escolha == 4:
        usuarios = fb.new_user(usuarios)
        
    
    if escolha == 5:
        numero_conta = len(conta_corragem) + 1
        conta = fb.criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            conta_corragem.append(conta)
        
    if escolha == 6:
        fb.listar_contas(conta_corragem)

    if escolha == 7:
        break