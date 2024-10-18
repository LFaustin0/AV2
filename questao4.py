def calculadora(n1, n2, operacao):
    if operacao == '+':
        total = n1 + n2
        print(f"{n1} + {n2} = {total}")

    elif operacao == '-':
        total = n1 - n2
        print(f"{n1} - {n2} = {total}")

    elif operacao == '*':
        total = n1 * n2
        print(f"{n1} * {n2} = {total}")

    elif operacao == '/':
        total = n1 / n2
        print(f"{n1} / {n2} = {total}")

    else:
        print("Operação inválida!")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
operacao = input("Digite '+' para somar, '-' para subtrair, '*' para multiplicar ou '/' para dividir: ")

calculadora(num1, num2, operacao)
