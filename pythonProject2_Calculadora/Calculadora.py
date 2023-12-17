

# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
#
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(n1,n2,op):
    if op == 1:
        resultado = n1+n2
    elif op == 2:
        resultado = n1-n2
    elif op == 3:
        resultado = n1*n2
    elif op == 4:
        resultado = n1/n2
    else:
        resultado = 0 , "Opção inválida"

    return resultado

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
op = int(input("1 para SOMA // 2 para SUBTRAÇÃO // 3 para MULT // 4 para DIV "))


result = (calculadora(n1,n2,op))
print("O resultado é: ", result)
