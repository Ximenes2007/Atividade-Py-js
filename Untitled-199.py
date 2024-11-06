def exibirmensagem(nome, idade):
    print(f"Olá, {nome} com {idade} anos!")

def somar (a,b):
    return a + b

def calcularareacirculo(raio):
    area = 3.1415 * raio**2
    return area
 
nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
exibirmensagem(nome, idade)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = somar(a, b)
print(f"O resultado da soma é: {resultado}")

print("Área do círculo!!")
raio = float(input("digite o valor do raio: "))
area = calcularareacirculo(raio)
print(f"A área do círculo é: {area:.2f} cm²")