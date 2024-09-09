



print("Algoritmo do voto Obrigatório")

nome = input("Digite o seu Nome")
idade = int(input("Digite a sua idade"))

if idade >= 18 and idade < 65:
    print(f"{nome}É maior de idade e pode votar.")
elif 16 <= idade >= 18 and idade < 65:
    print(f"{nome}Seu voto é opcional.")
else:
    print(f"{nome}Não pode votar.")