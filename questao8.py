from random import randint

lista = []

for i in range(0, 10):
    num = randint(1, 50)
    lista.append(num)

def somar_(lista):
    total = 0

    for i in lista:
        total += i

    print(f"A soma dos numeros da lista é: {total}")

print(lista)
somar_(lista)
