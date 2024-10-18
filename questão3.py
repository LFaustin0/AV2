n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
operacao = input("Digite '+' para somar \n '-' para subtrair \n '*' para multiplicar \n '/' para dividir: ")

if operacao == '+':
    total = n1 + n2
    print(f"{n1} + {n2} = {total}")

elif operacao == '-':
    total = num1 - num2
    print(f"{n1} - {n2} = {total}")

elif operacao == '*':
    total = num1 * num2
    print(f"{n1} * {n2} = {total}")

elif operacao == '/':
    total = num1 / num2
    print(f"{n1} / {n2} = {total}")

else:
    print("Operação inválida!")
