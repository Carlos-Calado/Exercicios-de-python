try:
    idade = int(input("Digite sua idade: "))
    if idade >= 0:
        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")
    else:
        print("Idade não pode ser negativa.")
except ValueError:
    print("Por favor, digite um número válido para a idade.")
    