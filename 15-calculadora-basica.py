opcao = 0

while opcao != 6:
    print("CALCULADORA DAS OPERAÇÕES BÁSICAS:\n")
    print("Menu de escolha:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da Divisão")
    print("6. Sair")

    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        n1 = int(input("Insira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
        print(f"A soma dos valores é: {n1 + n2}\n")
    elif opcao == 2:
        n1 = int(input("Insira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
        print(f"A subtração dos valores é: {n1 - n2}\n")
    elif opcao == 3:
        n1 = int(input("Insira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
        print(f"A multiplicação dos valores é: {n1 * n2}\n")
    elif opcao == 4:
        if n2 != 0:
            n1 = int(input("Insira o primeiro valor: "))
            n2 = int(input("Insira o segundo valor: "))
            print(f"A divisão dos valores é: {n1 / n2}\n")
        else:
            print("Erro: Divisão por zero não é permitida.\n")
    elif opcao == 5:
        if n2 != 0:
            n1 = int(input("Insira o primeiro valor: "))
            n2 = int(input("Insira o segundo valor: "))
            print(f"O resto da divisão dos valores é: {n1 % n2}\n")
        else:
            print("Erro: Divisão por zero não é permitida.\n")
    elif opcao == 6:
        print("Finalizando o código!")
    else:
        print("Opção inválida. Tente novamente.\n")