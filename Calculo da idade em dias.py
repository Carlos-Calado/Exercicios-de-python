# Calculo da idade em dias


from datetime import date

ano_nascimento = int(input("Digite o ano do seu nascimento: "))

ano_atual = date.today().year
idade_anos = ano_atual - ano_nascimento
idade_dias = idade_anos * 365

print(f"Sua idade equivalente em dias é: {idade_dias} dias.")