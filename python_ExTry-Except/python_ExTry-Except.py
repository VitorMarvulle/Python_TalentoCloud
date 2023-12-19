ano = True

while ano:
    print("Digite seu nome: ")
    nome = input()
    try:
        
        print("Digite seu ano de nascimento: ")
        ano_nasc = int(input())

        if ano_nasc >= 1922 and ano_nasc <= 2021:
            ano = False
        else:
            print("O ano digitado é inválido, insira um ano entre 1922 e 2021")
            
    except ValueError:
        print("Erro: Por favor, digite um valor válido.")

print("Seu nome é:", nome)
print("Sua idade é:", 2022 - ano_nasc)
