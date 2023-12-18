def calculadora(n1,n2,op):
    if op == 1:
        resultado = n1+n2
    elif op == 2:
        resultado = n1-n2
    elif op == 3:
        resultado = n1*n2
    elif op == 4:
        resultado = n1/n2

    return resultado

op=1
while (op != 0):
  op = int(input("1 para SOMA // 2 para SUBTRAÇÃO // 3 para MULT // 4 para DIV // 0 para SAIR  "))
  if op==0:
    print("Você encerrou o loop")
    break
  elif op > 4:
    print("Opção inválida, digite novamente: ")
    op = int(input("1 para SOMA // 2 para SUBTRAÇÃO // 3 para MULT // 4 para DIV // 0 para SAIR  "))

  n1 = int(input("Digite o primeiro número: "))
  n2 = int(input("Digite o segundo número: "))

  result = (calculadora(n1,n2,op))
  print("O resultado é: ", result)