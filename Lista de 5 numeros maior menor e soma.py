print("Iniciando o programa...")

numeros = []
print("Lista de números criada:", numeros)

while len(numeros) < 5:
    print(f"Tamanho atual da lista: {len(numeros)}")
    entrada = input(f"Digite o {len(numeros) + 1}° número inteiro (ou 'sair' para terminar): ")
    print(f"Você digitou: {entrada}")

    if entrada.lower() == 'sair':
        print("Saindo do loop...")
        break

    try:
        numero = int(entrada)
        numeros.append(numero)
        print(f"Número {numero} adicionado à lista.")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

print("Saiu do loop. Lista final:", numeros)

if numeros:
    maior_numero = max(numeros)
    menor_numero = min(numeros)
    soma_total = sum(numeros)

    print("Os números adicionados à lista são:", numeros)
    print("O maior número é:", maior_numero)
    print("O menor número é:", menor_numero)
    print("A soma de todos os números é:", soma_total)
else:
    print("Nenhum número foi adicionado à lista.")

print("Programa finalizado.")
