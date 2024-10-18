def n_primo(numero):
    contador = 0

    for i in range(1, num + 1):
        if num % i == 0:
             contador += 1

    if contador == 2:
        return True
   
    else:
        return False 
    
numero = int(input("Digite um numero: "))
if n_primo(numero):
    print("Número primo!")
else:
    print("Número não primo.")
