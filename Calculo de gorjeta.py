# Calculo de gorjeta

valor_conta = float(input("Insira o valor da conta: "))
porcentagem_gorjeta = float(input("Insira o valor da gorjeta (%): "))

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    total = valor_conta + gorjeta
    return gorjeta, total

gorjeta, total = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")
print(f"O valor total da conta é: R$ {total:.2f}")