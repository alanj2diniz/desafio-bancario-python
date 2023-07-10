menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(opcao, valor):
    if valor > 0:
        global saldo, extrato
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido!")

def sacar(opcao, valor):
    global saldo, extrato, numero_saques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    
    else:
        print("Operação falhou! O valor informado é inválido.")

def imprimeExtrato():
    print("\n============ EXTRATO ============")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo: {saldo:.2f}")
    print("====================================")

def obterValor(tipoOperacao):
    return float(input(f"Informe o valor do {tipoOperacao}: "))

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = obterValor("depósito")
        depositar(opcao, valor)

    elif opcao == "s":
        valor = obterValor("saque")
        sacar(opcao, valor)

    elif opcao == "e":
        imprimeExtrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
