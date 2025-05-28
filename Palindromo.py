
# Verificação de palindromo

def eh_palindromo(palavra):

    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

texto = input("Digite uma palavra: ")

if eh_palindromo(texto):
    print("Verdadeiro!")
else:
    print("Falso!")