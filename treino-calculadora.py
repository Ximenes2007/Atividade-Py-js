# Função para realizar as operações
def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"

# Entrada do usuário
print("Bem-vindo à calculadora!")
num1 = float(input("Digite o primeiro número: "))
operacao = input("Escolha a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Chamar a função e exibir o resultado
resultado = calcular(num1, num2, operacao)
print(f"O resultado da operação é: {resultado}")