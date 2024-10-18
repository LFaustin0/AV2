import re

def email_ (email):
    if re.search('[@]', email):
        return True

    else:
        return False


email = input("Digite um email: ")
email = "teste@email.com"

if email_ (email):
    print("O email possui @")
else:
    print("O email não possui @")
