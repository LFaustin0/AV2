def fatorial(numero):
    total = 1

    for i in range(1, num + 1):       
        total *= i

    print(f"O fatorial de {numero} é {total}")

numero = int(input("Digite um número: "))
fatorial(numero)
