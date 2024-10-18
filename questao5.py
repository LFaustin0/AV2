import re

def vogais_(string):
    total = re.findall('[aeiou]', string)
    return len(total)

string = input("Digite algo: ")
print(f"Vogais: {vogais_(string)}")
