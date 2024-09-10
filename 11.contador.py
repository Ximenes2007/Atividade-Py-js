contador = 0
numero = int(input("Digite um valor da tabuada: "))

while (numero <= 10):
    resultado = numero * contador
    print(f"{numero} X {contador} = {resultado}")
    numero += 1