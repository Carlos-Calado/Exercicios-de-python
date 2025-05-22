#1- Classificador de Idade

idade = int(input("Digite sua idade: "))        #Inserir a idade

if idade <= 0:
    print("Valor inserido não é válido.")
else:
    if idade <= 12:
        print("Você é uma criança.")
    else:
        if idade <= 17:
            print("Você é um adolescente.")
        else:
            if idade <= 59:
                print("Você é um adulto.")
            else:
                print("Você é um idoso.")
        
#2- Calculadora de IMC

peso = int(input("Digite seu peso: "))        #Inserir o peso
altura = float(input("Digite sua altura: "))        #Inserir a altura
imc = peso/(altura*altura)


if imc < 18.5:
    print("Você esta abaixo do peso.")
else:
    if imc < 25:
        print("Você esta com o peso normal.")
    else:
        if idade < 30:
           print("Você esta com sobre peso.")
        else:
            print("Você esta obeso.")

#3- Conversor de Temperatura

temperatura = float(input("Digite o valor da temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

resultado = None

if origem == destino:
    resultado = temperatura
else:
    if origem == "C" and destino == "F":
        resultado = (temperatura * 9/5) + 32
    else:
        if origem == "C" and destino == "K":
            resultado = temperatura + 273.15
        else:
            if origem == "F" and destino == "C":
                resultado = (temperatura - 32) * 5/9
            else:
                if origem == "F" and destino == "K":
                    resultado = (temperatura - 32) * 5/9 + 273.15
                else:
                    if origem == "K" and destino == "C":
                        resultado = temperatura - 273.15
                    else:
                        if origem == "K" and destino == "F":
                            resultado = (temperatura - 273.15) * 9/5 + 32
                        else:
                            print("Unidade inválida! Use apenas C, F ou K.")

# Saída
if resultado is not None:
    print(f"{temperatura} {origem} é igual a {resultado:.2f} {destino}")

#4- Verificador de Ano Bissexto

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} NÃO é bissexto.")
    else:
        print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} NÃO é bissexto.")