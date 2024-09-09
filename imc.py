# IMC
print("Programa para Cálculo de IMC")
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite o sua altura (em metros): "))
imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}.")
print("Classificação do IMC:")
if imc < 18.5:
    print("Abaixo de peso normal.")
elif 18.5 <= imc  < 25:  
    print("Peso normal.")
elif 18.5 <= imc  < 30: 
    print("Sobrepeso.")
elif 18.5 <= imc  < 35: 
    print("Obesidade grau I")
elif 18.5 <= imc  < 40: 
    print("Obesidade grau II.")
else:
    print("Obesidade grau III.")
