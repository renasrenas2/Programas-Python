print("\n=== SISTEMA DE BANCO ===")

saldo = 1000.0
print(f"Seu saldo inicial é de: R$ {saldo}")

while True:
    print("[MENU]")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Sair")
    opcao = input("Digite qual opção você deseja realizar: ")

    if opcao == "1":
        valor = float(input("Digite o valor que você deseja depositar: "))
        saldo += valor
        print("\nDepósito realizado com sucesso!\n")
    elif opcao == "2":
        valor = float(input("Digite o valor que você deseja sacar: "))
        if valor < 0:
            print("\nValor de saque inválido. Digite novamente.\n")
        elif valor > saldo:
            print("\nValor inválido. Digite novamente.\n")
        saldo -= valor
        print("\nSaque realizado com sucesso!\n")
    elif opcao == "3":
        print(f"\nSeu saldo atual é de: {saldo}\n")
    elif opcao == "4":
        print("\nObrigado por usar o nosso sistema!\n")
        break
    else:
        print("\nOpção inválida! Digite novamente.\n")

    
        